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
                        preto: '#000000',
                        pretoClaro: '#0F0F0F',
                        vermelho: '#E50914',
                        vermelhoEscuro: '#B00006',
                        textoClaro: '#F0F0F0',
                        textoCinza: '#A0A0A0',
                        borda: '#222222',
                        matific: '#2563eb',
                        alura: '#7c3aed',
                        speak: '#10b981',
                        redacao: '#f59e0b'
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
            .conteudo { @apply max-w-4xl mx-auto px-5; }
            .campo { @apply w-full px-4 py-3 bg-pretoClaro border border-borda rounded-lg text-textoClaro focus:outline-none focus:ring-2 focus:ring-vermelho/30 focus:border-vermelho transition-shadow; }
            .btn-principal { @apply w-full bg-vermelho hover:bg-vermelhoEscuro text-white font-semibold py-4 rounded-lg transition-colors; }
            .btn-secundario { @apply w-full bg-transparent border border-vermelho text-vermelho font-semibold py-3.5 rounded-lg transition-colors hover:bg-vermelho/10; }
            .menu-item { @apply flex items-center gap-3 w-full px-4 py-3 rounded-lg text-left text-textoClaro hover:bg-vermelho/10 transition-colors; }
            .menu-ativo { @apply bg-vermelho/20 text-vermelho font-medium; }
            .card { @apply bg-pretoClaro border border-borda rounded-xl p-5; }
        }

        * { scrollbar-width: thin; scrollbar-color: #E50914 #000000; }
        html, body { @apply bg-preto text-textoClaro min-h-screen; }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="tela-login" class="min-h-screen flex flex-col justify-center">
    <div class="conteudo w-full max-w-md">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-black text-vermelho mb-2">FEIZÃO DE MORAES</h1>
            <p class="text-textoCinza text-lg">Estudante</p>
            <p class="text-textoCinza text-sm mt-1">Preencha seus dados para acessar o sistema</p>
        </div>

        <div class="card">
            <div id="aviso-login" class="hidden p-3 mb-4 rounded-lg text-center text-sm"></div>

            <div class="grid grid-cols-3 gap-3 mb-4">
                <div class="col-span-2">
                    <label class="block text-sm text-textoCinza mb-1">RA</label>
                    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">
                </div>
                <div>
                    <label class="block text-sm text-textoCinza mb-1">Dígito</label>
                    <input type="text" id="digito-ra" class="campo" placeholder="0" maxlength="1">
                </div>
            </div>

            <div class="mb-4">
                <label class="block text-sm text-textoCinza mb-1">UF</label>
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
                    <option value="MA">MA</option>
                    <option value="MG">MG</option>
                    <option value="MS">MS</option>
                    <option value="MT">MT</option>
                    <option value="PA">PA</option>
                    <option value="PB">PB</option>
                    <option value="PE">PE</option>
                    <option value="PI">PI</option>
                    <option value="PR">PR</option>
                    <option value="RJ">RJ</option>
                    <option value="RN">RN</option>
                    <option value="RO">RO</option>
                    <option value="RR">RR</option>
                    <option value="RS">RS</option>
                    <option value="SC">SC</option>
                    <option value="SE">SE</option>
                    <option value="TO">TO</option>
                </select>
            </div>

            <div class="mb-6">
                <label class="block text-sm text-textoCinza mb-1">Senha</label>
                <div class="relative">
                    <input type="password" id="senha" class="campo pr-10" placeholder="Digite sua senha">
                    <button type="button" onclick="mostrarSenha()" class="absolute right-3 top-3 text-textoCinza hover:text-textoClaro">
                        <i class="fa fa-eye"></i>
                    </button>
                </div>
                <p class="text-right mt-2">
                    <a href="#" class="text-vermelho text-sm">Esqueceu a senha?</a>
                </p>
            </div>

            <button onclick="fazerLogin()" id="btn-acessar" class="btn-principal mb-3">Acessar</button>
            <button type="button" class="btn-secundario">Voltar</button>

            <div class="text-center mt-6 text-textoCinza text-xs">
                Desenvolvido por Dengue de Goiás
            </div>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL -->
<div id="painel-principal" class="hidden min-h-screen">
    <div class="flex flex-col md:flex-row h-screen">
        <!-- MENU LATERAL -->
        <aside id="menu-lateral" class="bg-pretoClaro border-r border-borda w-full md:w-72 flex-shrink-0 overflow-y-auto">
            <div class="p-5 border-b border-borda">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-12 h-12 rounded-full bg-vermelho/20 flex items-center justify-center text-vermelho font-bold text-xl" id="inicial-usuario">A</div>
                    <div>
                        <h3 class="font-semibold text-lg" id="nome-usuario">Carregando...</h3>
                        <p class="text-sm text-textoCinza" id="serie-turma">---</p>
                    </div>
                </div>
                <p class="text-xs text-textoCinza" id="escola">---</p>
            </div>

            <nav class="p-3">
                <button onclick="mudarSecao('home')" id="menu-home" class="menu-item menu-ativo w-full">
                    <i class="fa fa-home fa-lg"></i>
                    <span>Home</span>
                </button>

                <button onclick="mudarSecao('tarefa')" id="menu-tarefa" class="menu-item w-full">
                    <i class="fa fa-check-square-o fa-lg"></i>
                    <span>Tarefa SP</span>
                </button>

                <button onclick="mudarSecao('redacao')" id="menu-redacao" class="menu-item w-full">
                    <i class="fa fa-pencil fa-lg"></i>
                    <span>Redação Paulista</span>
                </button>

                <button onclick="mudarSecao('plataformas')" id="menu-plataformas" class="menu-item w-full">
                    <i class="fa fa-laptop fa-lg"></i>
                    <span>Plataformas de Aprendizagem</span>
                </button>

                <button onclick="mudarSecao('agenda')" id="menu-agenda" class="menu-item w-full">
                    <i class="fa fa-calendar fa-lg"></i>
                    <span>Agenda</span>
                </button>

                <button onclick="mudarSecao('boletim')" id="menu-boletim" class="menu-item w-full">
                    <i class="fa fa-bar-chart fa-lg"></i>
                    <span>Boletim e Avaliações</span>
                </button>

                <button onclick="mudarSecao('presenca')" id="menu-presenca" class="menu-item w-full">
                    <i class="fa fa-user-check fa-lg"></i>
                    <span>Presença</span>
                </button>

                <button onclick="sair()" class="menu-item w-full mt-6 text-vermelho hover:bg-vermelho/10">
                    <i class="fa fa-sign-out fa-lg"></i>
                    <span>Sair</span>
                </button>
            </nav>

            <div class="p-4 border-t border-borda mt-4 text-center text-textoCinza text-xs">
                Desenvolvido por Dengue de Goiás
            </div>
        </aside>

        <!-- CONTEÚDO PRINCIPAL -->
        <main class="flex-1 overflow-y-auto p-5 md:p-8">
            <div id="conteudo-home" class="conteudo-secao">
                <h2 class="text-2xl font-bold mb-6">Olá, <span id="nome-boas-vindas"></span>!</h2>
                <div class="grid md:grid-cols-3 gap-5 mb-8">
                    <div class="card border-t-4 border-vermelho">
                        <h3 class="text-lg font-semibold mb-2">Tarefas Pendentes</h3>
                        <p class="text-3xl font-bold text-vermelho" id="qtd-pendentes">0</p>
                    </div>
                    <div class="card border-t-4 border-green-500">
                        <h3 class="text-lg font-semibold mb-2">Concluídas</h3>
                        <p class="text-3xl font-bold text-green-500" id="qtd-concluidas">0</p>
                    </div>
                    <div class="card border-t-4 border-yellow-500">
                        <h3 class="text-lg font-semibold mb-2">Frequência</h3>
                        <p class="text-3xl font-bold text-yellow-500" id="valor-frequencia">0%</p>
                    </div>
                </div>
            </div>

            <!-- TAREFAS -->
            <div id="conteudo-tarefa" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📋 Tarefa SP</h2>
                <div class="card mb-5">
                    <h3 class="text-lg font-semibold mb-4">Nova Tarefa</h3>
                    <div class="grid md:grid-cols-3 gap-4">
                        <input type="text" id="titulo-tarefa" class="campo" placeholder="Título da tarefa">
                        <input type="number" id="tempo-tarefa" min="1" value="1" class="campo" placeholder="Tempo em minutos (mín 1)">
                        <input type="date" id="prazo-tarefa" class="campo">
                    </div>
                    <textarea id="descricao-tarefa" class="campo mt-3" rows="2" placeholder="Descrição ou observações"></textarea>
                    <button onclick="adicionarAtividade('tarefa')" class="btn-principal w-auto mt-4 px-6 py-2">Adicionar</button>
                </div>
                <div id="lista-tarefas" class="space-y-4"></div>
            </div>

            <!-- REDAÇÃO -->
            <div id="conteudo-redacao" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">✍️ Redação Paulista</h2>
                <div class="card mb-5">
                    <h3 class="text-lg font-semibold mb-4">Nova Redação</h3>
                    <div class="grid md:grid-cols-3 gap-4">
                        <input type="text" id="titulo-redacao" class="campo" placeholder="Tema da redação">
                        <input type="number" id="tempo-redacao" min="1" value="1" class="campo" placeholder="Tempo em minutos (mín 1)">
                        <input type="date" id="prazo-redacao" class="campo">
                    </div>
                    <textarea id="texto-redacao" class="campo mt-3" rows="3" placeholder="Escreva a redação ou anotações"></textarea>
                    <button onclick="adicionarAtividade('redacao')" class="btn-principal w-auto mt-4 px-6 py-2">Salvar</button>
                </div>
                <div id="lista-redacoes" class="space-y-4"></div>
            </div>

            <!-- PLATAFORMAS -->
            <div id="conteudo-plataformas" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">💻 Plataformas de Aprendizagem</h2>
                <div class="grid md:grid-cols-3 gap-5 mb-8">
                    <button onclick="mudarSubcategoria('matific')" id="sub-matific" class="card hover:shadow-md transition-shadow text-left border-t-4 border-matific">
                        <h3 class="text-xl font-bold text-matific">➕ Matific</h3>
                        <p class="text-textoCinza mt-1">Atividades de matemática</p>
                    </button>
                    <button onclick="mudarSubcategoria('alura')" id="sub-alura" class="card hover:shadow-md transition-shadow text-left border-t-4 border-alura">
                        <h3 class="text-xl font-bold text-alura">📘 Alura</h3>
                        <p class="text-textoCinza mt-1">Cursos e conteúdos</p>
                    </button>
                    <button onclick="mudarSubcategoria('speak')" id="sub-speak" class="card hover:shadow-md transition-shadow text-left border-t-4 border-speak">
                        <h3 class="text-xl font-bold text-speak">🗣️ Speak</h3>
                        <p class="text-textoCinza mt-1">Inglês e comunicação</p>
                    </button>
                </div>

                <div id="conteudo-matific" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">➕ Matific</h3>
                    <div class="card mb-5">
                        <div class="grid md:grid-cols-3 gap-4">
                            <input type="text" id="titulo-matific" class="campo" placeholder="Título da atividade">
                            <input type="number" id="tempo-matific" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                            <input type="date" id="prazo-matific" class="campo">
                        </div>
                        <button onclick="adicionarAtividade('matific')" class="btn-principal w-auto mt-4 px-6 py-2">Adicionar</button>
                    </div>
                    <div id="lista-matific" class="space-y-4"></div>
                </div>

                <div id="conteudo-alura" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">📘 Alura</h3>
                    <div class="card mb-5">
                        <div class="grid md:grid-cols-3 gap-4">
                            <input type="text" id="titulo-alura" class="campo" placeholder="Nome do curso/aula">
                            <input type="number" id="tempo-alura" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                            <input type="date" id="prazo-alura" class="campo">
                        </div>
                        <button onclick="adicionarAtividade('alura')" class="btn-principal w-auto mt-4 px-6 py-2">Adicionar</button>
                    </div>
                    <div id="lista-alura" class="space-y-4"></div>
                </div>

                <div id="conteudo-speak" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">🗣️ Speak</h3>
                    <div class="card mb-5">
                        <div class="grid md:grid-cols-3 gap-4">
                            <input type="text" id="titulo-speak" class="campo" placeholder="Assunto da aula">
                            <input type="number" id="tempo-speak" min="1" value="1" class="campo" placeholder="Tempo em minutos">
                            <input type="date" id="prazo-speak" class="campo">
                        </div>
                        <button onclick="adicionarAtividade('speak')" class="btn-principal w-auto mt-4 px-6 py-2">Adicionar</button>
                    </div>
                    <div id="lista-speak" class="space-y-4"></div>
                </div>
            </div>

            <!-- AGENDA -->
            <div id="conteudo-agenda" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📅 Agenda</h2>
                <div class="card">
                    <p class="text-textoCinza mb-4">Eventos e atividades sincronizadas</p>
                    <div id="lista-agenda" class="space-y-3">
                        <div class="p-3 bg-preto border border-borda rounded-lg">
                            <p class="font-medium">Reunião de pais</p>
                            <p class="text-sm text-textoCinza">20/06/2026 • 19h00</p>
                        </div>
                        <div class="p-3 bg-preto border border-borda rounded-lg">
                            <p class="font-medium">Prova de Matemática</p>
                            <p class="text-sm text-textoCinza">25/06/2026 • 08h00</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- BOLETIM -->
            <div id="conteudo-boletim" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📊 Boletim e Avaliações</h2>
                <div class="card overflow-x-auto">
                    <table class="w-full border-collapse">
                        <thead>
                            <tr class="bg-vermelho/10">
                                <th class="text-left p-3 border-b border-borda">Disciplina</th>
                                <th class="text-center p-3 border-b border-borda">1º Bim</th>
                                <th class="text-center p-3 border-b border-borda">2º Bim</th>
                                <th class="text-center p-3 border-b border-borda">3º Bim</th>
                                <th class="text-center p-3 border-b border-borda">4º Bim</th>
                                <th class="text-center p-3 border-b border-borda">Média</th>
                            </tr>
                        </thead>
                        <tbody id="tabela-notas">
                            <tr>
                                <td class="p-3 border-b border-borda">Língua Portuguesa</td>
                                <td class="p-3 border-b border-borda text-center">8,2</td>
                                <td class="p-3 border-b border-borda text-center">8,5</td>
                                <td class="p-3 border-b border-borda text-center">8,8</td>
                                <td class="p-3 border-b border-borda text-center">9,0</td>
                                <td class="p-3 border-b border-borda text-center font-semibold text-green-500">8,6</td>
                            </tr>
                            <tr>
                                <td class="p-3 border-b border-borda">Matemática</td>
                                <td class="p-3 border-b border-borda text-center">7,8</td>
                                <td class="p-3 border-b border-borda text-center">8,0</td>
                                <td class="p-3 border-b border-borda text-center">8,4</td>
                                <td class="p-3 border-b border-borda text-center">8,7</td>
                                <td class="p-3 border-b border-borda text-center font-semibold text-green-500">8,2</td>
                            </tr>
                            <tr>
                                <td class="p-3 border-b border-borda">Ciências</td>
                                <td class="p-3 border-b border-borda text-center">8,5</td>
                                <td class="p-3 border-b border-borda text-center">8,3</td>
                                <td class="p-3 border-b border-borda text-center">9,0</td>
                                <td class="p-3 border-b border-borda text-center">9,2</td>
                                <td class="p-3 border-b border-borda text-center font-semibold text-green-500">8,7</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- PRESENÇA -->
            <div id="conteudo-presenca" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">👤 Presença</h2>
                <div class="card text-center">
                    <p class="text-lg">Total de aulas: <span class="font-semibold">200</span></p>
                    <p class="text-lg">Presenças: <span class="font-semibold text-green-500">184</span></p>
                    <p class="text-lg">Faltas: <span class="font-semibold text-vermelho">16</span></p>
                    <div class="w-full bg-borda h-3 rounded-full mt-4">
                        <div class="bg-vermelho h-3 rounded-full" style="width: 92%"></div>
                        <p class="mt-2 text-xl font-bold text-vermelho">92%</p>
                    </div>
                </div>
            </div>
        </main>
    </div>
</div>

<script>
// ---------------- DADOS E SEGURANÇA ----------------
let usuarioLogado = null;
let cronometros = {};

function carregarDados() {
    const dados = localStorage.getItem("feizao_moraes");
    if (dados) usuarioLogado = JSON.parse(dados);
}

function salvarDados() {
    if (usuarioLogado) {
        localStorage.setItem("feizao_moraes", JSON.stringify(usuarioLogado));
    }
}

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
        aviso.textContent = "Preencha todos os campos corretamente!";
        aviso.className = "block p-3 mb-4 rounded-lg text-center text-sm bg-vermelho/10 text-vermelho";
        return;
    }

    aviso.textContent = "Carregando dados...";
    aviso.className = "block p-3 mb-4 rounded-lg text-center text-sm bg-yellow-500/10 text-yellow-500";
    document.getElementById("btn-acessar").disabled = true;

    try {
        await new Promise(resolve => setTimeout(resolve, 800));

        usuarioLogado = {
            ra: ra,
            digito: digito,
            uf: uf,
            senha: senha,
            nome: "Marcelo Lima Del Rei Santos",
            serie: "8º Ano B Integral",
            escola: "Paulo Sarasate Governador",
            frequencia: 92,
            atividades: { tarefa: [], redacao: [], matific: [], alura: [], speak: [] }
        };

        const dadosAntigos = localStorage.getItem(`feizao_${ra}`);
        if (dadosAntigos) usuarioLogado.atividades = JSON.parse(dadosAntigos);

        salvarDados();
        abrirPainel();
    } catch (e) {
        aviso.textContent = "Erro ao conectar. Tente novamente.";
        aviso.className = "block p-3 mb-4 rounded-lg text-center text-sm bg-vermelho/10 text-vermelho";
    } finally {
        document.getElementById("btn-acessar").disabled = false;
    }
}

