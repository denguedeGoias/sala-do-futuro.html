<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro - Feizão de Moraes</title>
    <style>
        /* Cores oficiais: Preto e Vermelho */
        :root {
            --preto: #000000;
            --vermelho: #E50914;
            --vermelho-escuro: #B00006;
            --cinza-escuro: #121212;
            --cinza-medio: #1E1E1E;
            --cinza-claro: #333333;
            --texto: #FFFFFF;
            --texto-suave: #CCCCCC;
            --sucesso: #22C55E;
            --alerta: #F59E0B;
            --erro: #EF4444;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
        }

        body {
            background: var(--preto);
            color: var(--texto);
            min-height: 100vh;
        }

        /* Tela de Login */
        .tela-login {
            max-width: 420px;
            margin: 80px auto;
            padding: 30px;
            background: var(--cinza-escuro);
            border-radius: 8px;
            border: 1px solid var(--cinza-claro);
            box-shadow: 0 0 15px rgba(229, 9, 20, 0.2);
        }

        .tela-login h1 {
            text-align: center;
            color: var(--vermelho);
            margin-bottom: 10px;
            font-size: 28px;
        }

        .tela-login p.subtitulo {
            text-align: center;
            color: var(--texto-suave);
            margin-bottom: 25px;
        }

        .campo {
            width: 100%;
            padding: 12px;
            margin: 8px 0 16px;
            background: var(--cinza-medio);
            border: 1px solid var(--cinza-claro);
            border-radius: 4px;
            color: var(--texto);
            font-size: 15px;
        }

        .campo:focus {
            outline: none;
            border-color: var(--vermelho);
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.2);
        }

        .btn {
            width: 100%;
            padding: 12px;
            background: var(--vermelho);
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
        }

        .btn:hover {
            background: var(--vermelho-escuro);
        }

        /* Layout Principal */
        .container-principal {
            display: flex;
            min-height: 100vh;
        }

        .menu-lateral {
            width: 260px;
            background: var(--cinza-escuro);
            border-right: 1px solid var(--cinza-claro);
            padding: 20px 0;
        }

        .perfil {
            padding: 0 20px 20px;
            border-bottom: 1px solid var(--cinza-claro);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .circulo-inicial {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: var(--vermelho);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
        }

        .status-sync {
            font-size: 13px;
            color: var(--sucesso);
            margin-top: 5px;
        }

        .menu-item {
            width: 100%;
            padding: 12px 20px;
            text-align: left;
            background: transparent;
            border: none;
            color: var(--texto);
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: background 0.2s;
        }

        .menu-item:hover {
            background: var(--cinza-medio);
        }

        .menu-item.ativo {
            background: var(--vermelho);
            color: white;
        }

        .conteudo {
            flex: 1;
            padding: 30px;
            background: var(--preto);
        }

        .card {
            background: var(--cinza-escuro);
            border: 1px solid var(--cinza-claro);
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 20px;
        }

        .card h3 {
            margin-bottom: 15px;
            color: var(--vermelho);
        }

        .item-atividade {
            background: var(--cinza-medio);
            border-left: 4px solid var(--vermelho);
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
        }

        .acoes {
            margin-top: 12px;
            text-align: right;
        }

        .btn-pequeno {
            padding: 6px 12px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 14px;
            margin-left: 8px;
        }

        .btn-vermelho { background: var(--vermelho); color: white; }
        .btn-verde { background: var(--sucesso); color: white; }
        .btn-cinza { background: var(--cinza-claro); color: white; }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="telaLogin" class="tela-login">
    <h1>Sala do Futuro</h1>
    <p class="subtitulo">Feizão de Moraes</p>

    <label>RA:</label>
    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">

    <label>Dígito:</label>
    <input type="text" id="digito" class="campo" maxlength="1" placeholder="0">

    <label>UF:</label>
    <select id="uf" class="campo">
        <option value="SP" selected>SP</option>
        <option value="MG">MG</option>
        <option value="RJ">RJ</option>
        <option value="GO">GO</option>
        <option value="RS">RS</option>
    </select>

    <label>Senha:</label>
    <input type="password" id="senha" class="campo" placeholder="Senha da Sala do Futuro">

    <button onclick="conectarServidor()" class="btn">Conectar e Entrar</button>

    <p style="text-align:center; margin-top:20px; font-size:12px; color:var(--texto-suave)">
        Desenvolvido por Dengue de Goiás
    </p>
</div>

<!-- PAINEL PRINCIPAL -->
<div id="painelPrincipal" class="container-principal" style="display: none;">
    <!-- MENU LATERAL -->
    <div class="menu-lateral">
        <div class="perfil">
            <div class="circulo-inicial" id="inicialUsuario">A</div>
            <div>
                <h4 id="nomeUsuario">Aluno</h4>
                <p style="font-size:13px; color:var(--texto-suave)" id="dadosUsuario">SP • RA 00000000-0</p>
                <div class="status-sync" id="statusSync">🔄 Conectando...</div>
            </div>
        </div>

        <button onclick="abrirAba('inicio')" class="menu-item ativo">🏠 Início</button>
        <button onclick="abrirAba('tarefas')" class="menu-item">📋 Tarefas</button>
        <button onclick="abrirAba('redacao')" class="menu-item">✍️ Redação Paulista</button>
        <button onclick="abrirAba('config')" class="menu-item">⚙️ Configurações</button>
        <hr style="margin:15px 0; border:none; border-top:1px solid var(--cinza-claro)">
        <button onclick="sair()" class="menu-item" style="color:var(--erro)">🚪 Sair</button>
    </div>

    <!-- ÁREA DE CONTEÚDO -->
    <div class="conteudo">
        <div id="abaInicio">
            <h2 style="margin-bottom:20px; color:var(--vermelho)">Visão Geral</h2>
            <div class="card">
                <p>Pendentes: <strong id="qtdPendentes">0</strong></p>
                <p>Concluídas: <strong id="qtdConcluidas">0</strong></p>
                <p>Total: <strong id="qtdTotal">0</strong></p>
            </div>
        </div>

        <div id="abaTarefas" style="display:none;">
            <h2 style="margin-bottom:20px; color:var(--vermelho)">📋 Tarefas</h2>
            <div class="card">
                <input type="text" id="tituloTarefa" class="campo" placeholder="Título da tarefa">
                <input type="number" id="tempoTarefa" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                <input type="date" id="prazoTarefa" class="campo">
                <textarea id="descTarefa" class="campo" rows="2" placeholder="Descrição da tarefa"></textarea>
                <button onclick="salvarTarefa()" class="btn">Salvar Tarefa</button>
            </div>
            <div id="listaTarefas"></div>
        </div>

        <div id="abaRedacao" style="display:none;">
            <h2 style="margin-bottom:20px; color:var(--vermelho)">✍️ Redação Paulista</h2>
            <div class="card">
                <input type="text" id="tituloRedacao" class="campo" placeholder="Tema da redação">
                <input type="number" id="tempoRedacao" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                <input type="date" id="prazoRedacao" class="campo">
                <textarea id="textoRedacao" class="campo" rows="5" placeholder="Escreva o texto da redação"></textarea>
                <button onclick="salvarRedacao()" class="btn">Salvar Redação</button>
            </div>
            <div id="listaRedacoes"></div>
        </div>

        <div id="abaConfig" style="display:none;">
            <h2 style="margin-bottom:20px; color:var(--vermelho)">⚙️ Configurações</h2>
            <div class="card">
                <h3>Conexão com o Servidor</h3>
                <p style="margin-bottom:15px; color:var(--texto-suave)">Servidor da Sala do Futuro: <code>denguedegoias.github.io/sala-do-futuro</code></p>
                <button onclick="forcarSincronizacao()" class="btn">Atualizar do Servidor</button>
            </div>
        </div>
    </div>
</div>

<script>
// =====================
// CONEXÃO E SINCRONIZAÇÃO COM SERVIDOR
// =====================
const SERVIDOR_URL = "https://denguedegoias.github.io/sala-do-futuro/dados/";
let usuario = null;
let syncInterval = null;

// Conecta e valida acesso ao servidor
async function conectarServidor() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) {
        alert("Preencha RA e senha corretamente!");
        return;
    }

    try {
        // Simula validação e conexão com o servidor
        document.querySelector(".btn").textContent = "Conectando...";

        // Cria/recupera dados do usuário
        usuario = {
            ra: ra,
            digito: digito,
            uf: uf,
            nome: "Aluno",
            atividades: { tarefas: [], redacoes: [] },
            ultimaAtualizacao: new Date().toISOString()
        };

        // Tenta buscar dados salvos no servidor/local
        const dadosServidor = await buscarDadosServidor(ra);
        if (dadosServidor) usuario = { ...usuario, ...dadosServidor };

        abrirSistema();
        iniciarSincronizacao();
        alert("✅ Conectado ao servidor da Sala do Futuro!");

    } catch (erro) {
        alert("❌ Erro ao conectar: " + erro.message);
        document.querySelector(".btn").textContent = "Conectar e Entrar";
    }
}

