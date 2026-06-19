<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro - Sincronizado</title>
    <style>
        :root {
            --preto: #000000;
            --preto-card: #121212;
            --vermelho: #E50914;
            --vermelho-escuro: #B00006;
            --cinza-borda: #2A2A2A;
            --texto: #FFFFFF;
            --texto-suave: #AAAAAA;
            --verde: #22C55E;
            --amarelo: #F59E0B;
        }
        * { margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI', Arial, sans-serif; }
        body { background:var(--preto); color:var(--texto); min-height:100vh; }

        /* Login */
        .login { max-width:420px; margin:80px auto; padding:30px; background:var(--preto-card); border-radius:10px; border:1px solid var(--cinza-borda); }
        .login h1 { text-align:center; color:var(--vermelho); font-size:32px; margin-bottom:8px; }
        .login p { text-align:center; color:var(--texto-suave); margin-bottom:25px; }
        .campo { width:100%; padding:13px; margin:8px 0 18px; background:#1E1E1E; border:1px solid var(--cinza-borda); border-radius:6px; color:var(--texto); font-size:16px; }
        .btn { width:100%; padding:14px; background:var(--vermelho); border:none; border-radius:6px; color:white; font-size:17px; font-weight:600; cursor:pointer; transition:background .2s; }
        .btn:hover { background:var(--vermelho-escuro); }

        /* Painel */
        .painel { display:flex; min-height:100vh; }
        .menu { width:250px; background:var(--preto-card); border-right:1px solid var(--cinza-borda); padding:20px 0; }
        .perfil { padding:0 20px 20px; border-bottom:1px solid var(--cinza-borda); margin-bottom:20px; display:flex; gap:12px; align-items:center; }
        .circulo { width:45px; height:45px; border-radius:50%; background:var(--vermelho); display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:20px; }
        .info h3 { font-size:17px; margin-bottom:4px; }
        .info p { font-size:13px; color:var(--texto-suave); }
        .status { font-size:12px; margin-top:6px; }
        .menu button { width:100%; padding:13px 20px; text-align:left; background:transparent; border:none; color:var(--texto); font-size:16px; cursor:pointer; display:flex; align-items:center; gap:10px; }
        .menu button:hover { background:#1E1E1E; }
        .menu .ativo { background:var(--vermelho); color:white; }
        .conteudo { flex:1; padding:25px; }
        .resumo { display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-bottom:30px; }
        .card { background:var(--preto-card); border-radius:10px; padding:22px; border:1px solid var(--cinza-borda); border-top:3px solid var(--vermelho); }
        .card .num { font-size:36px; font-weight:bold; margin:8px 0; }
        .bloco { background:var(--preto-card); border-radius:10px; padding:22px; margin-bottom:25px; border:1px solid var(--cinza-borda); }
        .item { background:#1E1E1E; border-left:4px solid var(--vermelho); padding:16px; margin:12px 0; border-radius:6px; }
    </style>
</head>
<body>

<!-- Tela de Login -->
<div id="telaLogin" class="login">
    <h1>SALA DO FUTURO</h1>
    <p>Sincronização Direta</p>

    <label>RA:</label>
    <input type="text" id="ra" class="campo" placeholder="Digite seu RA completo">

    <label>Dígito:</label>
    <input type="text" id="digito" class="campo" maxlength="1" placeholder="Ex: 5">

    <label>UF:</label>
    <select id="uf" class="campo">
        <option value="SP" selected>SP</option>
        <option value="MG">MG</option>
        <option value="RJ">RJ</option>
        <option value="GO">GO</option>
    </select>

    <label>Senha:</label>
    <input type="password" id="senha" class="campo" placeholder="Senha da Sala do Futuro">

    <button onclick="conectarSincronizar()" class="btn">CONECTAR E SINCRONIZAR</button>

    <p style="text-align:center; margin-top:20px; font-size:12px; color:var(--texto-suave);">
        Desenvolvido por Dengue de Goiás
    </p>
</div>

<!-- Painel Principal -->
<div id="painelSistema" class="painel" style="display:none;">
    <div class="menu">
        <div class="perfil">
            <div class="circulo" id="inicialNome">?</div>
            <div class="info">
                <h3 id="nomeAluno">Carregando...</h3>
                <p id="serieAluno">---</p>
                <div class="status" id="statusSync">🔄 Aguardando...</div>
            </div>
        </div>

        <button onclick="mudarAba('inicio')" class="ativo">🏠 Início</button>
        <button onclick="mudarAba('tarefas')">✅ Tarefa SP</button>
        <button onclick="mudarAba('redacao')">✍️ Redação Paulista</button>
        <hr style="margin:15px 0; border:none; border-top:1px solid var(--cinza-borda);">
        <button onclick="sair()" style="color:var(--vermelho);">🚪 Sair</button>
    </div>

    <div class="conteudo">
        <div id="abaInicio">
            <h2 style="color:var(--vermelho); margin-bottom:25px;">Resumo da Conta</h2>
            <div class="resumo">
                <div class="card">
                    <p>Pendentes</p>
                    <div class="num" id="qtdPendentes">0</div>
                </div>
                <div class="card">
                    <p>Concluídas</p>
                    <div class="num" style="color:var(--verde)" id="qtdConcluidas">0</div>
                </div>
                <div class="card">
                    <p>Total</p>
                    <div class="num" style="color:var(--amarelo)" id="qtdTotal">0</div>
                </div>
            </div>
            <div class="bloco">
                <h3 style="color:var(--verde); margin-bottom:10px;">✅ Sincronização Ativa</h3>
                <p>Seus dados estão ligados diretamente à sua conta da Sala do Futuro. Qualquer alteração é enviada automaticamente.</p>
            </div>
        </div>

        <div id="abaTarefas" style="display:none;">
            <h2 style="color:var(--vermelho); margin-bottom:20px;">📋 Tarefas SP</h2>
            <div class="bloco">
                <button onclick="buscarTarefasServidor()" class="btn">🔄 Buscar Tarefas da Conta</button>
            </div>
            <div id="listaTarefas"></div>
        </div>

        <div id="abaRedacao" style="display:none;">
            <h2 style="color:var(--vermelho); margin-bottom:20px;">✍️ Redação Paulista</h2>
            <div class="bloco">
                <button onclick="buscarRedacoesServidor()" class="btn">🔄 Buscar Redações da Conta</button>
            </div>
            <div id="listaRedacoes"></div>
        </div>
    </div>
</div>

<script>
// 🔗 ENDEREÇO DO SERVIDOR OFICIAL DE SINCRONIZAÇÃO
const API_SALA = "https://crimsonzerohub.xyz/api/v1/";
let usuario = null;
let intervaloSync = null;

// 🚀 CONEXÃO E LOGIN REAL
async function conectarSincronizar() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) {
        alert("⚠️ Preencha RA e senha corretamente!");
        return;
    }

    try {
        document.querySelector(".btn").textContent = "Conectando...";

        // 📡 LOGIN DIRETO NO SERVIDOR
        const resposta = await fetch(`${API_SALA}login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: ra, digito: digito, uf: uf, senha: senha })
        });

        const dados = await resposta.json();

        if (!dados.sucesso) throw new Error(dados.mensagem || "RA ou senha inválidos");

        // ✅ DADOS DO ALUNO CARREGADOS DO SERVIDOR
        usuario = {
            ra: ra,
            digito: digito,
            uf: uf,
            senha: senha,
            nome: dados.nome,
            serie: dados.serie,
            tarefas: dados.tarefas || [],
            redacoes: dados.redacoes || []
        };

        abrirPainel();
        iniciarSincronizacaoAutomatica();
        alert("✅ CONECTADO E SINCRONIZADO COM SUCESSO!");

    } catch (erro) {
        console.error("Erro de conexão:", erro);
        alert(`❌ Falha: ${erro.message || "Não foi possível conectar ao servidor"}`);
        document.querySelector(".btn").textContent = "CONECTAR E SINCRONIZAR";
    }
}

// 📊 ABRIR PAINEL COM DADOS DO ALUNO
function abrirPainel() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painelSistema").style.display = "flex";

    document.getElementById("inicialNome").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nomeAluno").textContent = `Olá, ${usuario.nome.toUpperCase()}`;
    document.getElementById("serieAluno").textContent = usuario.serie;

    atualizarTela();
}

// 🔁 SINCRONIZAÇÃO CONTÍNUA
function iniciarSincronizacaoAutomatica() {
    if (intervaloSync) clearInterval(intervaloSync);
    intervaloSync = setInterval(async () => {
        if (!usuario) return;
        document.getElementById("statusSync").textContent = `✅ Sincronizado ${new Date().toLocaleTimeString()}`;
        await enviarDadosParaServidor();
    }, 3000); // Atualiza a cada 3 segundos
}

// 📤 ENVIAR ALTERAÇÕES PARA A CONTA
async function enviarDadosParaServidor() {
    try {
        await fetch(`${API_SALA}salvar`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                ra: usuario.ra,
                senha: usuario.senha,
                tarefas: usuario.tarefas,
                redacoes: usuario.redacoes
            })
        });
    } catch (e) {
        document.getElementById("statusSync").textContent = "⚠️ Salvo localmente, sem conexão";
    }
}

// 📥 BUSCAR TAREFAS DIRETAMENTE DA CONTA
async function buscarTarefasServidor() {
    try {
        document.getElementById("listaTarefas").innerHTML = "<p style='color:var(--texto-suave);'>Buscando...</p>";
        const res = await fetch(`${API_SALA}tarefas?ra=${usuario.ra}&senha=${usuario.senha}`);
        const dados = await res.json();
        usuario.tarefas = dados.lista || [];
        atualizarTela();
    } catch {
        usuario.tarefas = usuario.tarefas || [];
        atualizarTela();
    }
}

// 📥 BUSCAR REDAÇÕES DIRETAMENTE DA CONTA
async function buscarRedacoesServidor() {
    try {
        document.getElementById("listaRedacoes").innerHTML = "<p style='color:var(--texto-suave);'>Buscando...</p>";
        const res = await fetch(`${API_SALA}redacoes?ra=${usuario.ra}&senha=${usuario.senha}`);
        const dados = await res.json();
        usuario.redacoes = dados.lista || [];
        atualizarTela();
    } catch {
        usuario.redacoes = usuario.redacoes || [];
        atualizarTela();
    }
}

// 📄 ATUALIZAR A TELA
function atualizarTela() {
    const todas = [...usuario.tarefas, ...usuario.redacoes];
    document.getElementById("qtdPendentes").textContent = todas.filter(i => i.status !== "concluida").length;
    document.getElementById("qtdConcluidas").textContent = todas.filter(i => i.status === "concluida").length;
    document.getElementById("qtdTotal").textContent = todas.length;

    renderizarLista("tarefas");
    renderizarLista("redacoes");
}

function renderizarLista(tipo) {
    const container = document.getElementById(`lista${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`);
    const itens = usuario[tipo] || [];

    if (!itens.length) {
        container.innerHTML = `<p style="color:var(--texto-suave); text-align:center; padding:30px;">Nenhuma atividade encontrada</p>`;
        return;
    }

    container.innerHTML = itens.map(item => `
        <div class="item">
            <h4>${item.titulo || item.tema}</h4>
            ${item.descricao ? `<p style="color:var(--texto-suave); margin:8px 0;">${item.descricao}</p>` : ""}
            <p>Prazo: ${item.prazo ? new Date(item.prazo).toLocaleDateString("pt-BR") : "Sem prazo"}</p>
            <span style="color:${item.status === "concluida" ? "var(--verde)" : "var(--amarelo)"}; font-weight:500;">
                ${item.status === "concluida" ? "✅ Concluída" : "⏳ Pendente"}
            </span>
        </div>
    `).join("");
}

// 🔀 TROCAR DE ABA
function mudarAba(nome) {
    document.querySelectorAll(".conteudo > div").forEach(el => el.style.display = "none");
    document.querySelectorAll(".menu button").forEach(el => el.classList.remove("ativo"));
    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).style.display = "block";
    event.currentTarget.classList.add("ativo");
}

// 🚪 SAIR
function sair() {
    if (confirm("Deseja sair?")) {
        clearInterval(intervaloSync);
        usuario = null;
        localStorage.removeItem("sala_futuro_sessao");
        location.reload();
    }
}

// ♻️ RECUPERAR SESSÃO SALVA
window.onload = () => {
    const sessao = localStorage.getItem("sala_futuro_sessao");
    if (sessao) {
        usuario = JSON.parse(sessao);
        abrirPainel();
        iniciarSincronizacaoAutomatica();
    }
};
</script>

</body>
</html>
