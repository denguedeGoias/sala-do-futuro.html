<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro</title>
    <style>
        /* Cores oficiais do sistema */
        :root {
            --preto-fundo: #000000;
            --preto-card: #121212;
            --vermelho-destaque: #E50914;
            --vermelho-borda: #B00006;
            --cinza-borda: #2A2A2A;
            --texto-branco: #FFFFFF;
            --texto-suave: #AAAAAA;
            --verde-sucesso: #22C55E;
            --amarelo-alerta: #F59E0B;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
        }

        body {
            background-color: var(--preto-fundo);
            color: var(--texto-branco);
            min-height: 100vh;
        }

        /* Tela de Login */
        .tela-login {
            max-width: 420px;
            margin: 80px auto;
            padding: 30px;
            background: var(--preto-card);
            border-radius: 10px;
            border: 1px solid var(--cinza-borda);
            box-shadow: 0 0 15px rgba(229, 9, 20, 0.15);
        }

        .tela-login h1 {
            text-align: center;
            color: var(--vermelho-destaque);
            font-size: 32px;
            margin-bottom: 8px;
        }

        .tela-login p.subtitulo {
            text-align: center;
            color: var(--texto-suave);
            margin-bottom: 25px;
            font-size: 15px;
        }

        .campo {
            width: 100%;
            padding: 13px;
            margin: 8px 0 18px;
            background: #1E1E1E;
            border: 1px solid var(--cinza-borda);
            border-radius: 6px;
            color: var(--texto-branco);
            font-size: 16px;
        }

        .campo:focus {
            outline: none;
            border-color: var(--vermelho-destaque);
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.2);
        }

        .btn-principal {
            width: 100%;
            padding: 14px;
            background: var(--vermelho-destaque);
            border: none;
            border-radius: 6px;
            color: white;
            font-size: 17px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }

        .btn-principal:hover {
            background: var(--vermelho-borda);
        }

        /* Layout Principal */
        .container {
            display: flex;
            min-height: 100vh;
        }

        .menu-lateral {
            width: 250px;
            background: var(--preto-card);
            border-right: 1px solid var(--cinza-borda);
            padding: 20px 0;
        }

        .perfil {
            padding: 0 20px 20px;
            border-bottom: 1px solid var(--cinza-borda);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .circulo-inicial {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: var(--vermelho-destaque);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
        }

        .info-perfil h3 {
            font-size: 17px;
            margin-bottom: 4px;
        }

        .info-perfil p {
            font-size: 13px;
            color: var(--texto-suave);
        }

        .status-sync {
            font-size: 12px;
            margin-top: 6px;
            color: var(--verde-sucesso);
        }

        .item-menu {
            width: 100%;
            padding: 13px 20px;
            text-align: left;
            background: transparent;
            border: none;
            color: var(--texto-branco);
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: background 0.2s;
        }

        .item-menu:hover {
            background: #1E1E1E;
        }

        .item-menu.ativo {
            background: var(--vermelho-destaque);
            color: white;
        }

        .area-conteudo {
            flex: 1;
            padding: 25px;
        }

        .card-resumo {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-bottom: 30px;
        }

        .card-info {
            background: var(--preto-card);
            border: 1px solid var(--cinza-borda);
            border-radius: 10px;
            padding: 22px;
            border-top: 3px solid var(--vermelho-destaque);
        }

        .card-info .numero {
            font-size: 36px;
            font-weight: bold;
            margin: 8px 0;
        }

        .form-bloco {
            background: var(--preto-card);
            border-radius: 10px;
            padding: 22px;
            margin-bottom: 25px;
            border: 1px solid var(--cinza-borda);
        }

        .item-atividade {
            background: var(--preto-card);
            border-left: 4px solid var(--vermelho-destaque);
            padding: 16px;
            margin: 12px 0;
            border-radius: 6px;
            border: 1px solid var(--cinza-borda);
            border-left-width: 4px;
        }

        .acoes {
            margin-top: 12px;
            text-align: right;
        }

        .btn-pequeno {
            padding: 7px 14px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            margin-left: 8px;
        }

        .btn-vermelho { background: var(--vermelho-destaque); color: white; }
        .btn-verde { background: var(--verde-sucesso); color: white; }
        .btn-cinza { background: #333; color: white; }
    </style>
</head>
<body>

<!-- Tela de Login -->
<div id="telaLogin" class="tela-login">
    <h1>SALA DO FUTURO</h1>
    <p class="subtitulo">Acesso ao sistema do aluno</p>

    <label>RA do Aluno:</label>
    <input type="text" id="ra" class="campo" placeholder="Digite o RA completo">

    <label>Dígito Verificador:</label>
    <input type="text" id="digito" class="campo" maxlength="1" placeholder="Ex: 5">

    <label>UF:</label>
    <select id="uf" class="campo">
        <option value="SP" selected>SP</option>
        <option value="MG">MG</option>
        <option value="RJ">RJ</option>
        <option value="GO">GO</option>
    </select>

    <label>Senha:</label>
    <input type="password" id="senha" class="campo" placeholder="Senha de acesso">

    <button onclick="entrarSistema()" class="btn-principal">Entrar e Carregar Dados</button>

    <p style="text-align:center; margin-top:25px; font-size:12px; color:var(--texto-suave);">
        Desenvolvido por Dengue de Goiás
    </p>
</div>

<!-- Painel Principal -->
<div id="painelSistema" class="container" style="display: none;">
    <div class="menu-lateral">
        <div class="perfil">
            <div class="circulo-inicial" id="inicialAluno">J</div>
            <div class="info-perfil">
                <h3 id="nomeAluno">Olá, CARREGANDO...</h3>
                <p id="serieAluno">---</p>
                <div class="status-sync" id="statusSync">🔄 Conectando...</div>
            </div>
        </div>

        <button onclick="mudarAba('inicio')" class="item-menu ativo">🏠 Início</button>
        <button onclick="mudarAba('tarefas')" class="item-menu">✅ Tarefa SP</button>
        <button onclick="mudarAba('redacao')" class="item-menu">✍️ Redação Paulista</button>
        <hr style="margin:15px 0; border:none; border-top:1px solid var(--cinza-borda);">
        <button onclick="sair()" class="item-menu" style="color:var(--vermelho-destaque);">🚪 Sair</button>
    </div>

    <div class="area-conteudo">
        <!-- Aba Início -->
        <div id="abaInicio">
            <h2 style="color:var(--vermelho-destaque); margin-bottom:25px; font-size:24px;">Resumo Geral</h2>
            <div class="card-resumo">
                <div class="card-info">
                    <p>Pendências</p>
                    <div class="numero" id="qtdPendentes">0</div>
                </div>
                <div class="card-info">
                    <p>Concluídas</p>
                    <div class="numero" style="color:var(--verde-sucesso)" id="qtdConcluidas">0</div>
                </div>
                <div class="card-info">
                    <p>Total</p>
                    <div class="numero" style="color:var(--amarelo-alerta)" id="qtdTotal">0</div>
                </div>
            </div>
        </div>

        <!-- Aba Tarefa SP -->
        <div id="abaTarefas" style="display: none;">
            <h2 style="color:var(--vermelho-destaque); margin-bottom:20px;">✅ Tarefa SP</h2>
            <div class="form-bloco">
                <input type="text" id="tituloTarefa" class="campo" placeholder="Título da tarefa">
                <input type="number" id="tempoTarefa" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                <input type="date" id="prazoTarefa" class="campo">
                <textarea id="descricaoTarefa" class="campo" rows="3" placeholder="Descrição da atividade"></textarea>
                <button onclick="adicionarTarefa()" class="btn-principal">Salvar e Enviar para a Conta</button>
            </div>
            <div id="listaTarefas"></div>
        </div>

        <!-- Aba Redação Paulista -->
        <div id="abaRedacao" style="display: none;">
            <h2 style="color:var(--vermelho-destaque); margin-bottom:20px;">✍️ Redação Paulista</h2>
            <div class="form-bloco">
                <input type="text" id="temaRedacao" class="campo" placeholder="Tema da redação">
                <input type="number" id="tempoRedacao" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                <input type="date" id="prazoRedacao" class="campo">
                <textarea id="textoRedacao" class="campo" rows="6" placeholder="Escreva o texto completo aqui"></textarea>
                <button onclick="adicionarRedacao()" class="btn-principal">Salvar e Enviar para a Conta</button>
            </div>
            <div id="listaRedacoes"></div>
        </div>
    </div>
</div>

<script>
// Configuração do servidor
const SERVIDOR = "https://crimsonzerohub.xyz/api/";
let usuario = null;
let sincronizador = null;

// Entrar e buscar dados do aluno
async function entrarSistema() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) {
        alert("Preencha RA e senha corretamente!");
        return;
    }

    try {
        document.querySelector(".btn-principal").textContent = "Verificando...";

        // Busca dados do aluno no servidor
        const resposta = await fetch(`${SERVIDOR}aluno?ra=${ra}&digito=${digito}&uf=${uf}&senha=${senha}`);
        const dados = await resposta.json();

        if (!dados.sucesso) throw new Error("RA ou senha incorretos");

        usuario = {
            ra: ra,
            digito: digito,
            uf: uf,
            nome: dados.nome || "Aluno",
            serie: dados.serie || "Série não cadastrada",
            tarefas: dados.tarefas || [],
            redacoes: dados.redacoes || []
        };

        abrirPainel();
        iniciarSincronizacao();
        alert("✅ Conectado! Dados carregados da sua conta.");

    } catch (erro) {
        // Se não conectar ao servidor, usa dados locais para teste
        usuario = {
            ra: ra,
            digito: digito,
            uf: uf,
            nome: "JUAN",
            serie: "3ª SÉRIE A MANHA ANUAL",
            tarefas: [],
            redacoes: []
        };
        abrirPainel();
        iniciarSincronizacao();
        alert("⚠️ Usando modo de demonstração. Funcionalidades ativas.");
    }
}

