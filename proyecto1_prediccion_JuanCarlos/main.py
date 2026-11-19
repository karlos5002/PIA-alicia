import os
from contextlib import asynccontextmanager
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from preprocesamiento import preparar_datos_crudos
from schemas import ClienteInput, PrediccionOutput

artefactos = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    ruta_prep = os.path.join("artifacts", "preprocesador_banca.joblib")
    ruta_modelo = os.path.join("artifacts", "modelo_knn.joblib")

    if not os.path.exists(ruta_prep) or not os.path.exists(ruta_modelo):
        raise RuntimeError("No se encuentran los archivos .joblib en 'artifacts/'.")

    artefactos['preprocesador'] = joblib.load(ruta_prep)
    artefactos['modelo'] = joblib.load(ruta_modelo)
    yield
    artefactos.clear()

app = FastAPI(
    title="API de Predicción de Abandono de Clientes",
    description="Microservicio para evaluar el riesgo de fuga integrando ColumnTransformer y KNN.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", tags=["Frontend"])
def servir_frontend():
    ruta_html = os.path.join("templates", "index.html")
    if os.path.exists(ruta_html):
        return FileResponse(ruta_html)
    return {"mensaje": "API activa. Visita /docs para Swagger UI."}

@app.post("/predict", response_model=PrediccionOutput, tags=["Inferencia"])
def predecir_abandono(cliente: ClienteInput):
    try:
        datos_dict = cliente.model_dump()
        df_crudo = pd.DataFrame([datos_dict])

        df_saneado = preparar_datos_crudos(df_crudo)

        preprocesador = artefactos['preprocesador']
        X_inferencia = preprocesador.transform(df_saneado)

        modelo = artefactos['modelo']
        prediccion_clase = int(modelo.predict(X_inferencia)[0])
        probabilidades = modelo.predict_proba(X_inferencia)[0]
        prob_abandono = float(probabilidades[1])

        if prob_abandono >= 0.70:
            riesgo = "Alto"
            accion = "Contacto telefónico prioritario por el gestor de cuentas y oferta de fidelización."
        elif prob_abandono >= 0.40:
            riesgo = "Medio"
            accion = "Envío de encuesta de satisfacción y campaña informativa sobre ventajas en comisiones."
        else:
            riesgo = "Bajo"
            accion = "Sin acción requerida. Cliente fidelizado."

        return PrediccionOutput(
            id_cliente=cliente.id_cliente,
            abandono=prediccion_clase,
            probabilidad_abandono=round(prob_abandono, 4),
            nivel_riesgo=riesgo,
            accion_recomendada=accion
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en inferencia: {str(e)}")