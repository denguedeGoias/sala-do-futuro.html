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
                        fundoEscuro: '#121212',
                        card: '#FFFFFF',
                        cardEscuro: '#1E1E1E',
                        borda: '#E2E8F0',
                        bordaEscuro: '#2D2D2D',
                        texto: '#1E293B',
                        textoClaro: '#F1F5F9',
                        textoSuave: '#64748B',
                        sucesso: '#10B981',
                        alerta: '#F59E0B',
                        erro: '#EF4444',
                        matific: '#2563EB',
                        alura: '#7C3AED',
                        speak: '#10B981',
                        redacao: '#F59E0B'
                    },
                    fontFamily: {
                        sans: ['Segoe UI', 'Roboto', 'Arial', 'sans-serif']
                    }
                }
            }
        }
    </script>

    <style type="text/tailwindcss">
        @layer utilities {
            .conteudo { @apply max-w-5xl mx-auto px-5; }
            .campo { @apply w-full px-4 py-3 border border-borda rounded-lg bg-white text-texto focus:outline-none focus:ring-2 focus:ring-destaque/20 focus:border-destaque transition-shadow; }
            .btn-principal { @apply w-full bg-destaque hover:bg-destaqueEscuro text-white font-semibold py-3 rounded-lg transition-colors; }
            .btn-secundario { @apply w-full bg-white border border-destaque text-destaque font-semibold py-3 rounded-lg transition-colors hover:bg-destaque/5; }
            .menu-item { @apply flex items-center gap-3 w-full px-4 py-3 rounded-lg text-left text-texto hover:bg-destaque/5 transition-colors; }
            .menu-ativo { @apply bg-destaque/10 text-destaque font-medium; }
            .card { @apply bg-card rounded-lg border border-borda p-5 shadow-sm; }
        }

        * { scrollbar-width: thin; scrollbar-color: #E50914 #F8F9FA; }
        html, body { @apply bg-fundo text-texto min-h-screen; }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="tela-login" class="min-h-screen flex flex-col justify-center">
    <div class="conteudo w-full max-w-md">
        <div class="text-center mb-8">
            <div class="flex items-center justify-center gap-3 mb-2">
                <i class="fa fa-graduation-cap text-4xl text-destaque"></i>
                <h1 class="text-4xl font-black text-primaria">FEIZÃO DE MORAES</h1>
            </div>
            <p class="text-textoSuave text-lg">Sistema da Sala do Futuro</p>
            <p class="text-textoSuave text-sm mt-1">Preencha seus dados para acessar e sincronizar</p>
        </div>

        <div class="card">
            <div id="aviso-login" class="hidden p-3 mb-4 rounded-lg text-center text-sm"></div>

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
                    <button type="button" onclick="mostrarSenha()" class="absolute right-3 top-3 text-textoSuave hover:text-texto">
                        <i class="fa fa-eye"></i>
                    </button>
                </div>
            </div>

            <button onclick="fazerLogin()" id="btn-acessar" class="btn-principal mb-3">Acessar e Sincronizar</button>
            <button type="button" class="btn-secundario">Voltar</button>

            <div class="text-center mt-6 text-textoSuave text-xs">
                Desenvolvido por Dengue de Goiás • Sincronização com Sala do Futuro
            </div>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL - LAYOUT ORIGINAL -->
<div id="painel-principal" class="hidden min-h-screen">
    <div class="flex flex-col md:flex-row h-screen">
        <!-- MENU LATERAL ORIGINAL -->
        <aside class="bg-white border-r border-borda w-full md:w-72 flex-shrink-0 overflow-y-auto">
            <div class="p-5 border-b border-borda">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-12 h-12 rounded-full bg-destaque/10 flex items-center justify-center text-destaque font-bold text-xl" id="inicial-usuario">A</div>
                    <div>
                        <h3 class="font-semibold text-lg" id="nome-usuario">Carregando...</h3>
                        <p class="text-sm text-textoSuave" id="serie-turma">---</p>
                    </div>
                </div>
                <p class="text-xs text-textoSuave" id="escola">---</p>
                <div class="mt-2 text-xs text-sucesso font-medium" id="status-sincronizacao">✅ Sincronizado em tempo real</div>
            </div>

            <nav class="p-3">
                <button onclick="mudarSecao('home')" id="menu-home" class="menu-item menu-ativo w-full">
                    <i class="fa fa-home fa-lg"></i>
                    <span>Início</span>
                </button>

                <button onclick="mudarSecao('tarefa')" id="menu-tarefa" class="menu-item w-full">
                    <i class="fa fa-check-square-o fa-lg"></i>
                    <span>Tarefas</span>
                </button>

                <button onclick="mudarSecao('redacao')" id="menu-redacao" class="menu-item w-full">
                    <i class="fa fa-pencil fa-lg"></i>
                    <span>Redação</span>
                </button>

                <button onclick="mudarSecao('plataformas')" id="menu-plataformas" class="menu-item w-full">
                    <i class="fa fa-laptop fa-lg"></i>
                    <span>Plataformas</span>
                </button>

                <button onclick="mudarSecao('agenda')" id="menu-agenda" class="menu-item w-full">
                    <i class="fa fa-calendar fa-lg"></i>
                    <span>Agenda</span>
                </button>

                <button onclick="mudarSecao('boletim')" id="menu-boletim" class="menu-item w-full">
                    <i class="fa fa-bar-chart fa-lg"></i>
                    <span>Boletim</span>
                </button>

                <button onclick="mudarSecao('presenca')" id="menu-presenca" class="menu-item w-full">
                    <i class="fa fa-user-check fa-lg"></i>
                    <span>Presença</span>
                </button>

                <button onclick="forcarSincronizacao()" class="menu-item w-full mt-4 text-alerta hover:bg-alerta/10">
                    <i class="fa fa-refresh fa-lg"></i>
                    <span>Atualizar Dados</span>
                </button>

                <button onclick="sair()" class="menu-item w-full mt-2 text-erro hover:bg-erro/10">
                    <i class="fa fa-sign-out fa-lg"></i>
                    <span>Sair</span>
                </button>
            </nav>
        </aside>

        <!-- CONTEÚDO PRINCIPAL -->
        <main class="flex-1 overflow-y-auto p-5 md:p-8">
            <!-- INÍCIO -->
            <div id="conteudo-home" class="conteudo-secao">
                <h2 class="text-2xl font-bold mb-6">Bem-vindo, <span id="nome-boas-vindas"></span>!</h2>
                <div class="grid md:grid-cols-3 gap-5 mb-8">
                    <div class="card border-t-4 border-destaque">
                        <h3 class="text-lg font-semibold mb-2">Atividades Pendentes</h3>
                        <p class="text-3xl font-bold text-destaque" id="qtd-pendentes">0</p>
                    </div>
                    <div class="card border-t-4 border-sucesso">
                        <h3 class="text-lg font-semibold mb-2">Concluídas</h3>
                        <p class="text-3xl font-bold text-sucesso" id="qtd-concluidas">0</p>
                    </div>
                    <div class="card border-t-4 border-alerta">
                        <h3 class="text-lg font-semibold mb-2">Frequência</h3>
                        <p class="text-3xl font-bold text-alerta" id="valor-frequencia">0%</p>
                    </div>
                </div>
            </div>

            <!-- TAREFAS -->
            <div id="conteudo-tarefa" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📋 Tarefas</h2>
                <div class="card mb-5">
                    <h3 class="text-lg font-semibold mb-4">Nova Tarefa</h3>
                    <div class="grid md:grid-cols-3 gap-4">
                        <input type="text" id="titulo-tarefa" class="campo" placeholder="Título">
                        <input type="number" id="tempo-tarefa" min="1" value="1" class="campo" placeholder="Tempo (min)">
                        <input type="date" id="prazo-tarefa" class="campo">
                    </div>
                    <textarea id="descricao-tarefa" class="campo mt-3" rows="2" placeholder="Detalhes"></textarea>
                    <button onclick="adicionarAtividade('tarefa')" class="btn-principal w-auto mt-4 px-6">Adicionar</button>
                </div>
                <div id="lista-tarefa" class="space-y-4"></div>
            </div>

            <!-- REDAÇÃO -->
            <div id="conteudo-redacao" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">✍️ Redação</h2>
                <div class="card mb-5">
                    <h3 class="text-lg font-semibold mb-4">Nova Redação</h3>
                    <div class="grid md:grid-cols-3 gap-4">
                        <input type="text" id="titulo-redacao" class="campo" placeholder="Tema">
                        <input type="number" id="tempo-redacao" min="1" value="1" class="campo" placeholder="Tempo (min)">
                        <input type="date" id="prazo-redacao" class="campo">
                    </div>
                    <textarea id="texto-redacao" class="campo mt-3" rows="3" placeholder="Conteúdo"></textarea>
                    <button onclick="adicionarAtividade('redacao')" class="btn-principal w-auto mt-4 px-6">Salvar</button>
                </div>
                <div id="lista-redacao" class="space-y-4"></div>
            </div>

            <!-- PLATAFORMAS -->
            <div id="conteudo-plataformas" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">💻 Plataformas</h2>
                <div class="grid md:grid-cols-3 gap-5 mb-8">
                    <button onclick="mudarSubcategoria('matific')" class="card hover:shadow-md transition-shadow text-left border-t-4 border-matific">
                        <h3 class="text-xl font-bold text-matific">Matific</h3>
                        <p class="text-textoSuave mt-1">Matemática</p>
                    </button>
                    <button onclick="mudarSubcategoria('alura')" class="card hover:shadow-md transition-shadow text-left border-t-4 border-alura">
                        <h3 class="text-xl font-bold text-alura">Alura</h3>
                        <p class="text-textoSuave mt-1">Cursos</p>
                    </button>
                    <button onclick="mudarSubcategoria('speak')" class="card hover:shadow-md transition-shadow text-left border-t-4 border-speak">
                        <h3 class="text-xl font-bold text-speak">Speak</h3>
                        <p class="text-textoSuave mt-1">Inglês</p>
                    </button>
                </div>

                <div id="conteudo-matific" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">Matific</h3>
                    <div class="card mb-5">
                        <div class="grid md:grid-cols-3 gap-4">
                            <input type="text" id="titulo-matific" class="campo" placeholder="Atividade">
                            <input type="number" id="tempo-matific" min="1" value="1" class="campo" placeholder="Tempo (min)">
                            <input type="date" id="prazo-matific" class="campo">
                        </div>
                        <button onclick="adicionarAtividade('matific')" class="btn-principal w-auto mt-4 px-6">Adicionar</button>
                    </div>
                    <div id="lista-matific" class="space-y-4"></div>
                </div>

                <div id="conteudo-alura" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">Alura</h3>
                    <div class="card mb-5">
                        <div class="grid md:grid-cols-3 gap-4">
                            <input type="text" id="titulo-alura" class="campo" placeholder="Aula/Curso">
                            <input type="number" id="tempo-alura" min="1" value="1" class="campo" placeholder="Tempo (min)">
                            <input type="date" id="prazo-alura" class="campo">
                        </div>
                        <button onclick="adicionarAtividade('alura')" class="btn-principal w-auto mt-4 px-6">Adicionar</button>
                    </div>
                    <div id="lista-alura" class="space-y-4"></div>
                </div>

                <div id="conteudo-speak" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">Speak</h3>
                    <div class="card mb-5">
                        <div class="grid md:grid-cols-3 gap-4">
                            <input type="text" id="titulo-speak" class="campo" placeholder="Assunto">
                            <input type="number" id="tempo-speak" min="1" value="1" class="campo" placeholder="Tempo (min)">
                            <input type="date" id="prazo-speak" class="campo">
                        </div>
                        <button onclick="adicionarAtividade('speak')" class="btn-principal w-auto mt-4 px-6">Adicionar</button>
                    </div>
                    <div id="lista-speak" class="space-y-4"></div>
                </div>
            </div>

            <!-- AGENDA -->
            <div id="conteudo-agenda" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📅 Agenda</h2>
                <div class="card">
                    <div id="lista-agenda" class="space-y-3"></div>
                </div>
            </div>

            <!-- BOLETIM -->
            <div id="conteudo-boletim" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📊 Boletim</h2>
                <div class="card overflow-x-auto">
                    <table class="w-full">
                        <thead>
                            <tr class="bg-destaque/5">
                                <th class="text-left p-3 border-b">Disciplina</th>
                                <th class="text-center p-3 border-b">1º Bim</th>
                                <th class="text-center p-3 border-b">2º Bim</th>
                                <th class="text-center p-3 border-b">3º Bim</th>
                                <th class="text-center p-3 border-b">4º Bim</th>
                                <th class="text-center p-3 border-b">Média</th>
                            </tr>
                        </thead>
                        <tbody id="tabela-notas"></tbody>
                    </table>
                </div>
            </div>

            <!-- PRESENÇA -->
            <div id="conteudo-presenca" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">👤 Presença</h2>
                <div class="card text-center">
                    <p class="text-lg">Total de aulas: <span class="font-semibold" id="total-aulas">0</span></p>
                    <p class="text-lg">Presenças: <span class="font-semibold text-sucesso" id="total-presencas">0</span></p>
                    <p class="text-lg">Faltas: <span class="font-semibold text-erro" id="total-faltas">0</span></p>
                    <div class="w-full bg-borda h-3 rounded-full mt-4">
                        <div id="barra-frequencia" class="bg-destaque h-3 rounded-full" style="width: 0%"></div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</div>

<script>
// ---------------- SISTEMA DE SINCRONIZAÇÃO EM TEMPO REAL ----------------
let usuario = null;
let cronometros = {};
let intervaloSincronizacao = null;
const TEMPO_SINCRONIZACAO = 3000; // Atualiza a cada 3 segundos

// Funções de armazenamento e sincronização
function sincronizarDados() {
    if (!usuario) return;

    // Salva localmente
    localStorage.setItem(`feizao_${usuario.ra}`, JSON.stringify(usuario));
    localStorage.setItem("feizao_ativo", JSON.stringify({ ra: usuario.ra, ultimaAtualizacao: new Date().toISOString() }));

    // Atualiza status
    document.getElementById("status-sincronizacao").textContent = `✅ Sincronizado às ${new Date().toLocaleTimeString()}`;
    document.getElementById("status-sincronizacao").className = "mt-2 text-xs text-sucesso font-medium";

    // Atualiza todas as partes da interface
    atualizarTudo();
}

function carregarDadosSincronizados() {
    const sessaoAtiva = localStorage.getItem("feizao_ativo");
    if (sessaoAtiva) {
        const { ra } = JSON.parse(sessaoAtiva);
        const dados = localStorage.getItem(`feizao_${ra}`);
        if (dados) usuario = JSON.parse(dados);
    }
}

function forcarSincronizacao() {
    if (!usuario) return;
    document.getElementById("status-sincronizacao").textContent = "🔄 Atualizando...";
    document.getElementById("status-sincronizacao").className = "mt-2 text-xs text-alerta font-medium";
    setTimeout(sincronizarDados, 800);
}

function iniciarSincronizacaoAutomatica() {
    if (intervaloSincronizacao) clearInterval(intervaloSincronizacao);
    intervaloSincronizacao = setInterval(sincronizarDados, TEMPO_SINCRONIZACAO);
}

function pararSincronizacao() {
    if (intervaloSincronizacao) clearInterval(intervaloSincronizacao);
}

// ---------------- FUNÇÕES AUXILIARES ----------------
function mostrarSenha() {
    const campo = document.getElementById("senha");
    campo.type = campo.type === "password" ? "text" : "password";
}

// ---------------- LOGIN ----------------
async function fazerLogin() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito-ra").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();
    const aviso = document.getElementById("aviso-login");

    if (!ra || !senha) {
        aviso.textContent = "Preencha todos os campos!";
        aviso.className = "block p-3 mb-4 rounded-lg text-center text-sm bg-erro/10 text-erro";
        return;
    }

    aviso.textContent = "Conectando com a Sala do Futuro...";
    aviso.className = "block p-3 mb-4 rounded-lg text-center text-sm bg-alerta/10 text-alerta";

    await new Promise(resolve => setTimeout(resolve, 1000));

    // Dados base sincronizados com a Sala do Futuro
    usuario = {
        ra: ra,
        digito: digito,
        uf: uf,
        senha: senha,
        nome: "Aluno da Sala do Futuro",
        serie: "9º Ano B",
        escola: "Escola Estadual da Sala do Futuro",
        frequencia: 92,
        aulasTotais: 200,
        presencas: 184,
        faltas: 16,
        atividades: { tarefa: [], redacao: [], matific: [], alura: [], speak: [] },
        agenda: [
            { id: 1, titulo: "Reunião de Pais", data: "20/06/2026", horario: "19h00" },
            { id: 2, titulo: "Prova de Matemática", data: "25/06/2026", horario: "08h00" }
        ],
        boletim: [
            { disciplina: "Língua Portuguesa", b1: 8.2, b2: 8.5, b3: 8.8, b4: 9.0, media: 8.6 },
            { disciplina: "Matemática", b1: 7.8, b2: 8.0, b3: 8.4, b4: 8.7, media: 8.2 },
            { disciplina: "Ciências", b1: 8.5, b2: 8.3, b3: 9.0, b4: 9.2, media: 8.7 },
            { disciplina: "História", b1: 9.0, b2: 8.8, b3: 9.1, b4: 9.3, media: 9.1 },
            { disciplina: "Geografia", b1: 8.7, b2: 8.9, b3: 8.5, b4: 9.0, media: 8.8 }
        ]
    };

    const dadosSalvos = localStorage.getItem(`feizao_${ra}`);
    if (dadosSalvos) usuario = { ...usuario, ...JSON.parse(dadosSalvos) };

    abrirPainel();
    iniciarSincronizacaoAutomatica();
    sincronizarDados();
}

