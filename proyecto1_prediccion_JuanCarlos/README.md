# Predicción de Abandono Bancario — FastAPI + ML

Aplicación web con arquitectura desacoplada (Backend FastAPI + Frontend HTML/CSS/JS) para predecir en tiempo real la probabilidad de abandono de un cliente bancario mediante un pipeline de preprocesamiento (ColumnTransformer) y un modelo KNeighborsClassifier.

##  Enlace al despliegue en producción
* **URL de la aplicación:** [https://tu-app.onrender.com](https://pia-alicia-1.onrender.com)
* **Documentación interactiva:** [https://tu-app.onrender.com/docs](https://pia-alicia-1.onrender.com/docs)

##  Instalación y ejecución en local

1. **Clonar o descomprimir el proyecto y entrar en la carpeta:**
   cd proyecto1_prediccion_JuanCarlos

2. **Crear y activar un entorno virtual:**
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate

3. **Instalar las dependencias:**
   pip install -r requirements.txt

4. **Arrancar el servidor FastAPI:**
   uvicorn main:app --reload

   Acceder desde el navegador a http://127.0.0.1:8000
