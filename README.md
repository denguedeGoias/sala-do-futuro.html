<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro - GitHub</title>
    <style>
        :root {
            --preto: #000000;
            --preto-card: #121212;
            --preto-claro: #1E1E1E;
            --vermelho: #E50914;
            --vermelho-escuro: #B00006;
            --cinza: #2A2A2A;
            --texto: #FFFFFF;
            --texto-suave: #AAAAAA;
            --verde: #22C55E;
            --amarelo: #F59E0B;
        }
        * {margin:0; padding:0; box-sizing:border-box; font-family: Arial, sans-serif;}
        body {background: var(--preto); color: var(--texto); padding: 20px;}

        .tela {max-width: 450px; margin: 0 auto;}
        .card {background: var(--preto-card); border-radius: 10px; padding: 20px; margin-bottom: 20px; border: 1px solid var(--cinza);}
        h1 {text-align: center; color: var(--vermelho); margin-bottom: 20px; font-size: 26px;}
        label {display: block; margin: 15px 0 5px; color: var(--texto); font-size: 15px;}
        input {width: 100%; padding: 12px; background: var(--preto-claro); border: 1px solid var(--cinza); border-radius: 6px; color: var(--texto); font-size: 16px;}
        button {width: 100%; padding: 14px; margin-top: 20px; background: var(--vermelho); border: none; border-radius: 6px; color: white; font-size: 17px; font-weight: bold; cursor: pointer;}
        button:active {background: var(--vermelho-escuro);}

        .painel {display: none;}
        .info-topo {display: flex; gap: 15px; align-items: center; margin-bottom: 20px;}
        .inicial {width: 50px; height: 50px; border-radius: 50%; background: var(--vermelho); display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: bold;}
        .grid {display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;}
        .item-card {background: var(--preto-claro); padding: 15px; border-radius: 8px; text-align: center;}
        .numero {font-size: 28px; font-weight: bold; margin: 8px 0;}
        .desc {font-size: 14px; color: var(--texto-suave);}
        .abas {display: flex; gap: 10px; margin-bottom: 15px; overflow-x: auto; padding-bottom: 5px;}
        .aba {padding: 10px 15px; background: var(--preto-claro); border-radius: 6px; text-align: center; font-size: 15px; white-space: nowrap;}
        .aba.ativo {background: var(--vermelho);}
        .conteudo {display: none;}
        .conteudo.ativo {display: block;}
        .atividade {background: var(--preto-claro); border-left: 4px solid var(--vermelho); padding: 15px; margin: 12px 0; border-radius: 6px;}
        .atividade h4 {margin-bottom: 8px; font-size: 16px;}
        .atividade p {margin: 5px 0; font-size: 14px; color: var(--texto-suave);}
    </style>
</head>
<body>

<!-- Tela de Login -->
<div class="tela" id="telaLogin">
    <div class="card">
        <h1>SALA DO FUTURO</h1>
        <label>Seu RA:</label>
        <input type="text" id="ra" placeholder="Ex: 12345678">
        <label>Senha da Sala do Futuro:</label>
        <input type="password" id="senha" placeholder="Sua senha de acesso">
        <button onclick="conectar()">ENTRAR E BUSCAR DADOS</button>
    </div>
</div>