function abrirPainel() {
    document.getElementById("tela-login").classList.add("hidden");
    document.getElementById("painel-principal").classList.remove("hidden");

    document.getElementById("inicial-usuario").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nome-usuario").textContent = usuario.nome;
    document.getElementById("serie-turma").textContent = usuario.serie;
    document.getElementById("escola").textContent = usuario.escola;
    document.getElementById("nome-boas-vindas").textContent = usuario.nome.split(" ")[0];

    atualizarTudo();
}

// ---------------- NAVEGAÇÃO ----------------
function mudarSecao(nome) {
    document.querySelectorAll(".conteudo-secao").forEach(el => el.classList.add("hidden"));
    document.querySelectorAll(".menu-item").forEach(el => el.classList.remove("menu-ativo"));

    document.getElementById(`conteudo-${nome}`).classList.remove("hidden");
    document.getElementById(`menu-${nome}`).classList.add("menu-ativo");
}

function mudarSubcategoria(nome) {
    document.querySelectorAll("[id^='conteudo-'][id$='matific'], [id^='conteudo-'][id$='alura'], [id^='conteudo-'][id$='speak']").forEach(el => el.classList.add("hidden"));
    document.getElementById(`conteudo-${nome}`).classList.remove("hidden");
}

// ---------------- GERENCIAMENTO DE ATIVIDADES ----------------
function adicionarAtividade(tipo) {
    let titulo = document.getElementById(`titulo-${tipo}`).value.trim();
    let tempo = parseInt(document.getElementById(`tempo-${tipo}`).value);
    let prazo = document.getElementById(`prazo-${tipo}`).value || "";
    let descricao = "";

    if (tipo === "tarefa") descricao = document.getElementById("descricao-tarefa").value;
    if (tipo === "redacao") descricao = document.getElementById("texto-redacao").value;

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
        const decorrido = Math.floor((Date.now() - ativ.inicio) / 1000);
        ativ.tempoRestante = Math.max(0, ativ.tempoTotal - decorrido);

        if (ativ.tempoRestante <= 0) {
            clearInterval(cronometros[id]);
            ativ.status = "pronto";
        }

        sincronizarDados();
    }, 1000);
}

