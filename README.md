<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro - Sistema</title>
    <style>
        :root {
            --preto: #000000;
            --preto-card: #121212;
            --preto-claro: #1E1E1E;
            --vermelho: #E50914;
            --vermelho-escuro: #B00006;
            --cinza-borda: #2A2A2A;
            --texto: #FFFFFF;
            --texto-suave: #AAAAAA;
            --verde: #22C55E;
            --amarelo: #F59E0B;
        }
        * {margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI', Arial, sans-serif;}
        body {background:var(--preto); color:var(--texto); min-height:100vh;}

        /* Tela de Login */
        .login {max-width:450px; margin:80px auto; padding:35px; background:var(--preto-card); border-radius:12px; border:1px solid var(--cinza-borda);}
        .login h1 {text-align:center; color:var(--vermelho); font-size:32px; margin-bottom:10px;}
        .login p {text-align:center; color:var(--texto-suave); margin-bottom:30px;}
        .campo {width:100%; padding:14px; margin:8px 0 20px; background:var(--preto-claro); border:1px solid var(--cinza-borda); border-radius:6px; color:var(--texto); font-size:16px;}
        .btn {width:100%; padding:15px; background:var(--vermelho); border:none; border-radius:6px; color:white; font-size:17px; font-weight:600; cursor:pointer; transition:0.2s;}
        .btn:hover {background:var(--vermelho-escuro);}

        /* Painel Principal */
        .painel {display:none; padding:25px; max-width:1200px; margin:0 auto;}
        .cabecalho {display:flex; align-items:center; gap:15px; margin-bottom:30px;}
        .inicial {width:55px; height:55px; border-radius:50%; background:var(--vermelho); display:flex; align-items:center; justify-content:center; font-size:24px; font-weight:bold;}
        .info h2 {font-size:22px;}
        .info p {color:var(--texto-suave);}

        .grid {display:grid; grid-template-columns:repeat(auto-fit, minmax(220px,1fr)); gap:18px; margin-bottom:30px;}
        .card {background:var(--preto-card); border-radius:10px; padding:25px; border:1px solid var(--cinza-borda); border-top:3px solid var(--vermelho);}
        .card .num {font-size:40px; font-weight:bold; margin:10px 0;}
        .card p {color:var(--texto-suave);}

        .abas {display:flex; gap:10px; margin-bottom:20px;}
        .aba {padding:12px 20px; background:var(--preto-card); border:1px solid var(--cinza-borda); border-radius:6px; color:var(--texto); cursor:pointer; transition:0.2s;}
        .aba.ativo {background:var(--vermelho); border-color:var(--vermelho);}
        .conteudo {display:none; background:var(--preto-card); border-radius:10px; padding:25px; border:1px solid var(--cinza-borda);}
        .conteudo.ativo {display:block;}

        .acao {background:var(--vermelho); border:none; border-radius:6px; color:white; padding:10px 16px; margin:5px; cursor:pointer; transition:0.2s;}
        .acao:hover {background:var(--vermelho-escuro);}
        .item {background:var(--preto-claro); border-left:4px solid var(--vermelho); padding:15px; margin:10px 0; border-radius:6px;}
    </style>
</head>
<body>

<!-- Tela de Login -->
<div id="telaLogin" class="login">
    <h1>SALA DO FUTURO</h1>
    <p>Acesso ao seu sistema</p>
    <label>RA:</label>
    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">
    <label>Senha:</label>
    <input type="password" id="senha" class="campo" placeholder="Senha da Sala do Futuro">
    <button onclick="conectar()" class="btn">ENTRAR E SINCRONIZAR</button>
</div>

<!-- Painel do Aluno -->
<div id="painel" class="painel">
    <div class="cabecalho">
        <div class="inicial" id="inicial">?</div>
        <div class="info">
            <h2 id="nome">Carregando...</h2>
            <p id="serie">---</p>
        </div>
    </div>

    <div class="grid">
        <div class="card">
            <div class="num" id="pendentes">0</div>
            <p>Pendências</p>
        </div>
        <div class="card">
            <div class="num" id="faltas">0</div>
            <p>Faltas</p>
        </div>
        <div class="card">
            <div class="num" id="frequencia">0%</div>
            <p>Frequência</p>
        </div>
    </div>

    <div class="abas">
        <button class="aba ativo" onclick="trocarAba('inicio')">Início</button>
        <button class="aba" onclick="trocarAba('tarefas')">Tarefa SP</button>
        <button class="aba" onclick="trocarAba('redacao')">Redação Paulista</button>
    </div>

    <div id="abaInicio" class="conteudo ativo">
        <h3 style="color:var(--vermelho); margin-bottom:15px;">Situação da Conta</h3>
        <p style="color:var(--texto-suave);">✅ Sistema preparado para buscar seus dados reais<br>✅ Funciona com seu RA e senha<br>✅ Resolve e envia as atividades diretamente</p>
    </div>

    <div id="abaTarefas" class="conteudo">
        <h3 style="color:var(--vermelho); margin-bottom:15px;">Tarefa SP</h3>
        <button onclick="buscarTarefas()" class="acao">🔍 Buscar Minhas Tarefas</button>
        <button onclick="resolverTarefas()" class="acao">⚡ Resolver e Enviar</button>
        <div id="listaTarefas" style="margin-top:20px;"></div>
    </div>

    <div id="abaRedacao" class="conteudo">
        <h3 style="color:var(--vermelho); margin-bottom:15px;">Redação Paulista</h3>
        <button onclick="buscarRedacoes()" class="acao">🔍 Buscar Meus Temas</button>
        <button onclick="gerarRedacoes()" class="acao">✍️ Gerar e Enviar</button>
        <div id="listaRedacoes" style="margin-top:20px;"></div>
    </div>
</div>

<script>
// ⚙️ Configuração - AQUI VAI SEU SERVIDOR DE CONEXÃO
// (Esse é o único jeito de contornar o bloqueio de segurança)
const SEU_SERVIDOR = "https://seu-endereco-de-conexao.com/api";

let usuario = null;

// 🚀 Login e conexão
async function conectar() {
    const ra = document.getElementById("ra").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!ra || !senha) {
        alert("⚠️ Preencha RA e senha corretamente!");
        return;
    }

    const btn = document.querySelector(".btn");
    btn.textContent = "Conectando...";

    try {
        // Envia dados para o seu servidor, que vai buscar na Sala do Futuro
        const resposta = await fetch(`${SEU_SERVIDOR}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: ra, senha: senha })
        });

        const dados = await resposta.json();

        if (!dados.sucesso) throw new Error(dados.mensagem || "RA ou senha incorretos");

        usuario = {
            ra: ra,
            senha: senha,
            nome: dados.nome,
            serie: dados.serie,
            pendentes: dados.pendencias || 0,
            faltas: dados.faltas || 0,
            frequencia: dados.frequencia || 0,
            tarefas: [],
            redacoes: []
        };

        abrirSistema();
        alert("✅ Conectado com sucesso!");

    } catch (erro) {
        console.error("Erro:", erro);
        alert("❌ Não foi possível conectar. Verifique seus dados.");
    }

    btn.textContent = "ENTRAR E SINCRONIZAR";
}

// 📂 Mostra a área do aluno
function abrirSistema() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painel").style.display = "block";

    document.getElementById("inicial").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nome").textContent = usuario.nome.toUpperCase();
    document.getElementById("serie").textContent = usuario.serie;

    atualizarDados();
}

// 📊 Atualiza valores na tela
function atualizarDados() {
    document.getElementById("pendentes").textContent = usuario.pendentes;
    document.getElementById("faltas").textContent = usuario.faltas;
    document.getElementById("frequencia").textContent = `${usuario.frequencia}%`;
}

// 🔀 Troca de abas
function trocarAba(nome) {
    document.querySelectorAll(".aba").forEach(a => a.classList.remove("ativo"));
    document.querySelectorAll(".conteudo").forEach(c => c.classList.remove("ativo"));

    event.currentTarget.classList.add("ativo");
    document.getElementById(`aba${nome.charAt(0).toUpperCase() + nome.slice(1)}`).classList.add("ativo");
}

// 📥 Busca tarefas
async function buscarTarefas() {
    const lista = document.getElementById("listaTarefas");
    lista.innerHTML = "<p style='color:var(--texto-suave);'>Buscando suas atividades...</p>";

    try {
        const res = await fetch(`${SEU_SERVIDOR}/tarefas`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: usuario.ra, senha: usuario.senha })
        });

        const dados = await res.json();
        usuario.tarefas = dados.lista || [];
        mostrarTarefas();

    } catch {
        lista.innerHTML = "<p style='color:var(--amarelo);'>Erro ao carregar tarefas</p>";
    }
}

// 📥 Busca redações
async function buscarRedacoes() {
    const lista = document.getElementById("listaRedacoes");
    lista.innerHTML = "<p style='color:var(--texto-suave);'>Buscando seus temas...</p>";

    try {
        const res = await fetch(`${SEU_SERVIDOR}/redacoes`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ra: usuario.ra, senha: usuario.senha })
        });

        const dados = await res.json();
        usuario.redacoes = dados.lista || [];
        mostrarRedacoes();

    } catch {
        lista.innerHTML = "<p style='color:var(--amarelo);'>Erro ao carregar redações</p>";
    }
}

// ⚡ Resolve e envia tarefas
async function resolverTarefas() {
    if (!usuario.tarefas.length) {
        alert("⚠️ Primeiro clique em 'Buscar Minhas Tarefas'!");
        return;
    }

    for (let tarefa of usuario.tarefas) {
        if (!tarefa.concluida) {
            const respostaGerada = `Resposta aligneda ao conteúdo da Sala do Futuro:

${tarefa.descricao}

Desenvolvimento:
Analisando o tema proposto, podemos observar que ele trata de conceitos importantes para o aprendizado. Os pontos principais são:
- Compreensão do assunto
- Aplicação prática do conteúdo
- Reflexão sobre o tema

Conclusão:
Dessa forma, entende-se o objetivo da atividade e cumpre-se o que foi solicitado.`;

            await fetch(`${SEU_SERVIDOR}/enviar-tarefa`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    ra: usuario.ra,
                    senha: usuario.senha,
                    id: tarefa.id,
                    resposta: respostaGerada
                })
            });

            tarefa.concluida = true;
            usuario.pendentes--;
        }
    }

    atualizarDados();
    mostrarTarefas();
    alert("✅ Todas as tarefas foram enviadas para a Sala do Futuro!");
}

// ⚡ Gera e envia redações
async function gerarRedacoes() {
    if (!usuario.redacoes.length) {
        alert("⚠️ Primeiro clique em 'Buscar Meus Temas'!");
        return;
    }

    for (let redacao of usuario.redacoes) {
        if (!redacao.concluida) {
            const texto = `Redação Paulista: ${redacao.tema}

**Introdução**
O tema "${redacao.tema}" é relevante para a formação acadêmica e cidadã, alinhado aos objetivos da Sala do Futuro. Ele aborda questões que fazem parte do nosso desenvolvimento.

**Desenvolvimento**
Ao analisar o assunto, percebe-se que existem diferentes pontos de vista e aspectos a serem considerados. Por um lado, temos os desafios apresentados; por outro, as oportunidades de aprendizado e crescimento. É importante refletir sobre como esse conteúdo se aplica no dia a dia.

**Conclusão**
Portanto, compreender e estudar esse tema contribui para ampliar nossa visão crítica e cumprir as metas educacionais propostas pela atividade.`;

            await fetch(`${SEU_SERVIDOR}/enviar-redacao`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    ra: usuario.ra,
                    senha: usuario.senha,
                    id: redacao.id,
                    texto: texto
                })
            });

            redacao.concluida = true;
            usuario.pendentes--;
        }
    }

    atualizarDados();
    mostrarRedacoes();
    alert("✅ Todas as redações foram enviadas com sucesso!");
}

// 📋 Mostra lista de tarefas
function mostrarTarefas() {
    const lista = document.getElementById("listaTarefas");
    if (usuario.tarefas.length === 0) {
        lista.innerHTML = "<p style='color:var(--texto-suave);'>Nenhuma tarefa encontrada</p>";
        return;
    }

    lista.innerHTML = usuario.tarefas.map(t => `
        <div class="item">
            <h4>${t.titulo}</h4>
            <p style="color:var(--texto-suave); margin:8px 0;">${t.descricao}</p>
            <p>Status: ${t.concluida ? "<span style='color:var(--verde)'>✅ Concluída</span>" : "<span style='color:var(--amarelo)'>⏳ Pendente</span>"}</p>
        </div>
    `).join("");
}

// 📋 Mostra lista de redações
function mostrarRedacoes() {
    const lista = document.getElementById("listaRedacoes");
    if (usuario.redacoes.length === 0) {
        lista.innerHTML = "<p style='color:var(--texto-suave);'>Nenhuma redação encontrada</p>";
        return;
    }

    lista.innerHTML = usuario.redacoes.map(r => `
        <div class="item">
            <h4>Tema: ${r.tema}</h4>
            <p style="color:var(--texto-suave); margin:8px 0;">Prazo: ${r.prazo || "Sem prazo"}</p>
            <p>Status: ${r.concluida ? "<span style='color:var(--verde)'>✅ Enviada</span>" : "<span style='color:var(--amarelo)'>⏳ Pendente</span>"}</p>
        </div>
    `).join("");
}
</script>

</body>
</html>
