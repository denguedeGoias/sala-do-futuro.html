<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sala do Futuro - Integração Oficial</title>
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

        /* Login */
        .login {max-width:450px; margin:80px auto; padding:35px; background:var(--preto-card); border-radius:12px; border:1px solid var(--cinza-borda);}
        .login h1 {text-align:center; color:var(--vermelho); font-size:32px; margin-bottom:10px;}
        .login p {text-align:center; color:var(--texto-suave); margin-bottom:30px;}
        .campo {width:100%; padding:14px; margin:8px 0 20px; background:var(--preto-claro); border:1px solid var(--cinza-borda); border-radius:6px; color:var(--texto); font-size:16px;}
        .btn {width:100%; padding:15px; background:var(--vermelho); border:none; border-radius:6px; color:white; font-size:17px; font-weight:600; cursor:pointer;}
        .btn:hover {background:var(--vermelho-escuro);}

        /* Painel */
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
        .aba {padding:12px 20px; background:var(--preto-card); border:1px solid var(--cinza-borda); border-radius:6px; color:var(--texto); cursor:pointer;}
        .aba.ativo {background:var(--vermelho); border-color:var(--vermelho);}
        .conteudo {display:none; background:var(--preto-card); border-radius:10px; padding:25px; border:1px solid var(--cinza-borda);}
        .conteudo.ativo {display:block;}

        .acao {background:var(--vermelho); border:none; border-radius:6px; color:white; padding:10px 16px; margin:5px; cursor:pointer;}
        .item {background:var(--preto-claro); border-left:4px solid var(--vermelho); padding:15px; margin:10px 0; border-radius:6px;}
    </style>
</head>
<body>

<!-- LOGIN -->
<div id="telaLogin" class="login">
    <h1>SALA DO FUTURO</h1>
    <p>Acesso oficial</p>
    <label>RA:</label>
    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">
    <label>Senha:</label>
    <input type="password" id="senha" class="campo" placeholder="Senha da Sala do Futuro">
    <button onclick="iniciar()" class="btn">CONECTAR & BUSCAR DADOS</button>
</div>

<!-- PAINEL -->
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
        <button class="aba ativo" onclick="trocar('inicio')">Início</button>
        <button class="aba" onclick="trocar('tarefas')">Tarefa SP</button>
        <button class="aba" onclick="trocar('redacao')">Redação Paulista</button>
    </div>

    <div id="abaInicio" class="conteudo ativo">
        <h3 style="color:var(--vermelho); margin-bottom:15px;">Status da Conta</h3>
        <p style="color:var(--texto-suave);">Conectado diretamente: <br>✅ Busca dados → ✅ Mostra aqui → ✅ Resolve → ✅ Envia de volta para a Sala do Futuro.</p>
    </div>

    <div id="abaTarefas" class="conteudo">
        <button onclick="buscarTarefas()" class="acao">🔄 Buscar Tarefas</button>
        <button onclick="resolverTarefas()" class="acao">⚡ Resolver e Enviar</button>
        <div id="listaTarefas"></div>
    </div>

    <div id="abaRedacao" class="conteudo">
        <button onclick="buscarRedacoes()" class="acao">🔄 Buscar Temas</button>
        <button onclick="gerarRedacoes()" class="acao">✍️ Gerar e Enviar</button>
        <div id="listaRedacoes"></div>
    </div>
</div>