// Busca dados do servidor
async function buscarDadosServidor(ra) {
    try {
        const resposta = await fetch(`${SERVIDOR_URL}${ra}.json`, { cache: "no-cache" });
        if (!resposta.ok) throw new Error("Dados não encontrados no servidor");
        return await resposta.json();
    } catch {
        // Se não encontrar no servidor, usa dados locais salvos
        const local = localStorage.getItem(`sala_futuro_${ra}`);
        return local ? JSON.parse(local) : null;
    }
}

// Envia dados para o servidor
async function enviarParaServidor() {
    if (!usuario) return;
    usuario.ultimaAtualizacao = new Date().toISOString();

    // Salva localmente primeiro
    localStorage.setItem(`sala_futuro_${usuario.ra}`, JSON.stringify(usuario));

    // Tenta enviar para o servidor
    try {
        await fetch(`${SERVIDOR_URL}${usuario.ra}.json`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(usuario)
        });
        document.getElementById("statusSync").textContent = `✅ Sincronizado ${new Date().toLocaleTimeString()}`;
    } catch {
        document.getElementById("statusSync").textContent = `⚠️ Salvo localmente`;
    }
}

function iniciarSincronizacao() {
    if (syncInterval) clearInterval(syncInterval);
    syncInterval = setInterval(enviarParaServidor, 3000); // Sincroniza a cada 3 segundos
}

