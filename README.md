<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#000000">
    <title>Feizão de Moraes</title>
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='12' fill='%23000000'/%3E%3Ctext x='50' y='60' font-size='42' font-weight='bold' fill='%23E50914' text-anchor='middle'%3EFM%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primaria: '#000000',
                        destaque: '#E50914',
                        destaqueEscuro: '#B00006',
                        fundo: '#F8F9FA',
                        card: '#FFFFFF',
                        borda: '#E2E8F0',
                        texto: '#1E293B',
                        textoSuave: '#64748B',
                        sucesso: '#10B981',
                        alerta: '#F59E0B',
                        erro: '#EF4444'
                    },
                    fontFamily: {
                        sans: ['Segoe UI', 'Roboto', 'Arial', 'sans-serif']
                    }
                }
            }
        }
    </script>

    <style type="text/tailwindcss">
        :root {
            --cor-principal: #E50914;
            --cor-principal-escura: #B00006;
            --cor-fundo: #F8F9FA;
            --cor-card: #FFFFFF;
            --cor-borda: #E2E8F0;
            --cor-texto: #1E293B;
            --cor-texto-suave: #64748B;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scrollbar-width: thin;
            scrollbar-color: var(--cor-principal) var(--cor-fundo);
        }

        html, body {
            background-color: var(--cor-fundo);
            color: var(--cor-texto);
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
            min-height: 100vh;
            transition: all 0.3s ease;
        }

        .conteudo { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }

        .campo {
            width: 100%;
            padding: 0.75rem 1rem;
            background: var(--cor-card);
            border: 1px solid var(--cor-borda);
            border-radius: 0.5rem;
            color: var(--cor-texto);
            transition: all 0.2s ease;
        }

        .campo:focus {
            outline: none;
            border-color: var(--cor-principal);
            box-shadow: 0 0 0 2px rgba(var(--cor-principal), 0.15);
        }

        .btn-principal {
            background-color: var(--cor-principal);
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.25rem;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .btn-principal:hover {
            background-color: var(--cor-principal-escura);
        }

        .btn-secundario {
            background: transparent;
            color: var(--cor-principal);
            border: 1px solid var(--cor-principal);
            border-radius: 0.5rem;
            padding: 0.75rem 1.25rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-secundario:hover {
            background-color: rgba(var(--cor-principal), 0.08);
        }

        .menu-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100%;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            color: var(--cor-texto);
            background: transparent;
            border: none;
            text-align: left;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .menu-item:hover {
            background-color: rgba(var(--cor-principal), 0.08);
        }

        .menu-ativo {
            background-color: rgba(var(--cor-principal), 0.12);
            color: var(--cor-principal);
            font-weight: 500;
        }

        .card {
            background: var(--cor-card);
            border: 1px solid var(--cor-borda);
            border-radius: 0.75rem;
            padding: 1.25rem;
            transition: border 0.2s ease;
        }

        .card:hover {
            border-color: #CBD5E1;
        }

        .barra-lateral {
            background: var(--cor-card);
            border-right: 1px solid var(--cor-borda);
        }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="tela-login" class="min-h-screen flex flex-col justify-center">
    <div class="conteudo w-full max-w-md">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-black" style="color: var(--cor-principal)">FEIZÃO DE MORAES</h1>
            <p class="text-textoSuave mt-1">Sistema de Tarefas e Redação</p>
        </div>

        <div class="card">
            <div id="aviso-login" class="hidden mb-4 p-2.5 rounded text-center text-sm"></div>

            <div class="grid grid-cols-3 gap-3 mb-4">
                <div class="col-span-2">
                    <label class="block text-sm text-textoSuave mb-1">RA</label>
                    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">
                </div>
                <div>
                    <label class="block text-sm text-textoSuave mb-1">Dígito</label>
                    <input type="text" id="digito-ra" class="campo" placeholder="0" maxlength="1">
                </div>
            </div>

            <div class="mb-4">
                <label class="block text-sm text-textoSuave mb-1">UF</label>
                <select id="uf" class="campo">
                    <option value="SP" selected>SP</option>
                    <option value="AC">AC</option>
                    <option value="AL">AL</option>
                    <option value="AM">AM</option>
                    <option value="BA">BA</option>
                    <option value="CE">CE</option>
                    <option value="DF">DF</option>
                    <option value="ES">ES</option>
                    <option value="GO">GO</option>
                    <option value="MG">MG</option>
                    <option value="MS">MS</option>
                    <option value="MT">MT</option>
                    <option value="RJ">RJ</option>
                    <option value="RS">RS</option>
                </select>
            </div>

            <div class="mb-6">
                <label class="block text-sm text-textoSuave mb-1">Senha</label>
                <div class="relative">
                    <input type="password" id="senha" class="campo pr-10" placeholder="Senha de acesso">
                    <button type="button" onclick="alternarSenha()" class="absolute right-3 top-1/2 -translate-y-1/2 text-textoSuave hover:text-texto">
                        <i class="fa fa-eye"></i>
                    </button>
                </div>
            </div>

            <button onclick="fazerLogin()" class="btn-principal w-full mb-3">Acessar</button>

            <div class="text-center mt-5 text-textoSuave text-xs">
                Desenvolvido por Dengue de Goiás
            </div>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL -->
<div id="painel-principal" class="hidden min-h-screen flex flex-col md:flex-row">
    <!-- MENU LATERAL -->
    <aside class="w-full md:w-64 barra-lateral flex-shrink-0">
        <div class="p-4 border-b border-borda">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-lg" style="background: rgba(var(--cor-principal), 0.15); color: var(--cor-principal)" id="inicial-nome">A</div>
                <div>
                    <h3 class="font-medium" id="nome-aluno">Carregando...</h3>
                    <p class="text-xs text-textoSuave" id="dados-aluno">---</p>
                </div>
            </div>
            <div class="mt-2 text-xs text-sucesso font-medium" id="status-sincronizacao">✅ Sincronizado</div>
        </div>

        <nav class="p-3 space-y-1">
            <button onclick="mudarAba('inicio')" id="aba-inicio" class="menu-item menu-ativo">
                <i class="fa fa-home"></i>
                <span>Início</span>
            </button>
            <button onclick="mudarAba('tarefas')" id="aba-tarefas" class="menu-item">
                <i class="fa fa-check-square-o"></i>
                <span>Tarefas</span>
            </button>
            <button onclick="mudarAba('redacao')" id="aba-redacao" class="menu-item">
                <i class="fa fa-pencil"></i>
                <span>Redação Paulista</span>
            </button>
            <button onclick="abrirPersonalizacao()" class="menu-item">
                <i class="fa fa-paint-brush"></i>
                <span>Personalizar Cores</span>
            </button>
            <button onclick="forcarSincronizacao()" class="menu-item text-alerta hover:bg-alerta/10">
                <i class="fa fa-refresh"></i>
                <span>Atualizar</span>
            </button>
            <div class="h-px bg-borda my-3"></div>
            <button onclick="sair()" class="menu-item text-erro hover:bg-erro/10">
                <i class="fa fa-sign-out"></i>
                <span>Sair</span>
            </button>
        </nav>
    </aside>

    <!-- CONTEÚDO PRINCIPAL -->
    <main class="flex-1 p-4 md:p-6 overflow-auto">
        <!-- INÍCIO -->
        <div id="conteudo-inicio" class="conteudo-aba">
            <h2 class="text-xl font-semibold mb-5">Visão Geral</h2>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                <div class="card border-t-2" style="border-color: var(--cor-principal)">
                    <h3 class="text-sm text-textoSuave">Pendentes</h3>
                    <p class="text-3xl font-bold mt-1" style="color: var(--cor-principal)" id="cont-pendentes">0</p>
                </div>
                <div class="card border-t-2 border-sucesso">
                    <h3 class="text-sm text-textoSuave">Concluídas</h3>
                    <p class="text-3xl font-bold mt-1 text-sucesso" id="cont-concluidas">0</p>
                </div>
                <div class="card border-t-2 border-alerta">
                    <h3 class="text-sm text-textoSuave">Total</h3>
                    <p class="text-3xl font-bold mt-1 text-alerta" id="cont-total">0</p>
                </div>
            </div>
        </div>

        <!-- TAREFAS -->
        <div id="conteudo-tarefas" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">📋 Tarefas</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-tarefa" class="campo" placeholder="Título da tarefa">
                    <input type="number" id="tempo-tarefa" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-tarefa" class="campo">
                </div>
                <textarea id="descricao-tarefa" class="campo mb-3" rows="2" placeholder="Descrição (opcional)"></textarea>
                <button onclick="adicionar('tarefa')" class="btn-principal">Adicionar Tarefa</button>
            </div>
            <div id="lista-tarefa" class="space-y-3"></div>
        </div>

        <!-- REDAÇÃO -->
        <div id="conteudo-redacao" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">✍️ Redação Paulista</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-redacao" class="campo" placeholder="Tema da redação">
                    <input type="number" id="tempo-redacao" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-redacao" class="campo">
                </div>
                <textarea id="texto-redacao" class="campo mb-3" rows="4" placeholder="Escreva o conteúdo ou anotações"></textarea>
                <button onclick="adicionar('redacao')" class="btn-principal">Salvar Redação</button>
            </div>
            <div id="lista-redacao" class="space-y-3"></div>
        </div>

        <!-- PERSONALIZAÇÃO DE CORES -->
        <div id="conteudo-personalizar" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">🎨 Personalizar Cores</h2>
            <div class="card max-w-lg">
                <p class="text-sm text-textoSuave mb-4">Escolha as cores que deseja usar no sistema:</p>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label class="block text-sm text-textoSuave mb-1">Cor Principal</label>
                        <input type="color" id="cor-principal" value="#E50914" class="w-full h-10 cursor-pointer">
                    </div>
                    <div>
                        <label class="block text-sm text-textoSuave mb-1">Cor de Fundo</label>
                        <input type="color" id="cor-fundo" value="#F8F9FA" class="w-full h-10 cursor-pointer">
                    </div>
                </div>

                <button onclick="aplicarCores()" class="btn-principal w-full">Aplicar e Salvar</button>
                <button onclick="restaurarCores()" class="btn-secundario w-full mt-3">Restaurar Padrão</button>
            </div>
        </div>
    </main>
</div>

<script>
// ---------------- VARIÁVEIS GERAIS ----------------
let usuario = null;
let cronometros = {};
let intervaloSincronizacao = null;
const TEMPO_SINCRONIZACAO = 2500; // A cada 2,5 segundos

// ---------------- SINCRONIZAÇÃO ----------------
function sincronizarDados() {
    if (!usuario) return;
    localStorage.setItem(`feizao_${usuario.ra}`, JSON.stringify(usuario));
    localStorage.setItem("feizao_sessao", JSON.stringify({ ra: usuario.ra, ultima: new Date().toISOString() }));
    document.getElementById("status-sincronizacao").textContent = `✅ Sincronizado ${new Date().toLocaleTimeString()}`;
    atualizarTela();
}

function forcarSincronizacao() {
    document.getElementById("status-sincronizacao").textContent = "🔄 Atualizando...";
    setTimeout(sincronizarDados, 600);
}

function iniciarSincronizacao() {
    if (intervaloSincronizacao) clearInterval(intervaloSincronizacao);
    intervaloSincronizacao = setInterval(sincronizarDados, TEMPO_SINCRONIZACAO);
}

function pararSincronizacao() {
    if (intervaloSincronizacao) clearInterval(intervaloSincronizacao);
}

// ---------------- PERSONALIZAÇÃO DE CORES ----------------
function aplicarCores() {
    const corP = document.getElementById("cor-principal").value;
    const corF = document.getElementById("cor-fundo").value;
    document.documentElement.style.setProperty('--cor-principal', corP);
    document.documentElement.style.setProperty('--cor-principal-escura', escurecerCor(corP, 20));
    document.documentElement.style.setProperty('--cor-fundo', corF);
    if (usuario) {
        usuario.config = usuario.config || {};
        usuario.config.cores = { principal: corP, fundo: corF };
        sincronizarDados();
    }
}

function restaurarCores() {
    document.getElementById("cor-principal").value = "#E50914";
    document.getElementById("cor-fundo").value = "#F8F9FA";
    aplicarCores();
}

function escurecerCor(cor, percentual) {
    const r = parseInt(cor.slice(1,3),16);
    const g = parseInt(cor.slice(3,5),16);
    const b = parseInt(cor.slice(5,7),16);
    const novoR = Math.max(0, Math.round(r * (100 - percentual)/100)).toString(16).padStart(2,'0');
    const novoG = Math.max(0, Math.round(g * (100 - percentual)/100)).toString(16).padStart(2,'0');
    const novoB = Math.max(0, Math.round(b * (100 - percentual)/100)).toString(16).padStart(2,'0');
    return `#${novoR}${novoG}${novoB}`;
}

function carregarCoresSalvas() {
    if (!usuario || !usuario.config?.cores) return;
    const { principal, fundo } = usuario.config.cores;
    document.getElementById("cor-principal").value = principal;
    document.getElementById("cor-fundo").value = fundo;
    document.documentElement.style.setProperty('--cor-principal', principal);
    document.documentElement.style.setProperty('--cor-principal-escura', escurecerCor(principal, 20));
    document.documentElement.style.setProperty('--cor-fundo', fundo);
}

// ---------------- LOGIN ----------------
function alternarSenha() {
    const campo = document.getElementById("senha");
    campo.type = campo.type === "password" ? "text" : "password";
}

async function fazerLogin() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito-ra").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();
    const aviso = document.getElementById("aviso-login");

    if (!ra || !senha) {
        aviso.textContent = "Preencha todos os campos!";
        aviso.className = "block p-2.5 mb-4 rounded bg-erro/10 text-erro text-center text-sm";
        return;
    }

    aviso.textContent = "Conectando...";
    aviso.className = "block p-2.5 mb-4 rounded bg-alerta/10 text-alerta text-center text-sm";
    await new Promise(resolve => setTimeout(resolve, 800));

    usuario = {
        ra: ra,
        digito: digito,
        uf: uf,
        senha: senha,
        nome: "Aluno",
        serie: "8º Ano",
        atividades: { tarefa: [], redacao: [] },
        config: {}
    };

    const dadosSalvos = localStorage.getItem(`feizao_${ra}`);
    if (dadosSalvos) usuario = { ...usuario, ...JSON.parse(dadosSalvos) };

    abrirPainel();
    iniciarSincronizacao();
    carregarCoresSalvas();
    sincronizarDados();
}

function abrirPainel() {
    document.getElementById("tela-login").classList.add("hidden");
    document.getElementById("painel-principal").classList.remove("hidden");
    document.getElementById("inicial-nome").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nome-aluno").textContent = usuario.nome;
    document.getElementById("dados-aluno").textContent = usuario.serie;
}

// ---------------- NAVEGAÇÃO ----------------
function mudarAba(nome) {
    document.querySelectorAll(".conteudo-aba").forEach(el => el.classList.add("hidden"));
    document.querySelectorAll(".menu-item").forEach(el => el.classList.remove("menu-ativo"));
    document.getElementById(`conteudo-${nome}`).classList.remove("hidden");
    document.getElementById(`aba-${nome}`)?.classList.add("menu-ativo");
    if (nome === "personalizar") document.getElementById("conteudo-personalizar").classList.remove("hidden");
}

function abrirPersonalizacao() {
    mudarAba("personalizar");
}

// ---------------- GERENCIAMENTO DE TAREFAS E REDAÇÃO ----------------
function adicionar(tipo) {
    const titulo = document.getElementById(`titulo-${tipo}`).value.trim();
    const tempo = parseInt(document.getElementById(`tempo-${tipo}`).value);
    const prazo = document.getElementById(`prazo-${tipo}`).value || "";
    const descricao = tipo === "tarefa" ? document.getElementById("descricao-tarefa").value : document.getElementById("texto-redacao").value;

    if (!titulo) return alert("Digite um título!");
    if (tempo < 1) return alert("Tempo mínimo é 1 minuto!");

    const nova = {
        id: Date.now(),
        titulo,
        descricao,
        tempoTotal: tempo * 60,
        tempoRestante: tempo * 60,
        prazo,
        status: "pendente",
        inicio: null
    };

    usuario.atividades[tipo].push(nova);
    limparCampos(tipo);
    sincronizarDados();
}

function limparCampos(tipo) {
    document.getElementById(`titulo-${tipo}`).value = "";
    document.getElementById(`tempo-${tipo}`).value = "1";
    document.getElementById(`prazo-${tipo}`).value = "";
    if (tipo === "tarefa") document.getElementById("descricao-tarefa").value = "";
    if (tipo === "redacao") document.getElementById("texto-redacao").value = "";
}

function iniciarContagem(tipo, id) {
    const ativ = usuario.atividades[tipo].find(a => a.id === id);
    if (!ativ || ativ.status !== "pendente") return;
    ativ.inicio = Date.now();
    ativ.status = "andamento";
    cronometros[id] = setInterval(() => {
        const decorrido = Math.floor((Date.now() - ativ.inicio)/1000);
        ativ.tempoRestante = Math.max(0, ativ.tempoTotal - decorrido);
        if (ativ.tempoRestante <= 0) {
            clearInterval(cronometros[id]);
            ativ.status = "pronto";
        }
        sincronizarDados();
    }, 1000);
}

function concluir(tipo, id) {
    const ativ = usuario.atividades[tipo].find(a => a.id === id);
    if (!ativ || ativ.status !== "pronto") return;
    ativ.status = "concluida";
    sincronizarDados();
}

// ---------------- ATUALIZAÇÃO DE TELA ----------------
function atualizarTela() {
    const todas = [...usuario.atividades.tarefa, ...usuario.atividades.redacao];
    document.getElementById("cont-pendentes").textContent = todas.filter(a => a.status !== "concluida").length;
    document.getElementById("cont-concluidas").textContent = todas.filter(a => a.status === "concluida").length;
    document.getElementById("cont-total").textContent = todas.length;
    atualizarLista("tarefa");
    atualizarLista("redacao");
}

function atualizarLista(tipo) {
    const container = document.getElementById(`lista-${tipo}`);
    const itens = usuario.atividades[tipo];
    if (!itens.length) {
        container.innerHTML = `<div class="p-4 text-center text-textoSuave">Nenhuma ${tipo === "tarefa" ? "tarefa cadastrada" : "redação salva"}</div>`;
        return;
    }
    const icone = tipo === "tarefa" ? "📋" : "✍️";
    container.innerHTML = itens.map(ativ => {
        const min = Math.floor(ativ.tempoRestante / 60);
        const seg = ativ.tempoRestante % 60;
        const tempo = `${min}:${seg.toString().padStart(2, "0")}`;
        return `
        <div class="card border-l-4" style="border-left-color: var(--cor-principal)">
            <div class="flex justify-between items-center flex-wrap gap-2">
                <div>
                    <span class="mr-2">${icone}</span>
                    <span class="font-medium">${ativ.titulo}</span>
                    ${ativ.prazo ? `<span class="text-xs text-textoSuave ml-2">Prazo: ${new Date(ativ.prazo).toLocaleDateString("pt-BR")}</span>` : ""}
                </div>
                <span class="text-sm ${ativ.status === "concluida" ? "text-sucesso" : ativ.status === "pronto" ? "text-alerta" : ativ.status === "andamento" ? "text-destaque" : "text-textoSuave"}">
                    ${ativ.status === "pendente" ? "Aguardando" : ativ.status === "andamento" ? tempo : ativ.status === "pronto" ? "Finalizar" : "Concluída"}
                </span>
            </div>
            ${ativ.descricao ? `<p class="text-sm text-textoSuave mt-2">${ativ.descricao}</p>` : ""}
            <div class="mt-3 flex justify-end gap-2">
                ${ativ.status === "pendente" ? `<button onclick="iniciarContagem('${tipo}', ${ativ.id})" class="btn-principal text-xs py-1.5 px-3">Começar</button>` : ""}
                ${ativ.status === "pronto" ? `<button onclick="concluir('${tipo}', ${ativ.id})" class="bg-sucesso hover:bg-sucesso/90 text-white text-xs py-1.5 px-3 rounded">Confirmar</button>` : ""}
            </div>
        </div>`;
    }).join("");
}

function sair() {
    if (confirm("Deseja sair?")) {
        pararSincronizacao();
        usuario = null;
        localStorage.removeItem("feizao_sessao");
        location.reload();
    }
}

// ---------------- INICIALIZAÇÃO ----------------
window.onload = () => {
    const sessao = localStorage.getItem("feizao_sessao");
    if (sessao) {
        const { ra } = JSON.parse(sessao);
        const dados = localStorage.getItem(`feizao_${ra}`);
        if (dados) {
            usuario = JSON.parse(dados);
            abrirPainel();
            iniciarSincronizacao();
            carregarCoresSalvas();
        }
    }
};
</script>

</body>
</html>
