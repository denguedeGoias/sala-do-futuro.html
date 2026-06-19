<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feizão de Moraes</title>
    <style>
        :root {
            --cor-principal: #E50914;
            --cor-fundo: #ffffff;
            --cor-cinza: #f0f0f0;
            --cor-borda: #ddd;
            --cor-texto: #333;
            --cor-sucesso: #28a745;
            --cor-alerta: #ffc107;
            --cor-erro: #dc3545;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            background: var(--cor-cinza);
            color: var(--cor-texto);
            font-size: 15px;
        }

        .container {
            max-width: 900px;
            margin: 20px auto;
            background: var(--cor-fundo);
            border: 1px solid var(--cor-borda);
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .cabecalho {
            padding: 15px;
            border-bottom: 1px solid var(--cor-borda);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .perfil {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .circulo {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--cor-principal);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 18px;
        }

        .status-sync {
            font-size: 13px;
            color: var(--cor-sucesso);
        }

        .conteudo-principal {
            display: flex;
            min-height: 500px;
        }

        .menu {
            width: 220px;
            background: var(--cor-cinza);
            border-right: 1px solid var(--cor-borda);
            padding: 10px 0;
        }

        .menu button {
            display: block;
            width: 100%;
            padding: 10px 15px;
            text-align: left;
            border: none;
            background: transparent;
            font-size: 15px;
            color: var(--cor-texto);
            cursor: pointer;
        }

        .menu button:hover {
            background: #e9e9e9;
        }

        .menu .ativo {
            background: var(--cor-principal);
            color: white;
        }

        .area-conteudo {
            flex: 1;
            padding: 20px;
        }

        .form-bloco {
            background: var(--cor-cinza);
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            border: 1px solid var(--cor-borda);
        }

        input, textarea, select {
            width: 100%;
            padding: 8px;
            margin: 6px 0 12px;
            border: 1px solid var(--cor-borda);
            border-radius: 3px;
            font-size: 14px;
        }

        button {
            padding: 8px 16px;
            background: var(--cor-principal);
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 14px;
        }

        button:hover {
            background: #c00812;
        }

        .item {
            padding: 12px;
            margin: 8px 0;
            border: 1px solid var(--cor-borda);
            border-left: 4px solid var(--cor-principal);
            border-radius: 3px;
            background: white;
        }

        .item .acoes {
            margin-top: 8px;
            text-align: right;
        }

        .tela-login {
            max-width: 400px;
            margin: 80px auto;
            background: white;
            padding: 25px;
            border: 1px solid var(--cor-borda);
            border-radius: 4px;
        }

        .tela-login h1 {
            text-align: center;
            color: var(--cor-principal);
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div id="telaLogin" class="tela-login">
    <h1>Feizão de Moraes</h1>
    <p style="text-align:center; margin-bottom:20px;">Sistema Sala do Futuro</p>

    <label>RA:</label>
    <input type="text" id="ra" placeholder="Digite seu RA">

    <label>Dígito:</label>
    <input type="text" id="digito" maxlength="1" placeholder="0">

    <label>UF:</label>
    <select id="uf">
        <option value="SP" selected>SP</option>
        <option value="MG">MG</option>
        <option value="RJ">RJ</option>
        <option value="GO">GO</option>
    </select>

    <label>Senha:</label>
    <input type="password" id="senha" placeholder="Senha de acesso">

    <button onclick="entrar()" style="width:100%; margin-top:10px;">Acessar</button>
    <p style="text-align:center; font-size:12px; margin-top:15px; color:#777;">Desenvolvido por Dengue de Goiás</p>
</div>

<div id="sistema" class="container" style="display:none;">
    <div class="cabecalho">
        <div class="perfil">
            <div class="circulo" id="inicial">A</div>
            <div>
                <h3 id="nomeUsuario">Aluno</h3>
                <span style="font-size:13px;">SP • RA 00000000-0</span>
            </div>
        </div>
        <div class="status-sync" id="statusSync">✅ Sincronizado</div>
    </div>

    <div class="conteudo-principal">
        <div class="menu">
            <button onclick="abrirAba('inicio')" id="menuInicio" class="ativo">🏠 Início</button>
            <button onclick="abrirAba('tarefas')" id="menuTarefas">📋 Tarefas</button>
            <button onclick="abrirAba('redacao')" id="menuRedacao">✍️ Redação Paulista</button>
            <button onclick="abrirAba('cores')" id="menuCores">🎨 Personalizar Cores</button>
            <button onclick="atualizarDados()">🔄 Atualizar Dados</button>
            <hr style="margin:10px 0; border:none; border-top:1px solid #ddd;">
            <button onclick="sair()" style="color:var(--cor-erro)">🚪 Sair</button>
        </div>

        <div class="area-conteudo">
            <div id="abaInicio">
                <h2>Resumo Geral</h2>
                <div style="margin:15px 0; padding:10px; background:var(--cor-cinza); border-radius:3px;">
                    <p>Pendentes: <strong id="pendentes">0</strong></p>
                    <p>Concluídas: <strong id="concluidas">0</strong></p>
                </div>
            </div>

            <div id="abaTarefas" style="display:none;">
                <h2>Tarefas</h2>
                <div class="form-bloco">
                    <label>Título:</label>
                    <input type="text" id="tituloTarefa" placeholder="Ex: Estudar Matemática">

                    <label>Tempo (min):</label>
                    <input type="number" id="tempoTarefa" min="1" value="1">

                    <label>Prazo:</label>
                    <input type="date" id="prazoTarefa">

                    <label>Descrição:</label>
                    <textarea id="descTarefa" rows="2" placeholder="Detalhes da tarefa"></textarea>

                    <button onclick="adicionarTarefa()">Adicionar Tarefa</button>
                </div>
                <div id="listaTarefas"></div>
            </div>

            <div id="abaRedacao" style="display:none;">
                <h2>Redação Paulista</h2>
                <div class="form-bloco">
                    <label>Tema:</label>
                    <input type="text" id="tituloRedacao" placeholder="Ex: Desafios da Educação">

                    <label>Tempo (min):</label>
                    <input type="number" id="tempoRedacao" min="1" value="1">

                    <label>Prazo:</label>
                    <input type="date" id="prazoRedacao">

                    <label>Texto / Anotações:</label>
                    <textarea id="textoRedacao" rows="4" placeholder="Escreva aqui..."></textarea>

                    <button onclick="adicionarRedacao()">Salvar Redação</button>
                </div>
                <div id="listaRedacoes"></div>
            </div>

            <div id="abaCores" style="display:none;">
                <h2>Personalizar Cores</h2>
                <div class="form-bloco">
                    <label>Cor Principal:</label>
                    <input type="color" id="corPrincipal" value="#E50914">

                    <label>Cor de Fundo:</label>
                    <input type="color" id="corFundo" value="#ffffff">

                    <button onclick="aplicarCores()" style="margin-right:10px;">Aplicar</button>
                    <button onclick="restaurarCores()">Restaurar Padrão</button>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
let usuario = null;
let intervaloSync = null;

function sincronizar() {
    if (!usuario) return;
    localStorage.setItem(`feizao_${usuario.ra}`, JSON.stringify(usuario));
    localStorage.setItem("sessaoAtiva", JSON.stringify({ ra: usuario.ra, hora: new Date().toLocaleTimeString() }));
    document.getElementById("statusSync").textContent = `✅ Sincronizado ${new Date().toLocaleTimeString()}`;
    atualizarTela();
}

function iniciarSync() {
    if (intervaloSync) clearInterval(intervaloSync);
    intervaloSync = setInterval(sincronizar, 2000);
}

function atualizarDados() {
    document.getElementById("statusSync").textContent = "🔄 Atualizando...";
    setTimeout(sincronizar, 500);
}

function entrar() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) return alert("Preencha todos os campos!");

    usuario = {
        ra: ra,
        digito: digito,
        uf: uf,
        nome: "Aluno",
        atividades: { tarefas: [], redacoes: [] },
        cores: { principal: "#E50914", fundo: "#ffffff" }
    };

    const salvo = localStorage.getItem(`feizao_${ra}`);
    if (salvo) usuario = Object.assign(usuario, JSON.parse(salvo));

    abrirSistema();
    iniciarSync();
    aplicarCoresSalvas();
    sincronizar();
}

function abrirSistema() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("sistema").style.display = "block";
    document.getElementById("inicial").textContent = usuario.nome.charAt(0).toUpperCase();
    document.querySelector(".perfil span").textContent = `${usuario.uf} • RA ${usuario.ra}-${usuario.digito}`;
}

