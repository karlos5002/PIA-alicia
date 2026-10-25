# 🩺 Práctica AS1 - Parte 2: API y Despliegue de Riesgo Pulmonar

## 1. Descripción de la Aplicación

En este proyecto he desarrollado una aplicación web para evaluar el riesgo que tiene una persona de padecer cáncer de pulmón basándose en sus hábitos con el tabaco. El proyecto tiene dos partes conectadas:

* **El Backend (La API):** Está hecho con Python y FastAPI. Su función es recibir los datos del formulario (edad, cigarrillos al día, años fumando, exposición al humo, etc.). Para asegurar que los datos no llegan con errores, utilizo Pydantic para validarlos estrictamente. Una vez que los datos son correctos, el código calcula una puntuación de riesgo partiendo de una base de 10 puntos y suma o resta segun los factores médicos. Finalmente, devuelve un JSON indicando si el riesgo es Bajo, Medio o Alto, acompañado de una recomendación.

* **El Frontend (La Web):** Es una interfaz desarrollada con HTML, CSS y un archivo JavaScript (app.js). Este script hace una petición asíncrona (fetch) a la API cuando el usuario pulsa el botón, recoge la respuesta del servidor y muestra el resultado en pantalla usando colores visuales (verde, amarillo o rojo).

## 2. URL Pública

La aplicación está completamente operativa  en el siguiente enlace:
 [**https://api-pulmon-juancarlos.onrender.com**]


## 3. Plataforma de Despliegue

Como vimos en clase que Hugging Face Spaces ya no ofrece un entorno gratuito para este tipo de despliegues, como alternativa  he desplegado el proyecto  utilizando **Render**.

## 4. Tutorial de Despliegue en Render paso a paso


**Paso 1: Preparar el codigo en GitHub**
Lo primero es tener todo el código actualizado y subido a un repositorio de GitHub. En mi caso, los archivos de la API no estaban sueltos en la carpeta principal, sino dentro de una subcarpeta llamada mi_proyecto_JuanCarlos_Cano.

**Paso 2: Limpiar el requirements.txt**
Este fue el principal fallo. Render tienen muy poca memoria RAM (solo 512 MB). Si dejas librerías pesadas de análisis de datos en el requirements.txt (como numpy o pandas), la memoria del servidor fallara durante el despliegue.
Para solucionarlo, limpié el archivo y dejé estrictamente lo que necesita el servidor web para funcionar:



**Paso 3: Crear y configurar el servicio en Render**

1. Entra en Render, inicia sesión con GitHub y, en el panel principal, dale a **New** y selecciona **Web Service**.

2. Te pedirá que vincules un repositorio.

3. Llegarás a la pantalla de configuracion es importante que si tu repositorio tiene mas carpetas debes seleccionar la que necesitas en especifico en root directory si no fallara

   * **Root Directory:** Aquí debes poner el nombre de la carpeta exacta donde está tu archivo app.py. 

   * **Build Command:** Escribe pip install -r requirements.txt.

   * **Start Command:** Escribe uvicorn app:app --host 0.0.0.0 --port 10000.