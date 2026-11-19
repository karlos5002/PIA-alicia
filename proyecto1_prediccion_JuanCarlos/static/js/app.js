document.getElementById('churn-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const btn = document.getElementById('btn-submit');
    const loading = document.getElementById('loading');
    const errorBox = document.getElementById('error-box');
    const resultCard = document.getElementById('result-card');

    errorBox.classList.add('hidden');
    resultCard.classList.add('hidden');
    loading.classList.remove('hidden');
    btn.disabled = true;

    const payload = {
        id_cliente: document.getElementById('id_cliente').value,
        edad: parseFloat(document.getElementById('edad').value),
        ingresos_anuales: parseFloat(document.getElementById('ingresos_anuales').value),
        saldo_cuenta: parseFloat(document.getElementById('saldo_cuenta').value),
        antiguedad_meses: parseInt(document.getElementById('antiguedad_meses').value),
        num_productos: parseInt(document.getElementById('num_productos').value),
        tiene_tarjeta: parseInt(document.getElementById('tiene_tarjeta').value),
        tipo_cuenta: document.getElementById('tipo_cuenta').value,
        canal_preferido: document.getElementById('canal_preferido').value,
        nivel_estudios: document.getElementById('nivel_estudios').value,
        nivel_satisfaccion: document.getElementById('nivel_satisfaccion').value
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || 'Error al procesar la petición');
        }

        const data = await response.json();

        document.getElementById('res-id').textContent = data.id_cliente;
        document.getElementById('res-veredicto').textContent = data.abandono === 1 ? 'Abandona (1)' : 'Permanece (0)';
        document.getElementById('res-prob').textContent = (data.probabilidad_abandono * 100).toFixed(1) + ' %';
        
        const badge = document.getElementById('res-riesgo');
        badge.textContent = data.nivel_riesgo;
        badge.className = 'badge riesgo-' + data.nivel_riesgo;

        document.getElementById('res-accion').textContent = data.accion_recomendada;

        resultCard.classList.remove('hidden');

    } catch (error) {
        errorBox.textContent = 'Error: ' + error.message;
        errorBox.classList.remove('hidden');
    } finally {
        loading.classList.add('hidden');
        btn.disabled = false;
    }
});