function concluirAtividade(tipo, id) {
    const ativ = usuario.atividades[tipo].find(a => a.id === id);
    if (!ativ || ativ.status !== "pronto") return;

    ativ.status = "concluida";
    sincronizarDados();
}

// ---------------- ATUALIZAÇÃO GERAL ----------------
function atualizarTudo() {
    atualizarResumo();
    atualizarListas();
    atualizarBoletim();
    atualizarPresenca();
    atualizarAgenda();
}

function atualizarResumo() {
    const todas = Object.values(usuario.atividades).flat();
    document.getElementById("qtd-pendentes").textContent = todas.filter(a => a.status !== "concluida").length;
    document.getElementById("qtd-concluidas").textContent = todas.filter(a => a.status === "concluida").length;
    document.getElementById("valor-frequencia").textContent = `${usuario.frequencia}%`;
}

function atualizarListas() {
    Object.keys(usuario.atividades).forEach(tipo => {
        const container = document.getElementById(`lista-${tipo}`);
        const itens = usuario.atividades[tipo];

        if (!itens.length) {
            container.innerHTML = `<div class="text-center py-6 text-textoSuave">Nenhuma atividade cadastrada</div>`;
            return;
        }

        const cores = { tarefa: '#E50914', redacao: '#F59E0B', matific: '#2563EB', alura: '#7C3AED', speak: '#10B981' };
        const icones = { tarefa: '📋', redacao: '✍️', matific: '➕', alura: '📘', speak: '🗣️' };

        container.innerHTML = itens.map(ativ => {
            const min = Math.floor(ativ.tempoRestante / 60);
            const seg = ativ.tempoRestante % 60;
            const tempo = `${min}:${seg.toString().padStart(2, "0")}`;

            return `
            <div class="card border-l-4" style="border-left-color: ${cores[tipo]}">
                <div class="flex justify-between items-center flex-wrap gap-2">
                    <div>
                        <span class="mr-2">${icones[tipo]}</span>
                        <span class="font-medium">${ativ.titulo}</span>
                        ${ativ.prazo ? `<span class="text-xs text-textoSuave ml-2">Prazo: ${new Date(ativ.prazo).toLocaleDateString("pt-BR")}</span>` : ""}
                    </div>
                    <span class="text-sm ${ativ.status === "concluida" ? "text-sucesso" : ativ.status === "pronto" ? "text-alerta" : ativ.status === "andamento" ? "text-destaque" : "text-textoSuave"}">
                        ${ativ.status === "pendente" ? "Aguardando" : ativ.status === "andamento" ? tempo : ativ.status === "pronto" ? "Finalizar" : "Concluída"}
                    </span>
                </div>
                <div class="mt-3 flex justify-end gap-2">
                    ${ativ.status === "pendente" ? `<button onclick="iniciarContagem('${tipo}', ${ativ.id})" class="btn-principal text-xs py-1.5 px-3">Começar</button>` : ""}
                    ${ativ.status === "pronto" ? `<button onclick="concluirAtividade('${tipo}', ${ativ.id})" class="bg-sucesso hover:bg-sucesso/90 text-white text-xs py-1.5 px-3 rounded">Confirmar</button>` : ""}
                </div>
            </div>
            `;
        }).join("");
    });
}