function forcarSincronizacao() {
    document.getElementById("statusSync").textContent = "🔄 Atualizando...";
    enviarParaServidor();
}

// =====================
// NAVEGAÇÃO
// =====================
function abrirSistema() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painelPrincipal").style.display = "flex";
    document.getElementById("inicialUsuario").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("dadosUsuario").textContent = `${usuario.uf} • RA ${usuario.ra}-${usuario.digito}`;
    atualizarTela();
}

function abrirAba(nome) {
    document.querySelectorAll(".conteudo > div").forEach(el => el.style.display = "none");
    document.querySelectorAll(".menu-item").forEach(el => el.classList.remove("ativo"));

    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).style.display = "block";
    event.currentTarget.classList.add("ativo");
}

// =====================
// GERENCIAMENTO DE TAREFAS E REDAÇÃO
// =====================
function salvarTarefa() {
    const tarefa = {
        id: Date.now(),
        titulo: document.getElementById("tituloTarefa").value.trim(),
        tempo: parseInt(document.getElementById("tempoTarefa").value),
        prazo: document.getElementById("prazoTarefa").value || "",
        descricao: document.getElementById("descTarefa").value,
        status: "pendente"
    };

    if (!tarefa.titulo) return alert("Digite o título da tarefa!");
    usuario.atividades.tarefas.push(tarefa);
    limparCampos("tarefa");
    enviarParaServidor();
}

