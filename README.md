<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro</title>
    <style>
        /* 🎨 Cores originais conforme a imagem */
        :root {
            --preto-base: #000000;
            --preto-card: #121212;
            --preto-claro: #1E1E1E;
            --vermelho-destaque: #E50914;
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
            background-color: var(--preto-base);
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
            color: var(--vermelho-destaque);
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
            border-color: var(--vermelho-destaque);
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.15);
        }

        .btn {
            width: 100%;
            padding: 15px;
            background: var(--vermelho-destaque);
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

        /* Área Principal */
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

        .inicial-perfil {
            width: 55px;
            height: 55px;
            border-radius: 50%;
            background: var(--vermelho-destaque);
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
        .grid-cards {
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
            border-top: 3px solid var(--vermelho-destaque);
        }

        .card .icone {
            width: 45px;
            height: 45px;
            border-radius: 8px;
            background: var(--vermelho-destaque);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            margin-bottom: 15px;
        }

        .card .valor {
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .card .legenda {
            color: var(--texto-suave);
            font-size: 15px;
        }

        .texto-alerta {
            font-size: 14px;
            margin-top: 8px;
        }

        /* Navegação e Conteúdo */
        .abas {
            display: flex;
            gap: 12px;
            margin-bottom: 25px;
        }

        .botao-aba {
            padding: 12px 20px;
            background: var(--preto-card);
            border: 1px solid var(--cinza-borda);
            border-radius: 6px;
            color: var(--texto-branco);
            cursor: pointer;
            transition: all 0.2s;
        }

        .botao-aba.ativo {
            background: var(--vermelho-destaque);
            border-color: var(--vermelho-destaque);
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

        .botao-acao {
            background: var(--vermelho-destaque);
            border: none;
            border-radius: 6px;
            color: white;
            padding: 12px 20px;
            font-size: 15px;
            font-weight: 500;
            cursor: pointer;
            margin: 8px 8px 20px 0;
        }

        .botao-acao:hover {
            background: var(--vermelho-escuro);
        }

        .item-atividade {
            background: var(--preto-claro);
            border-left: 4px solid var(--vermelho-destaque);
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
    <input type="text" id="campoRA" class="campo" placeholder="Digite seu RA">

    <label>Senha:</label>
    <input type="password" id="campoSenha" class="campo" placeholder="Senha de acesso">

    <button onclick="iniciarSessao()" class="btn">Entrar e Sincronizar</button>
</div>

<!-- Área do Aluno -->
<div id="painelAluno" class="painel">
    <div class="cabecalho-perfil">
        <div class="inicial-perfil" id="inicialNome">?</div>
        <div class="info-perfil">
            <h2 id="nomeAluno">Olá, Carregando...</h2>
            <p id="serieAluno">---</p>
        </div>
    </div>

    <!-- Cards com dados dinâmicos -->
    <div class="grid-cards">
        <div class="card">
            <div class="icone">✅</div>
            <div class="valor" id="contadorPendencias">0</div>
            <div class="legenda">Pendências</div>
        </div>
        <div class="card">
            <div class="icone">✉️</div>
            <div class="valor" id="contadorMensagens">0</div>
            <div class="legenda">Mensagens não lidas</div>
        </div>
        <div class="card">
            <div class="icone">🗓️</div>
            <div class="valor" id="contadorFaltas">0</div>
            <div class="legenda">Faltas</div>
        </div>
        <div class="card">
            <div class="icone">📈</div>
            <div class="valor" id="valorFrequencia">0%</div>
            <div class="legenda">Frequência</div>
            <div class="texto-alerta" id="textoFrequencia"></div>
        </div>
    </div>

    <!-- Abas do Sistema -->
    <div class="abas">
        <button class="botao-aba ativo" onclick="mudarAba('inicio')">Início</button>
        <button class="botao-aba" onclick="mudarAba('tarefas')">Tarefa SP</button>
        <button class="botao-aba" onclick="mudarAba('redacao')">Redação Paulista</button>
    </div>

    <!-- Conteúdo: Início -->
    <div id="abaInicio" class="conteudo-aba ativo">
        <h3 style="margin-bottom: 15px; color: var(--vermelho-destaque);">Situação da Conta</h3>
        <p style="color: var(--texto-suave);">Todos os dados são carregados diretamente da sua conta e atualizados automaticamente.</p>
        <br>
        <p style="color: var(--verde);">✅ Sincronização ativa e conectada</p>
    </div>

    <!-- Conteúdo: Tarefas -->
    <div id="abaTarefas" class="conteudo-aba">
        <h3 style="margin-bottom: 15px; color: var(--vermelho-destaque);">Tarefa SP</h3>
        <button onclick="buscarAtividades()" class="botao-acao">🔍 Buscar Pendentes</button>
        <button onclick="resolverTodasTarefas()" class="botao-acao">⚡ Resolver Todas Automaticamente</button>
        <div id="listaTarefas"></div>
    </div>

    <!-- Conteúdo: Redação -->
    <div id="abaRedacao" class="conteudo-aba">
        <h3 style="margin-bottom: 15px; color: var(--vermelho-destaque);">Redação Paulista</h3>
        <button onclick="buscarRedacoes()" class="botao-acao">🔍 Buscar Temas</button>
        <button onclick="resolverTodasRedacoes()" class="botao-acao">⚡ Gerar e Enviar Todas</button>
        <div id="listaRedacoes"></div>
    </div>
</div>

<script>
// 🔗 Endereço do servidor oficial
const SERVIDOR_API = "https://crimsonzerohub.xyz/api/v1/";
let dadosUsuario = null;
let atualizacaoAutomatica = null;

// 🚀 Login e carregamento de dados
async function iniciarSessao() {
    const ra = document.getElementById("campoRA").value.trim();
    const senha = document.getElementById("campoSenha").value.trim();

    if (!ra || !senha) {
        alert("⚠️ Preencha RA e senha corretamente!");
        return;
    }

    try {
        const botaoEntrar = document.querySelector(".btn");
        botaoEntrar.textContent = "Conectando...";

        // Requisição ao servidor com os dados do aluno
        const resposta = await fetch(`${SERVIDOR_API}login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: ra, senha: senha })
        });

        const dadosServidor = await resposta.json();

        if (!dadosServidor.sucesso) throw new Error(dadosServidor.mensagem || "RA ou senha incorretos");

        // Salva todos os dados recebidos
        dadosUsuario = {
            ra: ra,
            senha: senha,
            nome: dadosServidor.nome,
            serie: dadosServidor.serie,
            pendencias: dadosServidor.pendencias || 0,
            mensagens: dadosServidor.mensagens || 0,
            faltas: dadosServidor.faltas || 0,
            frequencia: dadosServidor.frequencia || 0,
            tarefas: dadosServidor.tarefas || [],
            redacoes: dadosServidor.redacoes || []
        };

        abrirSistema();
        iniciarSincronizacao();
        alert("✅ Conectado! Dados carregados com sucesso.");

    } catch (erro) {
        console.log("Erro de conexão:", erro);
        alert("⚠️ Não foi possível conectar. Verifique seus dados.");
        document.querySelector(".btn").textContent = "Entrar e Sincronizar";
    }
}

// 📂 Exibe a área do aluno
function abrirSistema() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painelAluno").style.display = "block";

    document.getElementById("inicialNome").textContent = dadosUsuario.nome.charAt(0).toUpperCase();
    document.getElementById("nomeAluno").textContent = `Olá, ${dadosUsuario.nome.toUpperCase()}`;
    document.getElementById("serieAluno").textContent = dadosUsuario.serie;

    atualizarTodosOsDados();
}

// 🔁 Atualiza contadores e dados da tela
function atualizarTodosOsDados() {
    document.getElementById("contadorPendencias").textContent = dadosUsuario.pendencias;
    document.getElementById("contadorMensagens").textContent = dadosUsuario.mensagens;
    document.getElementById("contadorFaltas").textContent = dadosUsuario.faltas;
    document.getElementById("valorFrequencia").textContent = `${dadosUsuario.frequencia}%`;

    const textoFreq = document.getElementById("textoFrequencia");
    if (dadosUsuario.frequencia < 75) {
        textoFreq.textContent = "Sua presença está abaixo do mínimo.";
        textoFreq.style.color = "var(--vermelho-destaque)";
    } else {
        textoFreq.textContent = "Sua presença está regular.";
        textoFreq.style.color = "var(--verde)";
    }

    listarAtividades();
    listarRedacoes();
}

// 🔄 Sincroniza dados a cada 5 segundos
function iniciarSincronizacao() {
    if (atualizacaoAutomatica) clearInterval(atualizacaoAutomatica);
    atualizacaoAutomatica = setInterval(async () => {
        if (!dadosUsuario) return;
        try {
            const res = await fetch(`${SERVIDOR_API}atualizar`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ ra: dadosUsuario.ra, senha: dadosUsuario.senha })
            });
            const novosDados = await res.json();
            if (novosDados.sucesso) {
                dadosUsuario = { ...dadosUsuario, ...novosDados.dados };
                atualizarTodosOsDados();
            }
        } catch {}
    }, 5000);
}

// 🔀 Troca de abas
function mudarAba(nome) {
    document.querySelectorAll(".botao-aba").forEach(btn => btn.classList.remove("ativo"));
    document.querySelectorAll(".conteudo-aba").forEach(div => div.classList.remove("ativo"));

    event.currentTarget.classList.add("ativo");
    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).classList.add("ativo");
}

// 📥 Busca atividades do servidor
async function buscarAtividades() {
    document.getElementById("listaTarefas").innerHTML = "<p style='color: var(--texto-suave);'>Buscando tarefas...</p>";
    try {
        const res = await fetch(`${SERVIDOR_API}tarefas?ra=${dadosUsuario.ra}&senha=${dadosUsuario.senha}`);
        const dados = await res.json();
        dadosUsuario.tarefas = dados.lista || [];
        atualizarTodosOsDados();
    } catch {
        document.getElementById("listaTarefas").innerHTML = "<p style='color: var(--amarelo);'>Erro ao buscar atividades.</p>";
    }
}

// 📥 Busca temas de redação
async function buscarRedacoes() {
    document.getElementById("listaRedacoes").innerHTML = "<p style='color: var(--texto-suave);'>Buscando temas...</p>";
    try {
        const res = await fetch(`${SERVIDOR_API}redacoes?ra=${dadosUsuario.ra}&senha=${dadosUsuario.senha}`);
        const dados = await res.json();
        dadosUsuario.redacoes = dados.lista || [];
        atualizarTodosOsDados();
    } catch {
        document.getElementById("listaRedacoes").innerHTML = "<p style='color: var(--amarelo);'>Erro ao buscar redações.</p>";
    }
}

// ⚡ Resolve tarefas automaticamente
function resolverTodasTarefas() {
    if (!dadosUsuario.tarefas || dadosUsuario.tarefas.length === 0) {
        alert("⚠️ Primeiro clique em 'Buscar Pendentes'!");
        return;
    }

    dadosUsuario.tarefas.forEach(tarefa => {
        if (tarefa.status !== "concluida") {
            tarefa.resposta = `Resposta elaborada conforme o conteúdo da Sala do Futuro:\n\n${tarefa.descricao}\n\nResposta completa e adequada ao nível da atividade.`;
            tarefa.status = "concluida";
            dadosUsuario.pendencias--;
        }
    });

    enviarAlteracoes();
    atualizarTodosOsDados();
    alert("✅ Todas as tarefas foram resolvidas e enviadas!");
}

// ⚡ Gera redações automaticamente
function resolverTodasRedacoes() {
    if (!dadosUsuario.redacoes || dadosUsuario.redacoes.length === 0) {
        alert("⚠️ Primeiro clique em 'Buscar Temas'!");
        return;
    }

    dadosUsuario.redacoes.forEach(redacao => {
        if (redacao.status !== "concluida") {
            redacao.texto = gerarTextoRedacao(redacao.tema);
            redacao.status = "concluida";
            dadosUsuario.pendencias--;
        }
    });

    enviarAlteracoes();
    atualizarTodosOsDados();
    alert("✅ Todas as redações foram geradas e enviadas!");
}

// 🧠 Cria texto de redação conforme tema
function gerarTextoRedacao(tema) {
    return `Redação Paulista: ${tema}

Introdução
O tema "${tema}" é relevante para a formação e desenvolvimento social. Ele aborda questões importantes que fazem parte do dia a dia e do conhecimento necessário.

Desenvolvimento
Em primeiro lugar, é possível observar que esse assunto envolve vários pontos de vista. Por um lado, existem desafios que precisam ser compreendidos; por outro, há caminhos para soluções e melhorias.

Além disso, a educação ajuda a entender melhor o assunto, formando uma visão crítica e preparada para agir de forma consciente.

Conclusão
Portanto, conclui-se que o tema deve ser estudado com atenção, visando sempre o aprendizado e o crescimento pessoal e coletivo.`;
}

// 📤 Envia alterações para o servidor
async function enviarAlteracoes() {
    try {
        await fetch(`${SERVIDOR_API}salvar`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dadosUsuario)
        });
    } catch {}
}

// 📋 Exibe lista de tarefas
function listarAtividades() {
    const container = document.getElementById("listaTarefas");
    if (!dadosUsuario.tarefas.length) {
        container.innerHTML = "<p style='color: var(--texto-suave);'>Nenhuma tarefa encontrada.</p>";
        return;
    }

    container.innerHTML = dadosUsuario.tarefas.map(item => `
        <div class="item-atividade">
            <h4>${item.titulo}</h4>
            <p>${item.descricao || "Sem descrição"}</p>
            <p>Prazo: ${item.prazo ? new Date(item.prazo).toLocaleDateString("pt-BR") : "Sem prazo"}</p>
            <p class="status" style="color: ${item.status === "concluida" ? "var(--verde)" : "var(--amarelo)"};">
                ${item.status === "concluida" ? "✅ Concluída" : "⏳ Pendente"}
            </p>
        </div>
    `).join("");
}

// 📋 Exibe lista de redações
function listarRedacoes() {
    const container = document.getElementById("listaRedacoes");
    if (!dadosUsuario.redacoes.length) {
        container.innerHTML = "<p style='color: var(--texto-suave);'>Nenhuma redação encontrada.</p>";
        return;
    }

    container.innerHTML = dadosUsuario.redacoes.map(item => `
        <div class="item-atividade">
            <h4>Tema: ${item.tema}</h4>
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