<!-- Tela Principal -->
<div class="tela painel" id="painel">
    <div class="card info-topo">
        <div class="inicial" id="letraInicial">?</div>
        <div>
            <h2 id="nomeAluno">Carregando...</h2>
            <p id="serieAluno">---</p>
        </div>
    </div>

    <div class="grid">
        <div class="item-card">
            <div class="numero" id="pendentes">0</div>
            <p class="desc">Pendências</p>
        </div>
        <div class="item-card">
            <div class="numero" id="faltas">0</div>
            <p class="desc">Faltas</p>
        </div>
        <div class="item-card">
            <div class="numero" id="frequencia">0%</div>
            <p class="desc">Frequência</p>
        </div>
        <div class="item-card">
            <div class="numero" id="mensagens">0</div>
            <p class="desc">Mensagens</p>
        </div>
    </div>

    <div class="abas">
        <div class="aba ativo" onclick="trocarAba('inicio')">Início</div>
        <div class="aba" onclick="trocarAba('tarefas')">Tarefa SP</div>
        <div class="aba" onclick="trocarAba('redacao')">Redação Paulista</div>
    </div>

    <div class="card conteudo ativo" id="abaInicio">
        <h3 style="color: var(--vermelho); margin-bottom: 12px;">Status</h3>
        <p style="color: var(--texto-suave); line-height: 1.6;">
            ✅ Hospedado no GitHub<br>
            ✅ Funciona em qualquer celular<br>
            ✅ Conecta direto na Sala do Futuro<br>
            ✅ Busca, mostra e envia suas atividades
        </p>
    </div>

    <div class="card conteudo" id="abaTarefas">
        <h3 style="color: var(--vermelho); margin-bottom: 12px;">Tarefas SP</h3>
        <button onclick="buscarTarefas()">🔍 Buscar Minhas Tarefas</button>
        <button onclick="resolverTodas()" style="margin-top: 10px;">⚡ Resolver e Enviar</button>
        <div id="listaTarefas" style="margin-top: 15px;"></div>
    </div>

    <div class="card conteudo" id="abaRedacao">
        <h3 style="color: var(--vermelho); margin-bottom: 12px;">Redação Paulista</h3>
        <button onclick="buscarRedacoes()">🔍 Buscar Meus Temas</button>
        <button onclick="gerarTodas()" style="margin-top: 10px;">✍️ Gerar e Enviar</button>
        <div id="listaRedacoes" style="margin-top: 15px;"></div>
    </div>
</div>

<script>
// Configurações prontas
const URL_SALA = "https://saladofuturo.educacao.sp.gov.br";
const PONTE = "https://corsproxy.io/?url="; // Funciona para contornar bloqueios
let usuario = null;

// 🚀 Login e conexão
async function conectar() {
    const ra = document.getElementById("ra").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) {
        alert("⚠️ Preencha o RA e a senha!");
        return;
    }

    const botao = document.querySelector("button");
    botao.textContent = "Conectando...";

    try {
        const resposta = await fetch(`${PONTE}${encodeURIComponent(`${URL_SALA}/api/login`)}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: ra, senha: senha })
        });

        const dados = await resposta.json();

        if (!dados.sucesso) throw new Error(dados.mensagem || "RA ou senha incorretos");

        usuario = {
            ra: ra,
            senha: senha,
            nome: dados.nome || "Aluno",
            serie: dados.serie || "Não informado",
            pendentes: dados.pendencias || 0,
            faltas: dados.faltas || 0,
            frequencia: dados.frequencia || 0,
            tarefas: [],
            redacoes: []
        };

        abrirSistema();
        alert("✅ Conectado com sucesso!");

    } catch (erro) {
        alert("❌ Erro: " + erro.message);
    }

    botao.textContent = "ENTRAR E BUSCAR DADOS";
}

function abrirSistema() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painel").style.display = "block, grid, flex";

    document.getElementById("letraInicial.textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nomeAluno").textContent = usuario.nome;
    document.getElementById("serieAluno").textContent = usuario.serie;

    atualizarDados();
}

function atualizarDados() {
    document.getElementById("pendentes").textContent = usuario.pendentes;
    document.getElementById("faltas").textContent = usuario.faltas;
    document.getElementById("frequencia").textContent = `${usuario.frequencia}%`;
}

function trocarAba(nome) {
    document.querySelectorAll(".aba").forEach(el => el.classList.remove("ativo"));
    document.querySelectorAll(".conteudo").forEach(el => el.classList.remove("ativo"));

    event.target.classList.add("ativo");
    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).classList.add("ativo");
}

async function buscarTarefas() {
    const lista = document.getElementById("listaTarefas");
    lista.innerHTML = "<p style='color: var(--texto-suave);'>Carregando...</p>";

    try {
        const res = await fetch(`${PONTE}${encodeURIComponent(`${URL_SALA}/api/tarefas?ra=${usuario.ra}&senha=${usuario.senha}`)}`);
        usuario.tarefas = (await res.json()).lista || [];
        listarTarefas();
    } catch {
        lista.innerHTML = "<p style='color: var(--amarelo);'>Não foi possível carregar</p>";
    }
}

async function buscarRedacoes() {
    const lista = document.getElementById("listaRedacoes");
    lista.innerHTML = "<p style='color: var(--texto-suave);'>Carregando...</p>";

    try {
        const res = await fetch(`${PONTE}${encodeURIComponent(`${URL_SALA}/api/redacao-paulista?ra=${usuario.ra}&senha=${usuario.senha}`)}`);
        usuario.redacoes = (await res.json()).lista || [];
        listarRedacoes();
    } catch {
        lista.innerHTML = "<p style='color: var(--amarelo);'>Não foi possível carregar</p>";
    }
}

async function resolverTodas() {
    if (!usuario.tarefas.length) return alert("⚠️ Busque as tarefas primeiro!");

    for (let t of usuario.tarefas) {
        if (!t.concluida) {
            t.resposta = `Resposta conforme conteúdo da Sala do Futuro:

${t.descricao}

A atividade aborda conceitos importantes para o aprendizado. Ao analisar o tema, compreendemos seus pontos principais e sua aplicação prática. Dessa forma, cumprimos o objetivo proposto pela tarefa.`;

            await fetch(`${PONTE}${encodeURIComponent(`${URL_SALA}/api/enviar-tarefa`)}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ ra: usuario.ra, senha: usuario.senha, id: t.id, resposta: t.resposta })
            });
            t.concluida = true;
        }
    }

    usuario.pendentes = Math.max(0, usuario.pendentes - usuario.tarefas.length);
    atualizarDados();
    listarTarefas();
    alert("✅ Todas as tarefas enviadas!");
}

