from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


class CancerPulmon(BaseModel):
    nombre: str = Field(min_length=1, max_length=50, description="Nombre del solicitante")
    edad_actual: int = Field(ge=18, le=120, description="Edad del solicitante" )
    cigarrillos_por_dia: int = Field(ge=1, le=100, description="Cantidad de cigarrillos que fuma al dia")
    anos_fumando: int = Field(ge=1, le=100, description="Cantidad de años que ha fumado")
    anos_sin_fumar: int = Field(ge=0, le=100, description="Cantidad de años que lleva sin fumar")


class ResultadoFumar(BaseModel):
    solicitante: str
    riesgo_cancer_pulmon: str
    recomendacion: str


app = FastApi(
    title="API de riesgo de cancer de pulmon",
    description="Esta API permite calcular el riesgo de cancer de pulmon basado en los habitos de fumar del solicitante.",
    version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=FileResponse)
def inicio():
    return FileResponse("index.html")

@app.post("/calcular_riesgo", response_model=ResultadoFumar)
def calcular_riesgo(cancer_pulmon: CancerPulmon):
       
    """Calcula el riesgo de cancer de pulmon basado en los habitos
    de fumar del solicitante."""
    # Calcular el riesgo de cancer basado en los habitos de fumar del solicitante
    
    paquetes_anos = (cancer_pulmon.cigarrillos_por_dia / 20) * cancer_pulmon.anos_fumando
    score = 70
    if cancer_pulmon.edad_actual < 30:
        score -= 10
    elif cancer_pulmon.edad_actual < 50:
        score -= 5
    if paquetes_anos > 20:
        score += 20
    elif paquetes_anos > 10:
        score += 10
    if cancer_pulmon.anos_sin_fumar > 5:
        score -= 10
    elif cancer_pulmon.anos_sin_fumar > 2:
        score -= 5

    score = max(0, min(score, 100, round(score, 1)))

    aprobacion = "Alto" if score >= 70 else "Medio" if score >= 40 else "Bajo"
    motivo = "Se recomienda ir al medico para una evaluacion mas detallada"
    if aprobacion == "Bajo":
        motivo = "Se recomienda ser saludable y evitar el consumo de tabaco"
    if aprobacion == "Medio":
        motivo = "Se recomienda ir al medico para una evaluacion mas detallada y considerar dejar de fumar"    
    if aprobacion == "Alto":
        motivo="Se recomienda encarecidamente ir al medico y dejar de fumar cuanto antes"    

    return ResultadoFumar(
        "solicitante": cancer_pulmon.nombre,
        "recomendacion": motivo,
        "score": score,
        "riesgo de cancer de pulmon": aprobacion
    )