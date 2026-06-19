<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#FFFFFF">
    <title>Feizão de Moraes | Sistema de Estudos</title>
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='12' fill='%230055CC'/%3E%3Ctext x='50' y='60' font-size='42' font-weight='bold' fill='%23FFFFFF' text-anchor='middle'%3EFM%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primaria: '#0055CC',
                        vermelho: '#E61B23',
                        fundo: '#F8FAFD',
                        card: '#FFFFFF',
                        textoPrincipal: '#1E293B',
                        textoSecundario: '#64748B',
                        borda: '#E2E8F0',
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
            .campo { @apply w-full px-4 py-3 border border-borda rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-primaria/20 focus:border-primaria transition-shadow; }
            .btn-principal { @apply w-full bg-primaria hover:bg-primaria/90 text-white font-semibold py-4 rounded-lg transition-colors; }
            .btn-secundario { @apply w-full bg-white border border-primaria text-primaria font-semibold py-3.5 rounded-lg transition-colors hover:bg-primaria/5; }
            .menu-item { @apply flex items-center gap-3 w-full px-4 py-3 rounded-lg text-left text-textoPrincipal hover:bg-primaria/5 transition-colors; }
            .menu-ativo { @apply bg-primaria/10 text-primaria font-medium; }
            .card-conteudo { @apply bg-card rounded-xl shadow-sm border border-borda p-5; }
        }

        * { scrollbar-width: thin; scrollbar-color: #0055CC #F8FAFD; }
        html, body { @apply bg-fundo text-textoPrincipal min-h-screen; }

        .logo-sistema {
            font-size: 28px;
            font-weight: 900;
            color: #000000;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="tela-login" class="min-h-screen flex flex-col justify-center">
    <div class="conteudo w-full max-w-md">
        <div class="text-center mb-8">
            <div class="flex items-center justify-center gap-3 mb-2">
                <i class="fa fa-graduation-cap text-4xl text-primaria"></i>
                <h1 class="logo-sistema">FEIZÃO DE MORAES</h1>
            </div>
            <p class="text-textoSecundario text-lg">Estudante</p>
            <p class="text-textoSecundario text-sm mt-1">Preencha seus dados para acessar o sistema</p>
        </div>

        <div class="card-conteudo">
            <div id="aviso-login" class="hidden p-3 mb-4 rounded-lg text-center text-sm"></div>

            <div class="grid grid-cols-3 gap-3 mb-4">
                <div class="col-span-2">
                    <label class="block text-sm text-textoSecundario mb-1">RA</label>
                    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">
                </div>
                <div>
                    <label class="block text-sm text-textoSecundario mb-1">Dígito</label>
                    <input type="text" id="digito-ra" class="campo" placeholder="0" maxlength="1">
                </div>
            </div>

            <div class="mb-4">
                <label class="block text-sm text-textoSecundario mb-1">UF</label>
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
                <label class="block text-sm text-textoSecundario mb-1">Senha</label>
                <div class="relative">
                    <input type="password" id="senha" class="campo pr-10" placeholder="Digite sua senha">
                    <button type="button" onclick="mostrarSenha()" class="absolute right-3 top-3 text-textoSecundario hover:text-textoPrincipal">
                        <i class="fa fa-eye"></i>
                    </button>
                </div>
                <p class="text-right mt-2">
                    <a href="#" class="text-primaria text-sm">Esqueceu a senha?</a>
                </p>
            </div>

            <button onclick="fazerLogin()" id="btn-acessar" class="btn-principal mb-3">Acessar</button>
            <button type="button" class="btn-secundario">Voltar</button>

            <div class="text-center mt-6">
                <p class="text-textoSecundario text-sm">Preciso de ajuda</p>
            </div>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL COM MENU LATERAL -->
<div id="painel-principal" class="hidden min-h-screen">
    <div class="flex flex-col md:flex-row h-screen">
        <!-- MENU LATERAL -->
        <aside id="menu-lateral" class="bg-white border-r border-borda w-full md:w-72 flex-shrink-0 overflow-y-auto">
            <div class="p-5 border-b border-borda">
                <div class="flex items-center gap-3 mb-3">
                    <div class="w-12 h-12 rounded-full bg-primaria/10 flex items-center justify-center text-primaria font-bold text-xl" id="inicial-usuario">A</div>
                    <div>
                        <h3 class="font-semibold text-lg" id="nome-usuario">Carregando...</h3>
                        <p class="text-sm text-textoSecundario" id="serie-turma">---</p>
                    </div>
                </div>
                <p class="text-xs text-textoSecundario" id="escola">---</p>
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

                <button onclick="sair()" class="menu-item w-full mt-6 text-erro hover:bg-erro/10 hover:text-erro">
                    <i class="fa fa-sign-out fa-lg"></i>
                    <span>Sair</span>
                </button>
            </nav>
        </aside>

        <!-- CONTEÚDO PRINCIPAL -->
        <main class="flex-1 overflow-y-auto p-5 md:p-8">
            <div id="conteudo-home" class="conteudo-secao">
                <h2 class="text-2xl font-bold mb-6">Olá, <span id="nome-boas-vindas"></span>!</h2>
                <div class="grid md:grid-cols-3 gap-5 mb-8">
                    <div class="card-conteudo border-t-4 border-primaria">
                        <h3 class="text-lg font-semibold mb-2">Tarefas Pendentes</h3>
                        <p class="text-3xl font-bold text-primaria" id="qtd-pendentes">0</p>
                    </div>
                    <div class="card-conteudo border-t-4 border-sucesso">
                        <h3 class="text-lg font-semibold mb-2">Concluídas</h3>
                        <p class="text-3xl font-bold text-sucesso" id="qtd-concluidas">0</p>
                    </div>
                    <div class="card-conteudo border-t-4 border-alerta">
                        <h3 class="text-lg font-semibold mb-2">Frequência</h3>
                        <p class="text-3xl font-bold text-alerta" id="valor-frequencia">0%</p>
                    </div>
                </div>
            </div>

            <!-- TAREFAS -->
            <div id="conteudo-tarefa" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📋 Tarefa SP</h2>
                <div class="card-conteudo mb-5">
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
                <div class="card-conteudo mb-5">
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
                    <button onclick="mudarSubcategoria('matific')" id="sub-matific" class="card-conteudo hover:shadow-md transition-shadow text-left border-t-4 border-matific">
                        <h3 class="text-xl font-bold text-matific">➕ Matific</h3>
                        <p class="text-textoSecundario mt-1">Atividades de matemática</p>
                    </button>
                    <button onclick="mudarSubcategoria('alura')" id="sub-alura" class="card-conteudo hover:shadow-md transition-shadow text-left border-t-4 border-alura">
                        <h3 class="text-xl font-bold text-alura">📘 Alura</h3>
                        <p class="text-textoSecundario mt-1">Cursos e conteúdos</p>
                    </button>
                    <button onclick="mudarSubcategoria('speak')" id="sub-speak" class="card-conteudo hover:shadow-md transition-shadow text-left border-t-4 border-speak">
                        <h3 class="text-xl font-bold text-speak">🗣️ Speak</h3>
                        <p class="text-textoSecundario mt-1">Inglês e comunicação</p>
                    </button>
                </div>

                <div id="conteudo-matific" class="hidden">
                    <h3 class="text-xl font-semibold mb-4">➕ Matific</h3>
                    <div class="card-conteudo mb-5">
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
                    <div class="card-conteudo mb-5">
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
                    <div class="card-conteudo mb-5">
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
                <div class="card-conteudo">
                    <p class="text-textoSecundario mb-4">Eventos e atividades sincronizadas</p>
                    <div id="lista-agenda" class="space-y-3"></div>
                </div>
            </div>

            <!-- BOLETIM -->
            <div id="conteudo-boletim" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">📊 Boletim e Avaliações</h2>
                <div class="card-conteudo">
                    <h3 class="text-lg font-semibold mb-4">Notas por Disciplina</h3>
                    <div class="overflow-x-auto">
                        <table class="w-full border-collapse">
                            <thead>
                                <tr class="bg-primaria/5">
                                    <th class="text-left p-3 border-b border-borda">Disciplina</th>
                                    <th class="text-center p-3 border-b border-borda">1º Bimestre</th>
                                    <th class="text-center p-3 border-b border-borda">2º Bimestre</th>
                                    <th class="text-center p-3 border-b border-borda">3º Bimestre</th>
                                    <th class="text-center p-3 border-b border-borda">4º Bimestre</th>
                                    <th class="text-center p-3 border-b border-borda">Média Final</th>
                                </tr>
                            </thead>
                            <tbody id="tabela-notas"></tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- PRESENÇA -->
            <div id="conteudo-presenca" class="conteudo-secao hidden">
                <h2 class="text-2xl font-bold mb-5">👤 Presença</h2>
                <div class="card-conteudo text-center">
                    <p class="text-lg">Total de aulas: <span class="font-semibold" id="total-aulas">0</span></p>
                    <p class="text-lg">Presenças: <span class="font-semibold text-sucesso" id="total-presencas">0</span></p>
                    <p class="text-lg">Faltas: <span class="font-semibold text-erro" id="total-faltas">0</span></p>
                    <div class="w-full bg-borda h-3 rounded-full mt-4">
                        <div id="barra-frequencia" class="bg-sucesso h-3 rounded-full" style="width: 0%"></div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</div>

<script>
// ---------------- CONFIGURAÇÕES E SEGURANÇA ----------------
const TEMPO_MINIMO = 60;
let usuarioLogado = null;
let cronometros = {};

// Armazenamento local seguro
function carregarDados() {
    const dados = localStorage.getItem("feizao_moraes_dados");
    if (dados) usuarioLogado = JSON.parse(dados);
}

function salvarDados() {
    if (usuarioLogado) {
        localStorage.setItem("feizao_mo
