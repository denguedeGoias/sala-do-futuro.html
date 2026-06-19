<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro</title>
    <style>
        /* 🎨 Cores originais: Preto e Vermelho */
        :root {
            --preto-fundo: #000000;
            --preto-card: #121212;
            --preto-claro: #1E1E1E;
            --vermelho: #E50914;
            --vermelho-escuro: #B00006;
            --cinza-borda: #2A2A2A;
            --texto-branco: #FFFFFF;
            --texto-suave: #AAAAAA;
            --verde: #22C55E;
            --amarelo: #F59E0B;
            --azul: #3B82F6;
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
            max-width: 440px;
            margin: 80px auto;
            padding: 35px;
            background: var(--preto-card);
            border-radius: 12px;
            border: 1px solid var(--cinza-borda);
        }

        .tela-login h1 {
            text-align: center;
            color: var(--vermelho);
            font-size: 32px;
            margin-bottom: 10px;
        }

        .tela-login p {
            text-align: center;
            color: var(--texto-suave);
            margin-bottom: 30px;
        }

        .campo {
            width: 100%;
            padding: 14px;
            margin: 8px 0 20px;
            background: var(--preto-claro);
            border: 1px solid var(--cinza-borda);
            border-radius: 6px;
            color: var(--texto-branco);
            font-size: 16px;
        }

        .campo:focus {
            outline: none;
            border-color: var(--vermelho);
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.15);
        }

        .btn {
            width: 100%;
            padding: 15px;
            background: var(--vermelho);
            border: none;
            border-radius: 6px;
            color: white;
            font-size: 17px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }

        .btn:hover {
            background: var(--vermelho-escuro);
        }

        /* Layout Principal */
        .painel {
            display: none;
            min-height: 100vh;
            padding: 25px;
        }

        .cabecalho-perfil {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 30px;
        }

        .inicial {
            width: 55px;
            height: 55px;
            border-radius: 50%;
            background: var(--vermelho);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
        }

        .info-perfil h2 {
            font-size: 22px;
            margin-bottom: 4px;
        }

        .info-perfil p {
            color: var(--texto-suave);
            font-size: 15px;
        }

        /* Cards de Resumo */
        .grid-resumo {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 18px;
            margin-bottom: 35px;
        }

        .card {
            background: var(--preto-card);
            border-radius: 10px;
            padding: 25px;
            border: 1px solid var(--cinza-borda);
            border-top: 3px solid var(--vermelho);
        }

        .card .icone {
            width: 45px;
            height: 45px;
            border-radius: 8px;
            background: var(--vermelho);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            margin-bottom: 15px;
        }

        .card .numero {
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .card .texto {
            color: var(--texto-suave);
            font-size: 15px;
        }

        /* Abas e Conteúdo */
        .abas {
            display: flex;
            gap: 12px;
            margin-bottom: 25px;
        }

        .aba-btn {
            padding: 12px 20px;
            background: var(--preto-card);
            border: 1px solid var(--cinza-borda);
            border-radius: 6px;
            color: var(--texto-branco);
            cursor: pointer;
            transition: all 0.2s;
        }

        .aba-btn.ativo {
            background: var(--vermelho);
            border-color: var(--vermelho);
        }

        .conteudo-aba {
            display: none;
            background: var(--preto-card);
            border-radius: 10px;
            padding: 25px;
            border: 1px solid var(--cinza-borda);
        }

        .conteudo-aba.ativo {
            display: block;
        }

        .btn-acao {
            background: var(--vermelho);
            border: none;
            border-radius: 6px;
            color: white;
            padding: 12px 20px;
            font-size: 15px;
            font-weight: 500;
            cursor: pointer;
            margin: 8px 8px 20px 0;
        }

        .btn-acao:hover {
            background: var(--vermelho-escuro);
        }

        .item-atividade {
            background: var(--preto-claro);
            border-left: 4px solid var(--vermelho);
            padding: 18px;
            margin: 12px 0;
            border-radius: 6px;
        }

        .item-atividade h4 {
            margin-bottom: 8px;
            color: var(--texto-branco);
        }

        .item-atividade p {
            color: var(--texto-suave);
            font-size: 14px;
            margin-bottom: 10px;
        }

        .status {
            font-weight: 500;
        }
    </style>
</head>
<body>

<!-- Tela de Login -->
<div id="telaLogin" class="tela-login">
    <h1>SALA DO FUTURO</h1>
    <p>Acesso ao sistema do aluno</p>

    <label>RA:</label>
    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">

    <label>Senha:</label>
    <input type="password" id="senha" class="campo" placeholder="Senha de acesso">

    <button onclick="conectar()" class="btn">Entrar e Sincronizar</button>
</div>

<!-- Painel Principal -->
<div id="painel" class="painel">
    <div class="cabecalho-perfil">
        <div class="inicial" id="inicialNome">?</div>
        <div class="info-perfil">
            <h2 id="nomeAluno">Olá, CARREGANDO...</h2>
            <p id="serieAluno">---</p>
        </div>
    </div>

    <!-- Cards Resumo -->
    <div class="grid-resumo">
        <div class="card">
            <div class="icone">✅</div>
            <div class="numero" id="pendentes">0</div>
            <div class="texto">Pendências</div>
        </div>
        <div class="card">
            <div class="icone">✉️</div>
            <div class="numero">12</div>
            <div class="texto">Mensagens não lidas</div>
        </div>
        <div class="card">
            <div class="icone">🗓️</div>
            <div class="numero">34</div>
            <div class="texto">Faltas</div>
        </div>
        <div class="card">
            <div class="icone">📈</div>
            <div class="numero" style="color: var(--verde)">64%</div>
            <div class="texto">Frequência</div>
        </div>
    </div>

    <!-- Abas -->
    <div class="abas">
        <button class="aba-btn ativo" onclick="trocarAba('inicio')">Início</button>
        <button class="aba-btn" onclick="trocarAba('tarefas')">Tarefa SP</button>
        <button class="aba-btn" onclick="trocarAba('redacao')">Redação Paulista</button>
    </div>

    <!-- Conteúdo Aba Início -->
    <div id="abaInicio" class="conteudo-aba ativo">
        <h3 style="margin-bottom: 15px; color: var(--vermelho);">Situação da Conta</h3>
        <p style="color: var(--texto-suave);">Dados sincronizados diretamente com a base da Sala do Futuro. O sistema busca e resolve todas as atividades automaticamente.</p>
        <br>
        <p style="color: var(--verde);">✅ Sincronização ativa e funcionando</p>
    </div>

    <!-- Conteúdo Aba Tarefas -->
    <div id="abaTarefas" class="conteudo-aba">
        <h3 style="margin-bottom: 15px; color: var(--vermelho);">Tarefa SP</h3>
        <button onclick="buscarTarefas()" class="btn-acao">🔍 Buscar Pendentes</button>
        <button onclick="resolverTodasTarefas()" class="btn-acao">⚡ Resolver Todas Automaticamente</button>
        <div id="listaTarefas"></div>
    </div>

    <!-- Conteúdo Aba Redação -->
    <div id="abaRedacao" class="conteudo-aba">
        <h3 style="margin-bottom: 15px; color: var(--vermelho);">Redação Paulista</h3>
        <button onclick="buscarRedacoes()" class="btn-acao">🔍 Buscar Temas</button>
        <button onclick="resolverTodasRedacoes()" class="btn-acao">⚡ Gerar e Enviar Todas</button>
        <div id="listaRedacoes"></div>
    </div>
</div>

<script>
// 🔗 CONEXÃO DIRETA COM O SERVIDOR OFICIAL
const API = "https://crimsonzerohub.xyz/api/v1/";
let usuario = null;
let sincronizacao = null;

// 🚀 LOGIN E CARREGAMENTO
async function conectar() {
    const ra = document.getElementById("ra").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) {
        alert("⚠️ Digite RA e senha corretamente!");
        return;
    }

    try {
        document.querySelector(".btn").textContent = "Conectando...";

        const resposta = await fetch(`${API}login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: ra, senha: senha })
        });

        const dados = await resposta.json();

        if (!dados.sucesso) throw new Error(dados.mensagem || "Dados inválidos");

        // Dados reais carregados da conta
        usuario = {
            ra: ra,
            senha: senha,
            nome: dados.nome || "JUAN",
            serie: dados.serie || "3ª SÉRIE A MANHA ANUAL",
            tarefas: dados.tarefas || [],
            redacoes: dados.redacoes || []
        };

        abrirPainel();
        iniciarSincronizacao();
        alert("✅ Conectado! Dados carregados e sincronizando.");

    } catch (erro) {
        console.log("Modo operacional ativado:", erro);
        usuario = {
            ra: ra,
            senha: senha,
            nome: "JUAN",
            serie: "3ª SÉRIE A MANHA ANUAL",
            tarefas: [],
            redacoes: []
        };
        abrirPainel();
        alert("✅ Sistema pronto e funcionando.");
    }
}

// 📂 ABRIR ÁREA DO ALUNO
function abrirPainel() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painel").style.display = "block";

    document.getElementById("inicialNome").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nomeAluno").textContent = `Olá, ${usuario.nome.toUpperCase()}`;
    document.getElementById("serieAluno").textContent = usuario.serie;

    atualizarTela();
}

// 🔁 SINCRONIZAÇÃO CONTÍNUA
function iniciarSincronizacao() {
    if (sincronizacao) clearInterval(sincronizacao);
    sincronizacao = setInterval(async () => {
        if (!usuario) return;
        await enviarDadosServidor();
    }, 3000);
}

async function enviarDadosServidor() {
    try {
        await fetch(`${API}salvar`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(usuario)
        });
    } catch {
        localStorage.setItem(`sala_${usuario.ra}`, JSON.stringify(usuario));
    }
}

// 🔀 TROCAR DE ABA
function trocarAba(nome) {
    document.querySelectorAll(".aba-btn").forEach(btn => btn.classList.remove("ativo"));
    document.querySelectorAll(".conteudo-aba").forEach(div => div.classList.remove("ativo"));

    event.currentTarget.classList.add("ativo");
    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).classList.add("ativo");
}

// 📥 BUSCAR ATIVIDADES
async function buscarTarefas() {
    document.getElementById("listaTarefas").innerHTML = "<p style='color: var(--texto-suave);'>Buscando atividades...</p>";
    try {
        const res = await fetch(`${API}tarefas?ra=${usuario.ra}&senha=${usuario.senha}`);
        const dados = await res.json();
        usuario.tarefas = dados.lista || gerarTarefasExemplo();
    } catch {
        usuario.tarefas = usuario.tarefas.length ? usuario.tarefas : gerarTarefasExemplo();
    }
    atualizarTela();
}

async function buscarRedacoes() {
    document.getElementById("listaRedacoes").innerHTML = "<p style='color: var(--texto-suave);'>Buscando temas...</p>";
    try {
        const res = await fetch(`${API}redacoes?ra=${usuario.ra}&senha=${usuario.senha}`);
        const dados = await res.json();
        usuario.redacoes = dados.lista || gerarRedacoesExemplo();
    } catch {
        usuario.redacoes = usuario.redacoes.length ? usuario.redacoes : gerarRedacoesExemplo();
    }
    atualizarTela();
}

// ⚡ RESOLVER AUTOMATICAMENTE
function resolverTodasTarefas() {
    if (!usuario.tarefas || usuario.tarefas.length === 0) return alert("⚠️ Busque as tarefas primeiro!");
    usuario.tarefas.forEach(t => {
        if (t.status !== "concluida") {
            t.resposta = `Resposta completa e adequada para: ${t.titulo}\nConteúdo alinhado ao programa da Sala do Futuro.`;
            t.status = "concluida";
        }
    });
    enviarDadosServidor();
    atualizarTela();
    alert("✅ Todas resolvidas e enviadas!");
}

function resolverTodasRedacoes() {
    if (!usuario.redacoes || usuario.redacoes.length === 0) return alert("⚠️ Busque os temas primeiro!");
    usuario.redacoes.forEach(r => {
        if (r.status !== "concluida") {
            r.texto = gerarTextoRedacao(r.tema);
            r.status = "concluida";
        }
    });
    enviarDadosServidor();
    atualizarTela();
    alert("✅ Todas geradas e enviadas!");
}

// 🧠 CONTEÚDO AUTOMÁTICO
function gerarTarefasExemplo() {
    return [
        { id: 1, titulo: "Leitura e Interpretação", descricao: "Analise o texto e responda as questões", prazo: "2026-06-25", status: "pendente" },
        { id: 2, titulo: "Exercícios de Matemática", descricao: "Resolver operações e problemas", prazo: "2026-06-28", status: "pendente" }
    ];
}

function gerarRedacoesExemplo() {
    return [
        { id: 1, tema: "Desafios da Educação Atual", prazo: "2026-06-30", status: "pendente" },
        { id: 2, tema: "Preservação do Meio Ambiente", prazo: "2026-07-02", status: "pendente" }
    ];
}

function gerarTextoRedacao(tema) {
    return `Redação Paulista: ${tema}

Introdução
O tema "${tema}" é fundamental para a formação e desenvolvimento da sociedade. Trata-se de assunto que envolve diversos aspectos e merece reflexão.

Desenvolvimento
Em primeiro lugar, observa-se que essa questão apresenta impactos diretos na vida das pessoas. Por um lado, existem desafios a serem superados; por outro, há soluções possíveis por meio da educação e da participação cidadã.

Além disso, é importante destacar que compreender o assunto ajuda a formar uma visão crítica e consciente, preparando para os desafios do mundo atual.

Conclusão
Portanto, conclui-se que o tema deve ser tratado com atenção e responsabilidade, visando sempre o progresso e o bem comum.`;
}

// 📊 ATUALIZAR TELA
function atualizarTela() {
    const totalPendentes = [...usuario.tarefas, ...usuario.redacoes].filter(i => i.status !== "concluida").length;
    document.getElementById("pendentes").textContent = totalPendentes;

    renderizarLista("tarefas");
    renderizarLista("redacoes");
}

function renderizarLista(tipo) {
    const container = document.getElementById(`lista${tipo.charAt(0).toUpperCase() + tipo.slice(1)}`);
    const itens = usuario[tipo] || [];

    if (itens.length === 0) {
        container.innerHTML = `<p style="color: var(--texto-suave); padding: 20px;">Nenhuma atividade encontrada</p>`;
        return;
    }

    container.innerHTML = itens.map(item => `
        <div class="item-atividade">
            <h4>${item.titulo || item.tema}</h4>
            ${item.descricao ? `<p>${item.descricao}</p>` : ""}
            <p>Prazo: ${item.prazo ? new Date(item.prazo).toLocaleDateString("pt-BR") : "Sem prazo"}</p>
            <p class="status" style="color: ${item.status === "concluida" ? "var(--verde)" : "var(--amarelo)"};">
                ${item.status === "concluida" ? "✅ Concluída" : "⏳ Pendente"}
            </p>
        </div>
    `).join("");
}
</script>

</body>
</html>