function abrirAba(nome) {
    document.querySelectorAll(".area-conteudo > div").forEach(el => el.style.display = "none");
    document.querySelectorAll(".menu button").forEach(el => el.classList.remove("ativo"));

    document.getElementById("aba" + nome.charAt(0).toUpperCase() + nome.slice(1)).style.display = "block";
    document.getElementById("menu" + nome.charAt(0).toUpperCase() + nome.slice(1)).classList.add("ativo");
}

function adicionarTarefa() {
    const titulo = document.getElementById("tituloTarefa").value.trim();
    if (!titulo) return alert("Digite um título!");

    const nova = {
        id: Date.now(),
        titulo: titulo,
        tempo: parseInt(document.getElementById("tempoTarefa").value),
        prazo: document.getElementById("prazoTarefa").value || "",
        descricao: document.getElementById("descTarefa").value,
        status: "pendente"
    };

    usuario.atividades.tarefas.push(nova);
    limparCampos("tarefa");
    sincronizar();
}

function adicionarRedacao() {
    const titulo = document.getElementById("tituloRedacao").value.trim();
    if (!titulo) return alert("Digite um tema!");

    const nova = {
        id: Date.now(),
        titulo: titulo,
        tempo: parseInt(document.getElementById("tempoRedacao").value),
        prazo: document.getElementById("prazoRedacao").value || "",
        texto: document.getElementById("textoRedacao").value,
        status: "pendente"
    };

    usuario.atividades.redacoes.push(nova);
    limparCampos("redacao");
    sincronizar();
}

