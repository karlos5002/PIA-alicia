from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field



class CancerPulmon(BaseModel):
    nombre: str = Field(min_length=1, max_length=50, description="nombre del solicitante")
    edad_actual: int = Field(ge=18, le=120, description="edad del solicitante")
    cigarrillos_por_dia: int = Field(ge=1, le=100, description="cantidad de cigarrillos que fuma al dia")
    anos_fumando: int = Field(ge=1, le=100, description="cantidad de años que ha fumado")
    anos_sin_fumar: int = Field(ge=0, le=100, description="cantidad de años que lleva sin fumar")
    exposicion_humo: bool = Field(default=False, description="convive  con fumadores?")

class ResultadoFumar(BaseModel):
    solicitante: str
    riesgo_cancer_pulmon: str
    score: float 
    recomendacion: str



app = FastAPI(
    title="API de Riesgo de cancer de pulmon",
    description="esta API permite calcular el riesgo de cancer basado en los hábitos de fumar del solicitante",
    version="1.0.0"
)

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

@app.get("/api/info")
def informacion_api():
    return {
        "estado": "Operativo",
        "servicio": "Evaluación de Riesgo Pulmonar",
        "version": "1.0.0",
    }

@app.post("/api/calcular_riesgo", response_model=ResultadoFumar)
def calcular_riesgo(cancer_pulmon: CancerPulmon):
    """
    Calcula el riesgo de cancer de pulmon basado en los habitos de fumar del solicitante.
    """
    paquetes_anos = (cancer_pulmon.cigarrillos_por_dia / 20) * cancer_pulmon.anos_fumando
    
    # Motor de Scoring
    score = 10.0
    
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
        
    if cancer_pulmon.exposicion_humo:
        score += 15

    score = max(0.0, min(100.0, round(score, 1)))

    aprobacion = "Alto" if score >= 70 else "Medio" if score >= 40 else "Bajo"
    
    if aprobacion == "Bajo":
        motivo = "Riesgo bajo. Se recomienda mantener un estilo de vida saludable y evitar el tabaco"
    elif aprobacion == "Medio":
        motivo = "Riesgo medio. Se recomienda ir al medico para una evaluación más detallada y considerar dejar de fumar"    
    else:
        motivo = "Riesgo alto. Se recomienda encarecidamente ir al medico y dejar de fumar cuanto antes"    

    return {
        "solicitante": cancer_pulmon.nombre,
        "riesgo_cancer_pulmon": aprobacion,
        "score": score,
        "recomendacion": motivo
    }