function salvarRedacao() {
    const redacao = {
        id: Date.now(),
        tema: document.getElementById("tituloRedacao").value.trim(),
        tempo: parseInt(document.getElementById("tempoRedacao").value),
        prazo: document.getElementById("prazoRedacao").value || "",
        texto: document.getElementById("textoRedacao").value,
        status: "pendente"
    };

    if (!redacao.tema) return alert("Digite o tema da redação!");
    usuario.atividades.redacoes.push(redacao);
    limparCampos("redacao");
    enviarParaServidor();
}

function limparCampos(tipo) {
    if (tipo === "tarefa") {
        ["tituloTarefa", "tempoTarefa", "prazoTarefa", "descTarefa"].forEach(id => document.getElementById(id).value = id === "tempoTarefa" ? "1" : "");
    } else {
        ["tituloRedacao", "tempoRedacao", "prazoRedacao", "textoRedacao"].forEach(id => document.getElementById(id).value = id === "tempoRedacao" ? "1" : "");
    }
}

function alterarStatus(tipo, id, novoStatus) {
    const lista = usuario.atividades[tipo];
    const item = lista.find(i => i.id === id);
    if (item) {
        item.status = novoStatus;
        enviarParaServidor();
    }
}

// =====================
// ATUALIZAÇÃO DA TELA
// =====================
function atualizarTela() {
    const todas = [...usuario.atividades.tarefas, ...usuario.atividades.redacoes];
    document.getElementById("qtdPendentes").textContent = todas.filter(i => i.status !== "concluida").length;
    document.getElementById("qtdConcluidas").textContent = todas.filter(i => i.status === "concluida").length;
    document.getElementById("qtdTotal").textContent = todas.length;

    renderizarLista("tarefas");
    renderizarLista("redacoes");
}

function renderizarLista(tipo) {
    const container = document.getElementById(`lista${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`);
    const itens = usuario.atividades[tipo];

    if (itens.length === 0) {
        container.innerHTML = `<p style="color:var(--texto-suave); text-align:center; padding:20px;">Nenhuma ${tipo === "tarefas" ? "tarefa cadastrada" : "redação salva"}</p>`;
        return;
    }

    container.innerHTML = itens.map(item => `
        <div class="item-atividade">
            <h4>${item.titulo || item.tema}</h4>
            ${item.prazo ? `<p style="font-size:13px; color:var(--texto-suave); margin:5px 0;">Prazo: ${new Date(item.prazo).toLocaleDateString("pt-BR")}</p>` : ""}
            <p style="margin:8px 0; color:var(--texto-suave);">${item.descricao || item.texto || ""}</p>
            <div class="acoes">
                ${item.status === "pendente" ? `<button onclick="alterarStatus('${tipo}', ${item.id}, 'em_andamento')" class="btn-pequeno btn-vermelho">Começar</button>` : ""}
                ${item.status === "em_andamento" ? `<button onclick="alterarStatus('${tipo}', ${item.id}, 'concluida')" class="btn-pequeno btn-verde">Concluir</button>` : ""}
                ${item.status === "concluida" ? `<span style="color:var(--sucesso)">✅ Concluído</span>` : ""}
            </div>
        </div>
    `).join("");
}

// =====================
// SAIR E INICIALIZAÇÃO
// =====================
function sair() {
    if (confirm("Deseja sair da Sala do Futuro?")) {
        clearInterval(syncInterval);
        usuario = null;
        location.reload();
    }
}

// Recupera sessão salva ao abrir
window.onload = () => {
    const sessao = localStorage.getItem("sala_futuro_sessao");
    if (sessao) {
        const dados = JSON.parse(sessao);
        usuario = dados;
        abrirSistema();
        iniciarSincronizacao();
    }
};
</script>

</body>
</html>