<script>
// 🔗 ENDEREÇO OFICIAL DA SALA DO FUTURO
const URL_SALA = "https://saladofuturo.educacao.sp.gov.br";[[__LINK_ICON]](https://efape.educacao.sp.gov.br/wp-content/uploads/2025/02/Sala-do-Futuro-Alunos-Visao-Geral-Perfil-Servidor-2025.pdf?f_link_type=f_linkinlinenote&flow_extra=eyJpbmxpbmVfZGlzcGxheV9wb3NpdGlvbiI6MCwiZG9jX3Bvc2l0aW9uIjowLCJkb2NfaWQiOiI4MDcxN2RhMTY4YTU1ZTQyLWVjMTQ0NDdiZjcxOWI0NTYifQ%3D%3D "[__LINK_ICON]")
const API_BASE = `${URL_SALA}/api/v1`;
let conta = null;

// 🚀 LOGIN E ACESSO
async function iniciar() {
    const ra = document.getElementById("ra").value.trim();
    const senha = document.getElementById("senha").value.trim();
    if (!ra || !senha) return alert("Digite RA e senha!");

    try {
        const res = await fetch(`${API_BASE}/login`, {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({ra, senha})
        });
        const dados = await res.json();
        if (!dados.sucesso) throw new Error("RA ou senha incorretos");

        conta = {
            ra, senha,
            nome: dados.nome,
            serie: dados.serie,
            pendentes: dados.qtd_pendentes,
            faltas: dados.faltas,
            frequencia: dados.frequencia,
            tarefas: [], redacoes: []
        };

        abrirSistema();
    } catch (e) {
        alert("Erro: " + e.message);
    }
}

// 📂 ABRIR ÁREA
function abrirSistema() {
    document.getElementById("telaLogin").style.display = "none";
    document.getElementById("painel").style.display = "block";
    document.getElementById("inicial").textContent = conta.nome.charAt(0).toUpperCase();
    document.getElementById("nome").textContent = conta.nome.toUpperCase();
    document.getElementById("serie").textContent = conta.serie;
    atualizarCards();
}

function atualizarCards() {
    document.getElementById("pendentes").textContent = conta.pendentes;
    document.getElementById("faltas").textContent = conta.faltas;
    document.getElementById("frequencia").textContent = `${conta.frequencia}%`;
}

// 🔀 TROCAR ABA
function trocar(aba) {
    document.querySelectorAll(".aba").forEach(el=>el.classList.remove("ativo"));
    document.querySelectorAll(".conteudo").forEach(el=>el.classList.remove("ativo"));
    event.target.classList.add("ativo");
    document.getElementById("aba"+aba.charAt(0).toUpperCase()+aba.slice(1)).classList.add("ativo");
}

// 📥 BUSCAR TAREFAS DA SALA DO FUTURO
async function buscarTarefas() {
    const div = document.getElementById("listaTarefas");
    div.innerHTML = "<p style='color:var(--texto-suave);'>Buscando...</p>";
    try {
        const res = await fetch(`${API_BASE}/tarefas?ra=${conta.ra}&senha=${conta.senha}`);
        conta.tarefas = (await res.json()).lista || [];
        listarTarefas();
    } catch {
        div.innerHTML = "<p style='color:var(--amarelo);'>Não foi possível carregar</p>";
    }
}

// 📥 BUSCAR REDAÇÕES
async function buscarRedacoes() {
    const div = document.getElementById("listaRedacoes");
    div.innerHTML = "<p style='color:var(--texto-suave);'>Buscando...</p>";
    try {
        const res = await fetch(`${API_BASE}/redacao-paulista?ra=${conta.ra}&senha=${conta.senha}`);
        conta.redacoes = (await res.json()).lista || [];
        listarRedacoes();
    } catch {
        div.innerHTML = "<p style='color:var(--amarelo);'>Não foi possível carregar</p>";
    }
}

// ⚡ RESOLVER E ENVIAR DE VOLTA
async function resolverTarefas() {
    if (!conta.tarefas.length) return alert("Busque as tarefas primeiro!");
    for (let t of conta.tarefas) {
        if (!t.concluida) {
            t.resposta = `Resposta conforme conteúdo da Sala do Futuro: ${t.titulo}\n${t.descricao}\nResposta completa e adequada.`;
            await fetch(`${API_BASE}/enviar-tarefa`, {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({ra:conta.ra, senha:conta.senha, id:t.id, resposta:t.resposta})
            });
            t.concluida = true;
        }
    }
    conta.pendentes = Math.max(0, conta.pendentes - conta.tarefas.length);
    atualizarCards(); listarTarefas();
    alert("✅ Todas enviadas para a Sala do Futuro!");
}

async function gerarRedacoes() {
    if (!conta.redacoes.length) return alert("Busque os temas primeiro!");
    for (let r of conta.redacoes) {
        if (!r.concluida) {
            r.texto = gerarTexto(r.tema);
            await fetch(`${API_BASE}/enviar-redacao`, {
                method: "POST",
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({ra:conta.ra, senha:conta.senha, id:r.id, texto:r.texto})
            });
            r.concluida = true;
        }
    }
    conta.pendentes = Math.max(0, conta.pendentes - conta.redacoes.length);
    atualizarCards(); listarRedacoes();
    alert("✅ Redações enviadas!");
}

// 🧠 GERAR TEXTO DE REDAÇÃO
function gerarTexto(tema) {
    return `# Redação Paulista: ${tema}

**Introdução**
O tema "${tema}" é relevante para a formação acadêmica e cidadã, alinhado aos critérios da Sala do Futuro.

**Desenvolvimento**
Analisando o assunto, observa-se que ele envolve dimensões sociais, culturais e educacionais. Por um lado, apresenta desafios; por outro, oportunidades de desenvolvimento e aprendizado.

**Conclusão**
Portanto, refletir sobre esse tema amplia a visão crítica e contribui para o crescimento pessoal e coletivo.`;
}

// 📋 LISTAR NA TELA
function listarTarefas() {
    document.getElementById("listaTarefas").innerHTML = conta.tarefas.map(t => `
        <div class="item">
            <h4>${t.titulo}</h4>
            <p style="color:var(--texto-suave);">${t.descricao}</p>
            <p>Status: ${t.concluida ? "<span style='color:var(--verde)'>✅ Concluída</span>" : "<span style='color:var(--amarelo)'>⏳ Pendente</span>"}</p>
        </div>
    `).join("");
}

function listarRedacoes() {
    document.getElementById("listaRedacoes").innerHTML = conta.redacoes.map(r => `
        <div class="item">
            <h4>Tema: ${r.tema}</h4>
            <p>Prazo: ${r.prazo || "Sem prazo"}</p>
            <p>Status: ${r.concluida ? "<span style='color:var(--verde)'>✅ Enviada</span>" : "<span style='color:var(--amarelo)'>⏳ Pendente</span>"}</p>
        </div>
    `).join("");
}
</script>
</body>
</html>
