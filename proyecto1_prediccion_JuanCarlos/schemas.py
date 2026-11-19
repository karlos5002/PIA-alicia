from typing import Optional, Literal
from pydantic import BaseModel, Field

class ClienteInput(BaseModel):
    id_cliente: str = Field(default="CLI-0000", description="Código identificador del cliente")
    edad: Optional[float] = Field(default=None, ge=18, le=120, description="Edad entre 18 y 120 años")
    ingresos_anuales: Optional[float] = Field(default=None, ge=0, description="Ingresos anuales en euros")
    saldo_cuenta: Optional[float] = Field(default=None, description="Saldo actual de la cuenta")
    num_productos: int = Field(default=1, ge=1, le=4, description="Productos contratados (1 a 4)")
    tiene_tarjeta: int = Field(default=0, ge=0, le=1, description="1 si posee tarjeta, 0 si no")
    antiguedad_meses: Optional[int] = Field(default=None, ge=0, description="Meses de antigüedad")
    tipo_cuenta: Optional[str] = Field(default=None, description="Corriente, Ahorro o Nomina")
    canal_preferido: Optional[str] = Field(default=None, description="App Movil, Web u Oficina")
    nivel_estudios: Optional[str] = Field(default=None, description="Primaria, Secundaria, Grado, Master o Doctorado")
    nivel_satisfaccion: Optional[str] = Field(default=None, description="Muy Bajo, Bajo, Medio, Alto o Muy Alto")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id_cliente": "CLI-8492",
                "edad": 45.0,
                "ingresos_anuales": 32000.0,
                "saldo_cuenta": 1500.0,
                "num_productos": 1,
                "tiene_tarjeta": 1,
                "antiguedad_meses": 14,
                "tipo_cuenta": "Corriente",
                "canal_preferido": "Oficina",
                "nivel_estudios": "Secundaria",
                "nivel_satisfaccion": "Muy Bajo"
            }
        }
    }

class PrediccionOutput(BaseModel):
    id_cliente: str
    abandono: int
    probabilidad_abandono: float
    nivel_riesgo: Literal["Bajo", "Medio", "Alto"]
    accion_recomendada: str