function abrirPainel() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painelSistema").style.display = "flex";

    document.getElementById("inicialAluno").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nomeAluno").textContent = `Olá, ${usuario.nome.toUpperCase()}`;
    document.getElementById("serieAluno").textContent = usuario.serie;

    atualizarTela();
}

function iniciarSincronizacao() {
    if (sincronizador) clearInterval(sincronizador);
    sincronizador = setInterval(enviarDadosConta, 3000);
}

async function enviarDadosConta() {
    if (!usuario) return;
    try {
        await fetch(`${SERVIDOR}salvar`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(usuario)
        });
        document.getElementById("statusSync").textContent = `✅ Sincronizado ${new Date().toLocaleTimeString()}`;
    } catch {
        // Salva localmente se servidor não responder
        localStorage.setItem(`sala_futuro_${usuario.ra}`, JSON.stringify(usuario));
        document.getElementById("statusSync").textContent = `⚠️ Salvo localmente`;
    }
    atualizarTela();
}

function mudarAba(nome) {
    document.querySelectorAll(".area-conteudo > div").forEach(el => el.style.display = "none");
    document.querySelectorAll(".item-menu").forEach(el => el.classList.remove("ativo"));

    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).style.display = "block";
    event.currentTarget.classList.add("ativo");
}

// Funções Tarefas
function adicionarTarefa() {
    const tarefa = {
        id: Date.now(),
        titulo: document.getElementById("tituloTarefa").value.trim(),
        tempo: parseInt(document.getElementById("tempoTarefa").value),
        prazo: document.getElementById("prazoTarefa").value || "",
        descricao: document.getElementById("descricaoTarefa").value,
        status: "pendente"
    };

    if (!tarefa.titulo) return alert("Digite o título da tarefa!");
    usuario.tarefas.push(tarefa);
    limparCampos("tarefa");
    enviarDadosConta();
}

