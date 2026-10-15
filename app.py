from transformers import pipeline

# Cargar un pipeline preentrenado de análisis de sentimiento
clasificador = pipeline("sentiment-analysis")

# Analizar un texto de prueba (el modelo por defecto está optimizado en inglés)
texto = "Python and FastAPI make building AI projects incredibly easy and fun."
resultado = clasificador(texto)

print(f"Texto analizado: '{texto}'")
print(f"Resultado: {resultado}")

from fastapi import FastAPI

# 1. Instanciamos la aplicación FastAPI
app = FastAPI(
title="API de Introducción a la IA",
description="Servicio web para consultar el estado del sistema y realizar pruebas de endpoints",
version="1.0.0"
)

# 2. Definimos nuestro primer endpoint (Ruta raíz)
@app.get("/")
def ruta_raiz():
    """
Endpoint principal de bienvenida.
Devuelve un mensaje en formato JSON.
"""
    return {
"mensaje": "¡Bienvenido a la API de Inteligencia Artificial!",
"version": "1.0.0",
"estado": "operativo"
}

# 3. Endpoint de comprobación de salud del servicio (Health Check)
@app.get("/health")
def estado_servicio():
    return {
"estado": "OK",
"memoria_disponible": "85%",
"modelos_cargados": 0
}