function limparCampos(tipo) {
    if (tipo === "tarefa") {
        document.getElementById("tituloTarefa").value = "";
        document.getElementById("tempoTarefa").value = "1";
        document.getElementById("prazoTarefa").value = "";
        document.getElementById("descTarefa").value = "";
    } else {
        document.getElementById("tituloRedacao").value = "";
        document.getElementById("tempoRedacao").value = "1";
        document.getElementById("prazoRedacao").value = "";
        document.getElementById("textoRedacao").value = "";
    }
}

function atualizarTela() {
    const todas = [...usuario.atividades.tarefas, ...usuario.atividades.redacoes];
    document.getElementById("pendentes").textContent = todas.filter(i => i.status !== "concluida").length;
    document.getElementById("concluidas").textContent = todas.filter(i => i.status === "concluida").length;

    renderLista("tarefas");
    renderLista("redacoes");
}

function renderLista(tipo) {
    const container = document.getElementById("lista" + tipo.charAt(0).toUpperCase() + tipo.slice(1));
    const itens = usuario.atividades[tipo];

    if (itens.length === 0) {
        container.innerHTML = "<p style='color:#777; text-align:center; padding:20px;'>Nenhuma atividade cadastrada</p>";
        return;
    }

    container.innerHTML = itens.map(item => `
        <div class="item">
            <h4>${item.titulo}</h4>
            ${item.prazo ? `<p><small>Prazo: ${new Date(item.prazo).toLocaleDateString("pt-BR")}</small></p>` : ""}
            ${item.descricao ? `<p>${item.descricao}</p>` : ""}
            ${item.texto ? `<p>${item.texto}</p>` : ""}
            <div class="acoes">
                ${item.status === "pendente" ? `<button onclick="mudarStatus(${item.id}, 'andamento')">Começar</button>` : ""}
                ${item.status === "andamento" ? `<button onclick="mudarStatus(${item.id}, 'concluida')">Concluir</button>` : ""}
                ${item.status === "concluida" ? `<span style="color:var(--cor-sucesso);">✅ Concluído</span>` : ""}
            </div>
        </div>
    `).join("");
}

function mudarStatus(id, novoStatus) {
    const todas = [...usuario.atividades.tarefas, ...usuario.atividades.redacoes];
    const item = todas.find(i => i.id === id);
    if (item) {
        item.status = novoStatus;
        sincronizar();
    }
}

function aplicarCores() {
    const corP = document.getElementById("corPrincipal").value;
    const corF = document.getElementById("corFundo").value;

    document.documentElement.style.setProperty("--cor-principal", corP);
    document.documentElement.style.setProperty("--cor-fundo", corF);

    usuario.cores = { principal: corP, fundo: corF };
    sincronizar();
}

function restaurarCores() {
    document.getElementById("corPrincipal").value = "#E50914";
    document.getElementById("corFundo").value = "#ffffff";
    aplicarCores();
}

function aplicarCoresSalvas() {
    if (!usuario.cores) return;
    document.getElementById("corPrincipal").value = usuario.cores.principal;
    document.getElementById("corFundo").value = usuario.cores.fundo;
    aplicarCores();
}

function sair() {
    if (confirm("Sair do sistema?")) {
        clearInterval(intervaloSync);
        usuario = null;
        localStorage.removeItem("sessaoAtiva");
        location.reload();
    }
}

window.onload = () => {
    const sessao = localStorage.getItem("sessaoAtiva");
    if (sessao) {
        const { ra } = JSON.parse(sessao);
        const dados = localStorage.getItem(`feizao_${ra}`);
        if (dados) {
            usuario = JSON.parse(dados);
            abrirSistema();
            iniciarSync();
            aplicarCoresSalvas();
            sincronizar();
        }
    }
};
</script>

</body>
</html>