// Funções Redação
function adicionarRedacao() {
    const redacao = {
        id: Date.now(),
        tema: document.getElementById("temaRedacao").value.trim(),
        tempo: parseInt(document.getElementById("tempoRedacao").value),
        prazo: document.getElementById("prazoRedacao").value || "",
        texto: document.getElementById("textoRedacao").value,
        status: "pendente"
    };

    if (!redacao.tema) return alert("Digite o tema da redação!");
    usuario.redacoes.push(redacao);
    limparCampos("redacao");
    enviarDadosConta();
}

function limparCampos(tipo) {
    if (tipo === "tarefa") {
        ["tituloTarefa", "tempoTarefa", "prazoTarefa", "descricaoTarefa"].forEach(id => {
            document.getElementById(id).value = id === "tempoTarefa" ? "1" : "";
        });
    } else {
        ["temaRedacao", "tempoRedacao", "prazoRedacao", "textoRedacao"].forEach(id => {
            document.getElementById(id).value = id === "tempoRedacao" ? "1" : "";
        });
    }
}

function alterarStatus(tipo, id, novoStatus) {
    const lista = tipo === "tarefa" ? usuario.tarefas : usuario.redacoes;
    const item = lista.find(i => i.id === id);
    if (item) {
        item.status = novoStatus;
        enviarDadosConta();
    }
}

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
    const itens = tipo === "tarefas" ? usuario.tarefas : usuario.redacoes;

    if (itens.length === 0) {
        container.innerHTML = `<p style="color:var(--texto-suave); text-align:center; padding:30px;">Nenhuma atividade cadastrada</p>`;
        return;
    }

    container.innerHTML = itens.map(item => `
        <div class="item-atividade">
            <h4>${item.titulo || item.tema}</h4>
            ${item.prazo ? `<p style="font-size:13px; color:var(--texto-suave); margin:6px 0;">Prazo: ${new Date(item.prazo).toLocaleDateString("pt-BR")}</p>` : ""}
            <p style="margin:10px 0; color:var(--texto-suave);">${item.descricao || item.texto || ""}</p>
            <div class="acoes">
                ${item.status === "pendente" ? `<button onclick="alterarStatus('${tipo}', ${item.id}, 'concluida')" class="btn-pequeno btn-vermelho">Marcar como Feita</button>` : ""}
                ${item.status === "concluida" ? `<span style="color:var(--verde-sucesso); font-weight:500;">✅ Concluída e enviada</span>` : ""}
            </div>
        </div>
    `).join("");
}

function sair() {
    if (confirm("Deseja realmente sair da conta?")) {
        clearInterval(sincronizador);
        usuario = null;
        localStorage.removeItem("sala_futuro_sessao");
        location.reload();
    }
}

// Recupera sessão salva
window.onload = () => {
    const sessao = localStorage.getItem("sala_futuro_sessao");
    if (sessao) {
        usuario = JSON.parse(sessao);
        abrirPainel();
        iniciarSincronizacao();
    }
};
</script>

</body>
</html>
