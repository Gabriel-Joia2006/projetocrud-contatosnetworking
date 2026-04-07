async function carregarEstadosECidades(estadoSelecionado = "", cidadeSelecionada = "") {
    const estadoSelect = document.getElementById("estado");
    const cidadeSelect = document.getElementById("cidade");

    const response = await fetch("/static/estados_cidades.json");
    const dados = await response.json();

    // Preenche estados
    estadoSelect.innerHTML = '<option value="">Selecione...</option>';
    Object.keys(dados).sort().forEach(uf => {
        const option = document.createElement("option");
        option.value = uf;
        option.textContent = uf;
        if (uf === estadoSelecionado) option.selected = true;
        estadoSelect.appendChild(option);
    });

    // Preenche cidades
    function atualizarCidades() {
        const uf = estadoSelect.value;
        cidadeSelect.innerHTML = '<option value="">Selecione...</option>';

        if (dados[uf]) {
            dados[uf].forEach(cidade => {
                const option = document.createElement("option");
                option.value = cidade;
                option.textContent = cidade;
                if (cidade === cidadeSelecionada) option.selected = true;
                cidadeSelect.appendChild(option);
            });
        }
    }

    estadoSelect.addEventListener("change", atualizarCidades);

    if (estadoSelecionado) atualizarCidades();
}