function abrirPainel() {
    document.getElementById("tela-login").classList.add("hidden");
    document.getElementById("painel-principal").classList.remove("hidden");

    document.getElementById("inicial-usuario").textContent = usuarioLogado.nome.charAt(0);
    document.getElementById("nome-usuario").textContent = usuarioLogado.nome;
    document.getElementById("serie-turma").textContent = usuarioLogado.serie;
    document.getElementById("escola").textContent = usuarioLogado.escola;
    document.getElementById("nome-boas-vindas").textContent = usuarioLogado.nome.split(" ")[0];

    atualizarResumo();
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
    let titulo = "", tempo = 1, prazo = "";

    switch(tipo) {
        case 'tarefa':
            titulo = document.getElementById("titulo-tarefa").value.trim();
            tempo = parseInt(document.getElementById("tempo-tarefa").value);
            prazo = document.getElementById("prazo-tarefa").value;
            break;
        case 'redacao':
            titulo = document.getElementById("titulo-redacao").value.trim();
            tempo = parseInt(document.getElementById("tempo-redacao").value);
            prazo = document.getElementById("prazo-redacao").value;
            break;
        case 'matific':
            titulo = document.getElementById("titulo-matific").value.trim();
            tempo = parseInt(document.getElementById("tempo-matific").value);
            prazo = document.getElementById("prazo-matific").value;
            break;
        case 'alura':
            titulo = document.getElementById("titulo-alura").value.trim();
            tempo = parseInt(document.getElementById("tempo-alura").value);
            prazo = document.getElementById("prazo-alura").value;
            break;
        case 'speak':
            titulo = document.getElementById("titulo-speak").value.trim();
            tempo = parseInt(document.getElementById("tempo-speak").value);
            prazo = document.getElementById("prazo-speak").value;
            break;
    }

    if (!titulo) return alert("Digite um título!");
    if (tempo < 1) return alert("Tempo mínimo é 1 minuto!");

    const nova = {
        id: Date.now(),
        titulo,
        tempoTotal: tempo * 60,
        tempoRestante: tempo * 60,
        prazo,
        status: "pendente"
    };

    usuarioLogado.atividades[tipo].push(nova);
    localStorage.setItem(`feizao_${usuarioLogado.ra}`, JSON.stringify(usuarioLogado.atividades));
    salvarDados();

    atualizarResumo();
    atualizarLista(tipo);
}

