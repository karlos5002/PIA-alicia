const formulario = document.getElementById("formulario-pulmon");
const panelResultado = document.getElementById("panel-resultado");
const resultadoCaja = document.getElementById("resultado-caja");
const btnEnviar = document.getElementById("btn-enviar");

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const datosSolicitud = {
    nombre: document.getElementById("nombre").value,
    edad_actual: parseInt(document.getElementById("edad").value),
    cigarrillos_por_dia: parseInt(document.getElementById("cigarrillos").value),
    anos_fumando: parseInt(document.getElementById("anos_fumando").value),
    anos_sin_fumar: parseInt(document.getElementById("anos_sin_fumar").value),
    exposicion_humo_segunda_mano: document.getElementById("segunda_mano").checked
  };

  btnEnviar.disabled = true;
  btnEnviar.textContent = "Analizando datos...";

  try {
    const respuesta = await fetch("/api/calcular_riesgo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(datosSolicitud)
    });

    if (!respuesta.ok) {
      throw new Error("Error en el servidor. Código: " + respuesta.status);
    }

    const resultado = await respuesta.json();

    panelResultado.classList.remove("hidden");
    
    let colorClase = "";
    let estadoTexto = "";
    
    if (resultado.riesgo_cancer_pulmon === "Bajo") {
      colorClase = "border-emerald-200 bg-emerald-50 text-emerald-900";
      estadoTexto = "Nivel de Riesgo: Bajo";
    } else if (resultado.riesgo_cancer_pulmon === "Medio") {
      colorClase = "border-amber-200 bg-amber-50 text-amber-900";
      estadoTexto = "Nivel de Riesgo: Medio";
    } else {
      colorClase = "border-rose-200 bg-rose-50 text-rose-900";
      estadoTexto = "Nivel de Riesgo: Alto";
    }

    resultadoCaja.className = `p-6 rounded-xl border ${colorClase}`;
    resultadoCaja.innerHTML = `
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-xl font-bold">${estadoTexto}</h3>
        <span class="px-3 py-1 bg-white border border-current rounded-full font-bold text-sm shadow-sm">
          Score: ${resultado.score} / 100
        </span>
      </div>
      <p class="text-sm mb-3"><strong>Paciente Evaluado:</strong> ${resultado.solicitante}</p>
      <p class="text-sm font-medium mt-4 p-3 bg-white/60 rounded-lg"><strong>Recomendación:</strong> ${resultado.recomendacion}</p>
    `;

  } catch (error) {
    alert("Error de conexión con la API.");
    console.error(error);
  } finally {
    btnEnviar.disabled = false;
    btnEnviar.textContent = "Evaluar Riesgo";
  }
});