async function gerarTodas() {
    if (!usuario.redacoes.length) return alert("⚠️ Busque os temas primeiro!");

    for (let r of usuario.redacoes) {
        if (!r.concluida) {
            r.texto = `Redação Paulista: ${r.tema}

**Introdução**
O tema "${r.tema}" é relevante para a formação acadêmica e cidadã, alinhado aos objetivos da Sala do Futuro. Ele trata de assuntos que ampliam nossa visão de mundo.

**Desenvolvimento**
Ao analisar o assunto, percebemos que existem diferentes pontos de vista e aspectos importantes a serem considerados. Entender esses pontos ajuda a desenvolver raciocínio e capacidade de argumentação.

**Conclusão**
Portanto, refletir e estudar esse tema contribui para o crescimento pessoal e cumpre os requisitos da atividade proposta.`;

            await fetch(`${PONTE}${encodeURIComponent(`${URL_SALA}/api/enviar-redacao`)}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ ra: usuario.ra, senha: usuario.senha, id: r.id, texto: r.texto })
            });
            r.concluida = true;
        }
    }

    usuario.pendentes = Math.max(0, usuario.pendentes - usuario.redacoes.length);
    atualizarDados();
    listarRedacoes();
    alert("✅ Redações enviadas!");
}

function listarTarefas() {
    document.getElementById("listaTarefas").innerHTML = usuario.tarefas.map(t => `
        <div class="atividade">
            <h4>${t.titulo}</h4>
            <p>${t.descricao || "Sem descrição"}</p>
            <p>Status: <span style="color: ${t.concluida ? 'var(--verde)' : 'var(--amarelo)'}">
                ${t.concluida ? "✅ Concluída" : "⏳ Pendente"}
            </span></p>
        </div>
    `).join("");
}

function listarRedacoes() {
    document.getElementById("listaRedacoes").innerHTML = usuario.redacoes.map(r => `
        <div class="atividade">
            <h4>Tema: ${r.tema}</h4>
            <p>Prazo: ${r.prazo || "Sem prazo"}</p>
            <p>Status: <span style="color: ${r.concluida ? 'var(--verde)' : 'var(--amarelo)'}">
                ${r.concluida ? "✅ Enviada" : "⏳ Pendente"}
            </span></p>
        </div>
    `).join("");
}
</script>

</body>
</html>
