<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#E50914">
    <title>Feizão de Moraes</title>
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='12' fill='%23000000'/%3E%3Ctext x='50' y='60' font-size='42' font-weight='bold' fill='%23E50914' text-anchor='middle'%3EFM%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        sucesso: '#22C55E',
                        alerta: '#F59E0B',
                        erro: '#EF4444',
                        neutro: '#6B7280'
                    },
                    fontFamily: {
                        sans: ['Segoe UI', 'Roboto', 'Arial', 'sans-serif']
                    }
                }
            }
        }
    </script>

    <style>
        :root {
            --cor-principal: #E50914;
            --cor-principal-escura: #B00006;
            --cor-fundo: #F8F9FA;
            --cor-card: #FFFFFF;
            --cor-borda: #E5E7EB;
            --cor-texto: #111827;
            --cor-texto-suave: #6B7280;
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
            transition: all 0.25s ease;
        }

        .campo {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid var(--cor-borda);
            border-radius: 0.5rem;
            background: var(--cor-card);
            color: var(--cor-texto);
            outline: none;
            transition: border 0.2s ease;
        }

        .campo:focus {
            border-color: var(--cor-principal);
            box-shadow: 0 0 0 2px rgba(229, 9, 20, 0.15);
        }

        .btn-principal {
            background: var(--cor-principal);
            color: white;
            border: none;
            border-radius: 0.5rem;
            padding: 0.75rem 1.25rem;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .btn-principal:hover {
            background: var(--cor-principal-escura);
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
            background: rgba(229, 9, 20, 0.08);
        }

        .menu-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100%;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            background: transparent;
            color: var(--cor-texto);
            border: none;
            text-align: left;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .menu-item:hover {
            background: rgba(229, 9, 20, 0.08);
        }

        .menu-ativo {
            background: rgba(229, 9, 20, 0.12);
            color: var(--cor-principal);
            font-weight: 500;
        }

        .card {
            background: var(--cor-card);
            border: 1px solid var(--cor-borda);
            border-radius: 0.75rem;
            padding: 1.25rem;
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
    <div class="w-full max-w-md mx-auto px-4">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-black" style="color: var(--cor-principal)">FEIZÃO DE MORAES</h1>
            <p class="text-sm mt-2" style="color: var(--cor-texto-suave)">Sistema de Tarefas e Redação Paulista</p>
        </div>

        <div class="card">
            <div id="aviso" class="hidden mb-4 p-2.5 rounded text-center text-sm"></div>

            <div class="grid grid-cols-3 gap-3 mb-4">
                <div class="col-span-2">
                    <label class="block text-sm mb-1" style="color: var(--cor-texto-suave)">RA</label>
                    <input type="text" id="ra" class="campo" placeholder="Digite seu RA">
                </div>
                <div>
                    <label class="block text-sm mb-1" style="color: var(--cor-texto-suave)">Dígito</label>
                    <input type="text" id="digito" class="campo" placeholder="0" maxlength="1">
                </div>
            </div>

            <div class="mb-4">
                <label class="block text-sm mb-1" style="color: var(--cor-texto-suave)">UF</label>
                <select id="uf" class="campo">
                    <option value="SP" selected>SP</option>
                    <option value="MG">MG</option>
                    <option value="RJ">RJ</option>
                    <option value="GO">GO</option>
                    <option value="RS">RS</option>
                </select>
            </div>

            <div class="mb-6">
                <label class="block text-sm mb-1" style="color: var(--cor-texto-suave)">Senha</label>
                <div class="relative">
                    <input type="password" id="senha" class="campo pr-10" placeholder="Senha de acesso">
                    <button type="button" onclick="mostrarSenha()" class="absolute right-3 top-1/2 -translate-y-1/2" style="color: var(--cor-texto-suave)">
                        <i class="fa fa-eye"></i>
                    </button>
                </div>
            </div>

            <button onclick="entrar()" class="btn-principal w-full">Acessar Sistema</button>

            <div class="text-center mt-6 text-xs" style="color: var(--cor-texto-suave)">
                Desenvolvido por Dengue de Goiás
            </div>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL -->
<div id="painel" class="hidden min-h-screen flex flex-col md:flex-row">
    <!-- MENU LATERAL -->
    <aside class="w-full md:w-64 barra-lateral flex-shrink-0">
        <div class="p-4 border-b" style="border-color: var(--cor-borda)">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-lg" style="background: rgba(229,9,20,0.15); color: var(--cor-principal)" id="inicial">A</div>
                <div>
                    <h3 class="font-medium" id="nome-usuario">Aluno</h3>
                    <p class="text-xs" style="color: var(--cor-texto-suave)" id="dados-usuario">---</p>
                </div>
            </div>
            <div class="mt-2 text-xs text-sucesso" id="status-sync">✅ Sincronizado</div>
        </div>

        <nav class="p-3 space-y-1">
            <button onclick="trocarAba('inicio')" id="menu-inicio" class="menu-item menu-ativo">
                <i class="fa fa-home"></i> Início
            </button>
            <button onclick="trocarAba('tarefas')" id="menu-tarefas" class="menu-item">
                <i class="fa fa-check-square"></i> Tarefas
            </button>
            <button onclick="trocarAba('redacao')" id="menu-redacao" class="menu-item">
                <i class="fa fa-pencil"></i> Redação Paulista
            </button>
            <button onclick="trocarAba('cores')" id="menu-cores" class="menu-item">
                <i class="fa fa-palette"></i> Personalizar Cores
            </button>
            <button onclick="forcarAtualizacao()" class="menu-item text-alerta hover:bg-alerta/10">
                <i class="fa fa-refresh"></i> Atualizar Dados
            </button>
            <div class="h-px my-3" style="background: var(--cor-borda)"></div>
            <button onclick="sair()" class="menu-item text-erro hover:bg-erro/10">
                <i class="fa fa-sign-out-alt"></i> Sair
            </button>
        </nav>
    </aside>

    <!-- ÁREA DE CONTEÚDO -->
    <main class="flex-1 p-4 md:p-6 overflow-auto">
        <!-- INÍCIO -->
        <div id="conteudo-inicio" class="conteudo">
            <h2 class="text-xl font-semibold mb-5">Visão Geral</h2>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div class="card border-t-2" style="border-color: var(--cor-principal)">
                    <h3 class="text-sm" style="color: var(--cor-texto-suave)">Pendentes</h3>
                    <p class="text-3xl font-bold mt-1" style="color: var(--cor-principal)" id="qtd-pendentes">0</p>
                </div>
                <div class="card border-t-2 border-sucesso">
                    <h3 class="text-sm" style="color: var(--cor-texto-suave)">Concluídas</h3>
                    <p class="text-3xl font-bold mt-1 text-sucesso" id="qtd-concluidas">0</p>
                </div>
                <div class="card border-t-2 border-alerta">
                    <h3 class="text-sm" style="color: var(--cor-texto-suave)">Total</h3>
                    <p class="text-3xl font-bold mt-1 text-alerta" id="qtd-total">0</p>
                </div>
            </div>
        </div>

        <!-- TAREFAS -->
        <div id="conteudo-tarefas" class="conteudo hidden">
            <h2 class="text-xl font-semibold mb-4">📋 Tarefas</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-tarefa" class="campo" placeholder="Título da tarefa">
                    <input type="number" id="tempo-tarefa" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-tarefa" class="campo">
                </div>
                <textarea id="descricao-tarefa" class="campo mb-3" rows="2" placeholder="Descrição (opcional)"></textarea>
                <button onclick="adicionarItem('tarefa')" class="btn-principal">Adicionar</button>
            </div>
            <div id="lista-tarefas" class="space-y-3"></div>
        </div>

        <!-- REDAÇÃO -->
        <div id="conteudo-redacao" class="conteudo hidden">
            <h2 class="text-xl font-semibold mb-4">✍️ Redação Paulista</h2>
            <div class="card mb-5">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3">
                    <input type="text" id="titulo-redacao" class="campo" placeholder="Tema da redação">
                    <input type="number" id="tempo-redacao" min="1" value="1" class="campo" placeholder="Tempo (min)">
                    <input type="date" id="prazo-redacao" class="campo">
                </div>
                <textarea id="texto-redacao" class="campo mb-3" rows="4" placeholder="Conteúdo, anotações ou rascunho"></textarea>
                <button onclick="adicionarItem('redacao')" class="btn-principal">Salvar</button>
            </div>
            <div id="lista-redacoes" class="space-y-3"></div>
        </div>

        <!-- PERSONALIZAÇÃO DE CORES -->
        <div id="conteudo-cores" class="conteudo hidden">
            <h2 class="text-xl font-semibold mb-4">🎨 Personalizar Cores</h2>
            <div class="card max-w-lg">
                <p class="text-sm mb-4" style="color: var(--cor-texto-suave)">Escolha as cores que preferir — ficam salvas automaticamente:</p>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label class="block text-sm mb-2">Cor Principal</label>
                        <input type="color" id="input-cor-principal" value="#E50914" class="w-full h-10 cursor-pointer rounded">
                    </div>
                    <div>
                        <label class="block text-sm mb-2">Cor de Fundo</label>
                        <input type="color" id="input-cor-fundo" value="#F8F9FA" class="w-full h-10 cursor-pointer rounded">
                    </div>
                </div>

                <button onclick="aplicarCores()" class="btn-principal w-full">Aplicar</button>
                <button onclick="restaurarPadrao()" class="btn-secundario w-full mt-3">Restaurar Padrão</button>
            </div>
        </div>
    </main>
</div>

<script>
// ---------------- VARIÁVEIS GERAIS ----------------
let usuario = null;
let cronometros = {};
let sincronizacaoInterval;

// ---------------- SINCRONIZAÇÃO EM TEMPO REAL ----------------
function sincronizar() {
    if (!usuario) return;
    localStorage.setItem(`feizao_${usuario.ra}`, JSON.stringify(usuario));
    localStorage.setItem("feizao_sessao", JSON.stringify({ ra: usuario.ra, atualizado: new Date().toISOString() }));
    document.getElementById("status-sync").textContent = `✅ Sincronizado ${new Date().toLocaleTimeString()}`;
    atualizarTela();
}

function forcarAtualizacao() {
    document.getElementById("status-sync").textContent = "🔄 Atualizando...";
    setTimeout(sincronizar, 600);
}

function iniciarSync() {
    if (sincronizacaoInterval) clearInterval(sincronizacaoInterval);
    sincronizacaoInterval = setInterval(sincronizar, 1000); // atualiza a cada 1 segundo
}

// ---------------- LOGIN E ACESSO ----------------
function mostrarSenha() {
    const campo = document.getElementById("senha");
    campo.type = campo.type === "password" ? "text" : "password";
}

async function entrar() {
    const ra = document.getElementById("ra").value.trim();
    const digito = document.getElementById("digito").value.trim() || "0";
    const uf = document.getElementById("uf").value;
    const senha = document.getElementById("senha").value.trim();
    const aviso = document.getElementById("aviso");

    if (!ra || !senha) {
        aviso.textContent = "Preencha todos os campos!";
        aviso.className = "block p-2.5 mb-4 rounded bg-red-100 text-red-700";
        return;
    }

    aviso.textContent = "Carregando dados...";
    aviso.className = "block p-2.5 mb-4 rounded bg-amber-100 text-amber-700";
    await new Promise(resolve => setTimeout(resolve, 800));

    usuario = {
        ra: ra,
        digito: digito,
        uf: uf,
        nome: "Aluno",
        atividades: { tarefa: [], redacao: [] },
        config: { cores: { principal: "#E50914", fundo: "#F8F9FA" } }
    };

    const dadosSalvos = localStorage.getItem(`feizao_${ra}`);
    if (dadosSalvos) usuario = { ...usuario, ...JSON.parse(dadosSalvos) };

    abrirPainel();
    iniciarSync();
    carregarCoresSalvas();
    sincronizar();
}

function abrirPainel() {
    document.getElementById("tela-login").classList.add("hidden");
    document.getElementById("painel").classList.remove("hidden");
    document.getElementById("inicial").textContent = usuario.nome.charAt(0).toUpperCase();
    document.getElementById("nome-usuario").textContent = usuario.nome;
    document.getElementById("dados-usuario").textContent = `${usuario.uf} • RA ${usuario.ra}-${usuario.digito}`;
}

// ---------------- NAVEGAÇÃO ----------------
function trocarAba(nome) {
    document.querySelectorAll(".conteudo").forEach(el => el.classList.add("hidden"));
    document.querySelectorAll(".menu-item").forEach(el => el.classList.remove("menu-ativo"));
    document.getElementById(`conteudo-${nome}`).classList.remove("hidden");
    document.getElementById(`menu-${nome}`).classList.add("menu-ativo");
}

// ---------------- GERENCIAMENTO DE ITENS ----------------
function adicionarItem(tipo) {
    const titulo = document.getElementById(`titulo-${tipo}`).value.trim();
    const tempo = parseInt(document.getElementById(`tempo-${tipo}`).value);
    const prazo = document.getElementById(`prazo-${tipo}`).value || "";
    const descricao = tipo === "tarefa" 
        ? document.getElementById("descricao-tarefa").value 
        : document.getElementById("texto-redacao").value;

    if (!titulo) return alert("Digite um título!");
    if (tempo < 1) return alert("Tempo mínimo é 1 minuto!");

    const novo = {
        id: Date.now(),
        titulo,
        descricao,
        tempoTotal: tempo * 60,
        tempoRestante: tempo * 60,
        prazo,
        status: "pendente",
        inicio: null
    };

    usuario.atividades[tipo].push(novo);
    limparCampos(tipo);
    sincronizar();
}

function limparCampos(tipo) {
    document.getElementById(`titulo-${tipo}`).value = "";
    document.getElementById(`tempo-${tipo}`).value = "1";
    document.getElementById(`prazo-${tipo}`).value = "";
    if (tipo === "tarefa") document.getElementById("descricao-tarefa").value = "";
    if (tipo === "redacao") document.getElementById("texto-redacao").value = "";
}

function iniciarContagem(tipo, id) {
    const item = usuario.atividades[tipo].find(i => i.id === id);
    if (!item || item.status !== "pendente") return;

    item.inicio = Date.now();
    item.status = "andamento";

    cronometros[id] = setInterval(() => {
        const decorrido = Math.floor((Date.now() - item.inicio) / 1000);
        item.tempoRestante = Math.max(0, item.tempoTotal - decorrido);

        if (item.tempoRestante <= 0) {
            clearInterval(cronometros[id]);
            item.status = "pronto";
        }

        sincronizar();
    }, 1000);
}

function concluirItem(tipo, id) {
    const item = usuario.atividades[tipo].find(i => i.id === id);
    if (!item || item.status !== "pronto") return;
    item.status = "concluida";
    sincronizar();
}

// ---------------- PERSONALIZAÇÃO DE CORES ----------------
function aplicarCores() {
    const corP = document.getElementById("input-cor-principal").value;
    const corF = document.getElementById("input-cor-fundo").value;
    const corPEscura = escurecer(corP, 20);

    document.documentElement.style.setProperty("--cor-principal", corP);
    document.documentElement.style.setProperty("--cor-principal-escura", corPEscura);
    document.documentElement.style.setProperty("--cor-fundo", corF);

    usuario.config.cores = { principal: corP, fundo: corF };
    sincronizar();
}

function restaurarPadrao() {
    document.getElementById("input-cor-principal").value = "#E50914";
    document.getElementById("input-cor-fundo").value = "#F8F9FA";
    aplicarCores();
}

function escurecer(cor, porcentagem) {
    const r = parseInt(cor.slice(1,3),16);
    const g = parseInt(cor.slice(3,5),16);
    const b = parseInt(cor.slice(5,7),16);
    const novoR = Math.max(0, Math.round(r * (100 - porcentagem)/100)).toString(16).padStart(2,'0');
    const novoG = Math.max(0, Math.round(g * (100 - porcentagem)/100)).toString(16).padStart(2,'0');
    const novoB = Math.max(0, Math.round(b * (100 - porcentagem)/100)).toString(16).padStart(2,'0');
    return `#${novoR}${novoG}${novoB}`;
}

function carregarCoresSalvas() {
    if (!usuario?.config?.cores) return;
    const { principal, fundo } = usuario.config.cores;
    document.getElementById("input-cor-principal").value = principal;
    document.getElementById("input-cor-fundo").value = fundo;
    aplicarCores();
}

// ---------------- ATUALIZAÇÃO DE TELA ----------------
function atualizarTela() {
    const todos = [...usuario.atividades.tarefa, ...usuario.atividades.redacao];
    document.getElementById("qtd-pendentes").textContent = todos.filter(i => i.status !== "concluida").length;
    document.getElementById("qtd-concluidas").textContent = todos.filter(i => i.status === "concluida").length;
    document.getElementById("qtd-total").textContent = todos.length;

    atualizarLista("tarefa");
    atualizarLista("redacao");
}

function atualizarLista(tipo) {
    const container = document.getElementById(tipo === "tarefa" ? "lista-tarefas" : "lista-redacoes");
    const itens = usuario.atividades[tipo];

    if (!itens.length) {
        container.innerHTML = `<div class="p-4 text-center" style="color: var(--cor-texto-suave)">Nenhuma ${tipo === "tarefa" ? "tarefa cadastrada" : "redação salva"}</div>`;
        return;
    }

    container.innerHTML = itens.map(item => {
        const min = Math.floor(item.tempoRestante / 60);
        const seg = item.tempoRestante % 60;
        const tempo = `${min}:${seg.toString().padStart(2, "0")}`;

        return `
        <div class="card border-l-4" style="border-color: var(--cor-principal)">
            <div class="flex justify-between items-center flex-wrap gap-2">
                <div>
                    <span class="font-medium">${item.titulo}</span>
                    ${item.prazo ? `<span class="text-xs ml-2" style="color: var(--cor-texto-suave)">Prazo: ${new Date(item.prazo).toLocaleDateString("pt-BR")}</span>` : ""}
                </div>
                <span class="text-sm ${
                    item.status === "concluida" ? "text-sucesso" :
                    item.status === "pronto" ? "text-alerta" :
                    item.status === "andamento" ? "text-red-600" :
                    "text-neutro"
                }">
                    ${item.status === "pendente" ? "Aguardando" :
                      item.status === "andamento" ? tempo :
                      item.status === "pronto" ? "Finalizar" :
                      "Concluída"}
                </span>
            </div>
            ${item.descricao ? `<p class="text-sm mt-2" style="color: var(--cor-texto-suave)">${item.descricao}</p>` : ""}
            <div class="mt-3 flex justify-end gap-2">
                ${item.status === "pendente" ? `<button onclick="iniciarContagem('${tipo}', ${item.id})" class="btn-principal text-xs py-1.5 px-3">Começar</button>` : ""}
                ${item.status === "pronto" ? `<button onclick="concluirItem('${tipo}', ${item.id})" class="bg-sucesso hover:bg-green-600 text-white text-xs py-1.5 px-3 rounded">Confirmar</button>` : ""}
            </div>
        </div>`;
    }).join("");
}

// ---------------- SAIR E INICIALIZAÇÃO ----------------
function sair() {
    if (confirm("Deseja realmente sair?")) {
        clearInterval(sincronizacaoInterval);
        usuario = null;
        localStorage.removeItem("feizao_sessao");
        location.reload();
    }
}

window.onload = () => {
    const sessao = localStorage.getItem("feizao_sessao");
    if (sessao) {
        const { ra } = JSON.parse(sessao);
        const dados = localStorage.getItem(`feizao_${ra}`);
        if (dados) {
            usuario = JSON.parse(dados);
            abrirPainel();
            iniciarSync();
            carregarCoresSalvas();
        }
    }
};
</script>

</body>
</html>