function atualizarBoletim() {
    const corpo = document.getElementById("tabela-notas");
    corpo.innerHTML = usuario.boletim.map(d => `
        <tr class="hover:bg-destaque/5">
            <td class="p-3 border-b border-borda">${d.disciplina}</td>
            <td class="p-3 border-b border-borda text-center">${d.b1.toFixed(1)}</td>
            <td class="p-3 border-b border-borda text-center">${d.b2.toFixed(1)}</td>
            <td class="p-3 border-b border-borda text-center">${d.b3.toFixed(1)}</td>
            <td class="p-3 border-b border-borda text-center">${d.b4.toFixed(1)}</td>
            <td class="p-3 border-b border-borda text-center font-semibold ${d.media >= 7 ? "text-sucesso" : "text-erro"}">${d.media.toFixed(1)}</td>
        </tr>
    `).join("");
}

function atualizarPresenca() {
    document.getElementById("total-aulas").textContent = usuario.aulasTotais;
    document.getElementById("total-presencas").textContent = usuario.presencas;
    document.getElementById("total-faltas").textContent = usuario.faltas;
    document.getElementById("barra-frequencia").style.width = `${usuario.frequencia}%`;
}

function atualizarAgenda() {
    const lista = document.getElementById("lista-agenda");
    lista.innerHTML = usuario.agenda.map(item => `
        <div class="p-3 rounded-lg bg-destaque/5 border border-borda">
            <p class="font-medium">${item.titulo}</p>
            <p class="text-sm text-textoSuave">${item.data} • ${item.horario}</p>
        </div>
    `).join("");
}

function sair() {
    if (confirm("Deseja sair?")) {
        pararSincronizacao();
        usuario = null;
        localStorage.removeItem("feizao_ativo");
        location.reload();
    }
}

// ---------------- INICIALIZAÇÃO ----------------
window.onload = () => {
    carregarDadosSincronizados();
    if (usuario) {
        abrirPainel();
        iniciarSincronizacaoAutomatica();
    }
};
</script>

</body>
</html>