function atualizarResumo() {
    const todas = Object.values(usuarioLogado.atividades).flat();
    document.getElementById("qtd-pendentes").textContent = todas.filter(a => a.status !== "concluida").length;
    document.getElementById("qtd-concluidas").textContent = todas.filter(a => a.status === "concluida").length;
}

function atualizarLista(tipo) {
    const lista = document.getElementById(`lista-${tipo}`);
    const itens = usuarioLogado.atividades[tipo];

    if (!itens || itens.length === 0) {
        lista.innerHTML = `<div class="text-center py-8 text-textoCinza">Nenhuma atividade cadastrada</div>`;
        return;
    }

    lista.innerHTML = itens.map(ativ => `
        <div class="card border-l-4 ${tipo === 'tarefa' ? 'border-vermelho' : tipo === 'redacao' ? 'border-redacao' : tipo === 'matific' ? 'border-matific' : tipo === 'alura' ? 'border-alura' : 'border-speak'}">
            <div class="flex justify-between items-center">
                <div>
                    <span class="mr-2">${tipo === 'tarefa' ? '📋' : tipo === 'redacao' ? '✍️' : tipo === 'matific' ? '➕' : tipo === 'alura' ? '📘' : '🗣️'}</span>
                    ${ativ.titulo}
                </div>
                <span class="text-sm ${ativ.status === 'concluida' ? 'text-green-500' : 'text-textoCinza'}">
                    ${ativ.status === 'concluida' ? 'Concluída' : 'Pendente'}
                </span>
            </div>
            <div class="mt-3 flex justify-end gap-2">
                ${ativ.status === 'pendente' ? `<button onclick="concluir('${tipo}', ${ativ.id})" class="bg-vermelho hover:bg-vermelhoEscuro text-white px-3 py-1 rounded text-sm">Concluir</button>` : ""}
            </div>
        </div>
    `).join("");
}

function concluir(tipo, id) {
    const ativ = usuarioLogado.atividades[tipo].find(a => a.id === id);
    if (ativ) {
        ativ.status = "concluida";
        localStorage.setItem(`feizao_${usuarioLogado.ra}`, JSON.stringify(usuarioLogado.atividades));
        salvarDados();
        atualizarResumo();
        atualizarLista(tipo);
    }
}

function sair() {
    if (confirm("Deseja sair?")) {
        usuarioLogado = null;
        localStorage.removeItem("feizao_moraes");
        location.reload();
    }
}

window.onload = () => {
    carregarDados();
    if (usuarioLogado) abrirPainel();
};
</script>

</body>
</html>
