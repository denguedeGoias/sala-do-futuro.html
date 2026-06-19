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
                        fundo: '#080808',
                        card: '#101010',
                        borda: '#1A1A1A',
                        vermelho: '#E50914',
                        vermelhoEscuro: '#B00006',
                        texto: '#E8E8E8',
                        textoSuave: '#999999',
                        sucesso: '#22C55E',
                        alerta: '#F59E0B',
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
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scrollbar-width: thin;
            scrollbar-color: #E50914 #000000;
        }

        html, body {
            background-color: #000000;
            color: #E8E8E8;
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
            min-height: 100vh;
        }

        .conteudo {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }

        .campo {
            width: 100%;
            padding: 0.75rem 1rem;
            background-color: #101010;
            border: 1px solid #1A1A1A;
            border-radius: 0.5rem;
            color: #E8E8E8;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }

        .campo:focus {
            outline: none;
            border-color: #E50914;
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.15);
        }

        .btn-principal {
            background-color: #E50914;
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.25rem;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .btn-principal:hover {
            background-color: #B00006;
        }

        .btn-secundario {
            background-color: transparent;
            color: #E50914;
            border: 1px solid #E50914;
            border-radius: 0.5rem;
            padding: 0.75rem 1.25rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-secundario:hover {
            background-color: rgba(229, 9, 20, 0.08);
        }

        .menu-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100%;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            color: #E8E8E8;
            background: transparent;
            border: none;
            text-align: left;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .menu-item:hover {
            background-color: rgba(229, 9, 20, 0.08);
        }

        .menu-ativo {
            background-color: rgba(229, 9, 20, 0.12);
            color: #E50914;
            font-weight: 500;
        }

        .card {
            background-color: #101010;
            border: 1px solid #1A1A1A;
            border-radius: 0.75rem;
            padding: 1.25rem;
            transition: border 0.2s ease;
        }

        .card:hover {
            border-color: #252525;
        }

        .linha-divisoria {
            height: 1px;
            background: linear-gradient(to right, transparent, #222, transparent);
            margin: 1.5rem 0;
        }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="tela-login" class="min-h-screen flex flex-col justify-center">
    <div class="conteudo w-full max-w-md">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-black text-vermelho tracking-tight">FEIZÃO DE MORAES</h1>
            <p class="text-textoSuave mt-1">Sistema de Atividades</p>
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
                    <option value="MG">MG</option>
                    <option value="RJ">RJ</option>
                    <option value="RS">RS</option>
                    <option value="PR">PR</option>
                    <option value="BA">BA</option>
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

            <button onclick="entrar()" class="btn-principal w-full mb-3">Acessar Sistema</button>

            <div class="text-center mt-5 text-textoSuave text-xs">
                Desenvolvido por Dengue de Goiás
            </div>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL -->
<div id="painel-principal" class="hidden min-h-screen flex flex-col md:flex-row">
    <!-- MENU LATERAL -->
    <aside class="w-full md:w-64 bg-fundo border-r border-borda flex-shrink-0">
        <div class="p-4 border-b border-borda">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-vermelho/15 flex items-center justify-center text-vermelho font-bold" id="inicial-nome">A</div>
                <div>
                    <h3 class="font-medium" id="nome-aluno">Carregando...</h3>
                    <p class="text-xs text-textoSuave" id="dados-aluno">---</p>
                </div>
            </div>
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
                <span>Redação</span>
            </button>
            <button onclick="mudarAba('matific')" id="aba-matific" class="menu-item">
                <i class="fa fa-calculator"></i>
                <span>Matific</span>
            </button>
            <button onclick="mudarAba('alura')" id="aba-alura" class="menu-item">
                <i class="fa fa-book"></i>
                <span>Alura</span>
            </button>
            <button onclick="mudarAba('speak')" id="aba-speak" class="menu-item">
                <i class="fa fa-comments"></i>
                <span>Speak</span>
            </button>
            <button onclick="mudarAba('agenda')" id="aba-agenda" class="menu-item">
                <i class="fa fa-calendar"></i>
                <span>Agenda</span>
            </button>
            <button onclick="mudarAba('boletim')" id="aba-boletim" class="menu-item">
                <i class="fa fa-bar-chart"></i>
                <span>Boletim</span>
            </button>

            <div class="linha-divisoria my-3"></div>

            <button onclick="sair()" class="menu-item text-vermelho hover:bg-vermelho/10">
                <i class="fa fa-sign-out"></i>
                <span>Sair</span>
            </button>
        </nav>
    </aside>

    <!-- ÁREA DE CONTEÚDO -->
    <main class="flex-1 p-4 md:p-6 overflow-auto">
        <!-- ABA INÍCIO -->
        <div id="conteudo-inicio" class="conteudo-aba">
            <h2 class="text-xl font-semibold mb-5">Visão Geral</h2>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                <div class="card border-t-2 border-vermelho">
                    <h3 class="text-sm text-textoSuave">Pendentes</h3>
                    <p class="text-3xl font-bold mt-1" id="cont-pendentes">0</p>
                </div>
                <div class="card border-t-2 border-sucesso">
                    <h3 class="text-sm text-textoSuave">Concluídas</h3>
                    <p class="text-3xl font-bold mt-1" id="cont-concluidas">0</p>
                </div>
                <div class="card border-t-2 border-alerta">
                    <h3 class="text-sm text-textoSuave">Frequência</h3>
                    <p class="text-3xl font-bold mt-1" id="valor-frequencia">0%</p>
                </div>
            </div>
        </div>

        <!-- ABA TAREFAS / CATEGORIAS -->
        <div id="conteudo-tarefas" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Tarefas Comuns</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-tarefa" class="campo" placeholder="Título da tarefa">
                    <input type="number" id="tempo-tarefa" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-tarefa" class="campo">
                </div>
                <button onclick="adicionar('tarefa')" class="btn-principal">Adicionar</button>
            </div>
            <div id="lista-tarefa" class="space-y-3"></div>
        </div>

        <div id="conteudo-redacao" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Redação Paulista</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-redacao" class="campo" placeholder="Tema da redação">
                    <input type="number" id="tempo-redacao" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-redacao" class="campo">
                </div>
                <button onclick="adicionar('redacao')" class="btn-principal">Adicionar</button>
            </div>
            <div id="lista-redacao" class="space-y-3"></div>
        </div>

        <div id="conteudo-matific" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Matific</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-matific" class="campo" placeholder="Atividade">
                    <input type="number" id="tempo-matific" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-matific" class="campo">
                </div>
                <button onclick="adicionar('matific')" class="btn-principal">Adicionar</button>
            </div>
            <div id="lista-matific" class="space-y-3"></div>
        </div>

        <div id="conteudo-alura" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Alura</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-alura" class="campo" placeholder="Curso/Aula">
                    <input type="number" id="tempo-alura" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-alura" class="campo">
                </div>
                <button onclick="adicionar('alura')" class="btn-principal">Adicionar</button>
            </div>
            <div id="lista-alura" class="space-y-3"></div>
        </div>

        <div id="conteudo-speak" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Speak</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-speak" class="campo" placeholder="Aula de inglês">
                    <input type="number" id="tempo-speak" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-speak" class="campo">
                </div>
                <button onclick="adicionar('speak')" class="btn-principal">Adicionar</button>
            </div>
            <div id="lista-speak" class="space-y-3"></div>
        </div>

        <div id="conteudo-agenda" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Agenda</h2>
            <div class="card">
                <div id="lista-agenda" class="space-y-3">
                    <div class="p-3 rounded bg-card border border-borda">
                        <p class="font-medium">Prova de Matemática</p>
                        <p class="text-xs text-textoSuave mt-1">22/06/2026 • 08h00</p>
                    </div>
                    <div class="p-3 rounded bg-card border border-borda">
                        <p class="font-medium">Entrega de Redação</p>
                        <p class="text-xs text-textoSuave mt-1">25/06/2026 • 18h00</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="conteudo-boletim" class="conteudo-aba hidden">
            <h2 class="text-xl font-semibold mb-4">Boletim de Notas</h2>
            <div class="card overflow-x-auto">
                <table class="w-full text-sm">
                    <thead>
                        <tr class="border-b border-borda">
                            <th class="text-left p-3">Disciplina</th>
                            <th class="text-center p-3">1º Bim</th>
                            <th class="text-center p-3">2º Bim</th>
                            <th class="text-center p-3">3º Bim</th>
                            <th class="text-center p-3">4º Bim</th>
                            <th class="text-center p-3">Média</th>
                        </tr>
                    </thead>
                    <tbody id="tabela-notas">
                        <tr class="border-b border-borda/40">
                            <td class="p-3">Língua Portuguesa</td>
                            <td class="p-3 text-center">8,2</td>
                            <td class="p-3 text-center">8,5</td>
                            <td class="p-3 text-center">8,8</td>
                            <td class="p-3 text-center">9,0</td>
                            <td class="p-3 text-center font-medium text-sucesso">8,6</td>
                        </tr>
                        <tr class="border-b border-borda/40">
                            <td class="p-3">Matemática</td>
                            <td class="p-3 text-center">7,9</td>
                            <td class="p-3 text-center">8,1</td>
                            <td class="p-3 text-center">8,3</td>
                            <td class="p-3 text-center">8,7</td>
                            <td class="p-3 text-center font-medium text-sucesso">8,3</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>
</div>

<script>
// ---------------- VARIÁVEIS GERAIS ----------------
let usuario = null;
let cronometros = {};
const TEMPO_MINIMO = 60; // 1 minuto em segundos

// ---------------- FUNÇÕES DE ARMAZENAMENTO ----------------
function carregarDados() {
    const dados = localStorage.getItem("feizao_moraes");
    if (dados) usuario = JSON.parse(dados);
}

function salvarDados() {
    if (usuario) localStorage.setItem("feizao_moraes", JSON.stringify(usuario));
}

function alternarSenha() {
    const campo = document.getElementById("senha");
    campo.type = campo.type === "password" ? "text" : "password";
}

// ---------------- LOGIN ----------------
async function entrar() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito-ra").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();
    const aviso = document.getElementById("aviso-login");

    if (!ra || !senha) {
        aviso.textContent = "Preencha todos os campos";
        aviso.className = "block mb-4 p-2.5 rounded bg-vermelho/10 text-vermelho text-center text-sm";
        return;
    }

    aviso.textContent = "Carregando dados...";
    aviso.className = "block mb-4 p-2.5 rounded bg-alerta/10 text-alerta text-center text-sm";

    await new Promise(resolve => setTimeout(resolve, 800));

    usuario = {
        ra: ra,
        digito: digito,
        uf: uf,
        nome: "Aluno Exemplo",
        serie: "9º Ano",
        turma: "B",
        escola: "Escola Estadual",
        frequencia: 92,
        atividades: {
            tarefa: [],
            redacao: [],
            matific: [],
            alura: [],
            speak: []
        }
    };

    const dadosSalvos = localStorage.getItem(`atividades_${ra}`);
    if (dadosSalvos) usuario.atividades = JSON.parse(dadosSalvos);

    salvarDados();
    abrirPainel();
}

function abrirPainel() {
    document.getElementById("tela-login").classList.add("hidden");
    document.getElementById("painel-principal").classList.remove("hidden");

    document.getElementById("inicial-nome").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nome-aluno").textContent = usuario.nome;
    document.getElementById("dados-aluno").textContent = `${usuario.serie} • ${usuario.turma}`;

    atualizarResumo();
}

// ---------------- NAVEGAÇÃO ----------------
function mudarAba(nome) {
    document.querySelectorAll(".conteudo-aba").forEach(el => el.classList.add("hidden"));
    document.querySelectorAll(".menu-item").forEach(el => el.classList.remove("menu-ativo"));

    document.getElementById(`conteudo-${nome}`).classList.remove("hidden");
    document.getElementById(`aba-${nome}`).classList.add("menu-ativo");

    if (["tarefas", "redacao", "matific", "alura", "speak"].includes(nome)) {
        atualizarLista(nome.replace("s", ""));
    }
}

// ---------------- GERENCIAMENTO DE ATIVIDADES ----------------
function adicionar(tipo) {
    const titulo = document.getElementById(`titulo-${tipo}`).value.trim();
    const tempo = parseInt(document.getElementById(`tempo-${tipo}`).value);
    const prazo = document.getElementById(`prazo-${tipo}`).value || "";

    if (!titulo) return alert("Digite um título");
    if (tempo < 1) return alert("Tempo mínimo é 1 minuto");

    const atividade = {
        id: Date.now(),
        titulo: titulo,
        tempoTotal: tempo * 60,
        tempoRestante: tempo * 60,
        prazo: prazo,
        status: "pendente",
        inicio: null
    };

    usuario.atividades[tipo].push(atividade);
    localStorage.setItem(`atividades_${usuario.ra}`, JSON.stringify(usuario.atividades));
    salvarDados();

    limparCampos(tipo);
    atualizarLista(tipo);
    atualizarResumo();
}

function limparCampos(tipo) {
    document.getElementById(`titulo-${tipo}`).value = "";
    document.getElementById(`tempo-${tipo}`).value = "1";
    document.getElementById(`prazo-${tipo}`).value = "";
}

function iniciarContagem(tipo, id) {
    const ativ = usuario.atividades[tipo].find(a => a.id === id);
    if (!ativ || ativ.status !== "pendente") return;

    ativ.inicio = Date.now();
    ativ.status = "andamento";
    salvarDados();

    cronometros[id] = setInterval(() => {
        const decorrido = Math.floor((Date.now() - ativ.inicio) / 1000);
        ativ.tempoRestante = Math.max(0, ativ.tempoTotal - decorrido);

        if (ativ.tempoRestante <= 0) {
            clearInterval(cronometros[id]);
            ativ.status = "pronto";
        }

        salvarDados();
        atualizarLista(tipo);
    }, 1000);
}

function concluirAtividade(tipo, id) {
    const ativ = usuario.atividades[tipo].find(a => a.id === id);
    if (!ativ || ativ.status !== "pronto") return;

    ativ.status = "concluida";
    localStorage.setItem(`atividades_${usuario.ra}`, JSON.stringify(usuario.atividades));
    salvarDados();

    atualizarLista(tipo);
    atualizarResumo();
}

// ---------------- ATUALIZAÇÃO DE TELA ----------------
function atualizarResumo() {
    const todas = Object.values(usuario.atividades).flat();
    document.getElementById("cont-pendentes").textContent = todas.filter(a => a.status !== "concluida").length;
    document.getElementById("cont-concluidas").textContent = todas.filter(a => a.status === "concluida").length;
    document.getElementById("valor-frequencia").textContent = `${usuario.frequencia}%`;
}

function atualizarLista(tipo) {
    const container = document.getElementById(`lista-${tipo}`);
    const itens = usuario.atividades[tipo];

    if (!itens || itens.length === 0) {
        container.innerHTML = `<div class="p-4 text-center text-textoSuave">Nenhuma atividade cadastrada</div>`;
        return;
    }

    container.innerHTML = itens.map(ativ => {
        const min = Math.floor(ativ.tempoRestante / 60);
        const seg = ativ.tempoRestante % 60;
        const tempo = `${min}:${seg.toString().padStart(2, "0")}`;

        return `
        <div class="card border-l-2 ${tipo === 'tarefa' ? 'border-vermelho' : tipo === 'redacao' ? 'border-redacao' : tipo === 'matific' ? 'border-matific' : tipo === 'alura' ? 'border-alura' : 'border-speak'}">
            <div class="flex justify-between items-center flex-wrap gap-2">
                <div>
                    <span class="font-medium">${ativ.titulo}</span>
                    ${ativ.prazo ? `<span class="text-xs text-textoSuave ml-2">Prazo: ${new Date(ativ.prazo).toLocaleDateString("pt-BR")}</span>` : ""}
                </div>
                <span class="text-sm ${ativ.status === "concluida" ? "text-sucesso" : ativ.status === "pronto" ? "text-alerta" : ativ.status === "andamento" ? "text-vermelho" : "text-textoSuave"}">
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
}

function sair() {
    if (confirm("Deseja sair do sistema?")) {
        usuario = null;
        localStorage.removeItem("feizao_moraes");
        location.reload();
    }
}

// ---------------- INICIALIZAÇÃO ----------------
window.onload = () => {
    carregarDados();
    if (usuario) abrirPainel();
};
</script>

</body>
</html>
