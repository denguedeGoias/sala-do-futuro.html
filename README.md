<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#050505">
<title>Sala do Futuro | SED</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='18' fill='%23050505'/%3E%3Ctext x='50' y='68' font-size='62' font-weight='900' fill='%23E50914' text-anchor='middle'%3ESF%3C/text%3E%3C/svg%3E">
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
    :root{
        --preto:#050505;--card:#111111;--borda:#1C1C1C;
        --vermelho:#B8000A;--sangue:#E50914;
        --texto:#EAEAEA;--cinza:#8A8A8A
    }
    *{margin:0;padding:0;box-sizing:border-box;scrollbar-width:thin;scrollbar-color:var(--vermelho) var(--preto)}
    html,body{background:var(--preto);color:var(--texto);font-family:system-ui,sans-serif;min-height:100vh}
    .card{background:var(--card);border:1px solid var(--borda);border-radius:14px;border-top:2.5px solid var(--vermelho)}
    .linhaV{height:22px;width:3px;background:var(--vermelho);display:inline-block;margin-right:8px;border-radius:2px}
    .input{background:var(--card);border:1px solid var(--borda);color:#fff;border-radius:10px;padding:12px 14px;width:100%;outline:none}
    .input:focus{border-color:var(--sangue);box-shadow:0 0 0 2px rgba(229,9,20,0.2)}
    .btnV{background:var(--vermelho);color:#fff;padding:12px;border-radius:10px;font-weight:600;width:100%;border:none;cursor:pointer;transition:background .2s}
    .btnV:hover{background:var(--sangue)}.btnV:disabled{opacity:.4;cursor:not-allowed}
    .stPend{color:#ff5252}.stFaz{color:#ffb74d}.stOk{color:#66bb6a}.bloq{opacity:.5;pointer-events:none}
    .icone{width:44px;height:44px;background:var(--vermelho);border-radius:10px;display:grid;place-items:center}
    .item{background:#090909;border:1px solid var(--borda);border-radius:10px;padding:10px 12px;margin-bottom:8px}
    .off{display:none !important}.cron{color:var(--sangue);font-weight:700;font-family:monospace}
    .aviso{padding:8px 12px;border-radius:8px;margin:8px 0;text-align:center;font-size:13px}
    .aviso.erro{background:rgba(229,9,20,0.15);border:1px solid rgba(229,9,20,0.3);color:#ff8888}
    .aviso.info{background:rgba(255,183,77,0.15);border:1px solid rgba(255,183,77,0.3);color:#ffd270}
</style>
</head>
<body class="min-h-screen">

<!-- TELA DE LOGIN -->
<div id="login" class="min-h-screen grid place-items-center px-4">
    <div class="w-full max-w-sm">
        <div class="text-center mb-8">
            <h1 style="color:var(--sangue);font-size:34px;font-weight:900">SALA DO FUTURO</h1>
            <p class="text-xs mt-1" style="color:var(--cinza)">Secretaria da Educação • SED</p>
        </div>
        <div class="card p-5">
            <div id="avisoLogin" class="aviso info mb-3">Digite seu RA e senha da SED para entrar</div>
            
            <label class="text-xs block mb-1" style="color:var(--cinza)">RA COM DÍGITO E UF</label>
            <input id="ra" class="input mb-3" placeholder="Ex: 123456789 0 SP" maxlength="15">
            
            <label class="text-xs block mb-1" style="color:var(--cinza)">SENHA DA SED</label>
            <input id="senha" type="password" class="input mb-4" placeholder="Mesma senha do portal sed.educacao.sp.gov.br">
            
            <button onclick="fazerLogin()" id="btnEntrar" class="btnV">ENTRAR</button>
            <p class="text-center text-xs mt-3" style="color:var(--cinza)">Se não conectar, entra no modo de uso local</p>
        </div>
    </div>
</div>

<!-- PAINEL PRINCIPAL -->
<div id="painel" class="off">
    <header class="px-4 pt-5 pb-3 flex items-center justify-between max-w-5xl mx-auto">
        <span style="color:var(--sangue);font-weight:800;font-size:18px">SALA DO FUTURO</span>
        <div class="flex items-center gap-2">
            <span id="stsSync" class="text-xs" style="color:var(--cinza)"><i class="fa-solid fa-circle-check mr-1"></i>Modo Local</span>
            <button onclick="sair()" class="text-xs px-3 py-1.5 rounded" style="border:1px solid var(--borda);color:var(--cinza);background:transparent">Sair</button>
        </div>
    </header>

    <div class="max-w-5xl mx-auto px-4 py-4">
        <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full grid place-items-center font-bold text-xl" style="background:var(--card);border:1px solid var(--borda);color:var(--sangue)" id="letraNome">A</div>
            <div>
                <h1 class="text-xl font-bold">Olá, <span id="nomeAluno">Aluno</span></h1>
                <p class="text-sm" style="color:var(--cinza)">RA: <span id="raMostra">00000000</span> • <span id="turmaAluno">Turma 3ºA</span></p>
            </div>
        </div>
    </div>

    <!-- CARDS RESUMO -->
    <div class="max-w-5xl mx-auto px-4 grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-check"></i></div>
            <div class="text-3xl font-extrabold" id="pend">0</div><div class="text-sm" style="color:var(--cinza)">Pendências</div></div>
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-envelope"></i></div>
            <div class="text-3xl font-extrabold" id="msg">0</div><div class="text-sm" style="color:var(--cinza)">Avisos</div></div>
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-calendar-xmark"></i></div>
            <div class="text-3xl font-extrabold" id="faltas">0</div><div class="text-sm" style="color:var(--cinza)">Faltas</div></div>
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-chart-line"></i></div>
            <div class="text-3xl font-extrabold" id="freq" style="color:#66bb6a">100%</div>
            <div class="text-sm" style="color:var(--cinza)">Frequência</div></div>
    </div>

    <!-- CRIAR ATIVIDADE -->
    <div class="max-w-5xl mx-auto px-4 mt-6">
        <div class="card p-4">
            <div class="mb-4"><span class="linhaV"></span><b class="text-base">📝 NOVA ATIVIDADE</b>
            <span class="text-xs ml-2" style="color:var(--cinza)">⏱️ Tempo mínimo: 60 segundos</span></div>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-3">
                <select id="tipo" class="input">
                    <option value="tarefa">📋 Tarefa Comum</option>
                    <option value="matific">➕ Matific</option>
                    <option value="alura">📘 Alura</option>
                    <option value="speak">🗣️ Speak</option>
                    <option value="redacao">✍️ Redação</option>
                </select>
                <input id="titulo" class="input" placeholder="Título da atividade">
                <input id="prazo" type="date" class="input">
                <input id="info" class="input" placeholder="Nota / % / Tempo">
                <textarea id="obs" rows="1" class="input md:col-span-4" placeholder="Observações adicionais..."></textarea>
                <button onclick="cadastrarAtividade()" class="btnV md:col-span-4">CADASTRAR ATIVIDADE</button>
            </div>
        </div>
    </div>

    <!-- LISTA DE ATIVIDADES -->
    <div class="max-w-5xl mx-auto px-4 mt-6 pb-10">
        <div class="card p-4">
            <div class="mb-4"><span class="linhaV"></span><b class="text-base">📅 SUAS ATIVIDADES</b></div>
            <div id="listaAtividades" class="space-y-3">
                <div class="text-center text-sm py-6" style="color:var(--cinza)">Nenhuma atividade cadastrada ainda</div>
            </div>
        </div>
    </div>
</div>

<script>
// Configurações gerais
const MIN_TEMPO = 60000; // 1 minuto em milissegundos
const TIPOS_ATIV = {
    tarefa: { nome: "📋 Tarefa", cor: "#4285F4" },
    matific: { nome: "➕ Matific", cor: "#34A853" },
    alura: { nome: "📘 Alura", cor: "#9C27B0" },
    speak: { nome: "🗣️ Speak", cor: "#FF9800" },
    redacao: { nome: "✍️ Redação", cor: "#00BCD4" }
};

// Banco de dados local
let banco = JSON.parse(localStorage.getItem("sala_futuro_db") || "{}");
if (!banco.atividades) {
    banco = {
        usuario: null,
        atividades: [],
        faltas: 0,
        frequencia: 100,
        mensagens: 1
    };
    salvarDados();
}

// Função de login
async function fazerLogin() {
    const ra = document.getElementById("ra").value.trim();
    const senha = document.getElementById("senha").value;
    const aviso = document.getElementById("avisoLogin");
    const botao = document.getElementById("btnEntrar");

    if (!ra || !senha) {
        aviso.className = "aviso erro";
        aviso.textContent = "⚠️ Preencha RA e senha!";
        return;
    }

    botao.disabled = true;
    aviso.className = "aviso info";
    aviso.textContent = "🔄 Tentando conectar com a SED...";

    try {
        // Simula conexão segura
        await new Promise(resolve => setTimeout(resolve, 1200));
        
        // Se não conectar ao servidor, cria usuário local
        banco.usuario = {
            ra: ra.replace(/\D/g, ""),
            nome: "Aluno " + ra.substring(0, 3),
            turma: "3ª Série A",
            senha: senha
        };
        salvarDados();

        aviso.className = "aviso";
        aviso.textContent = "✅ Entrando no modo de uso seguro!";
        setTimeout(abrirPainel, 800);

    } catch (erro) {
        aviso.className = "aviso info";
        aviso.textContent = "ℹ️ Entrando no modo local (funciona tudo)";
        
        banco.usuario = {
            ra: ra.replace(/\D/g, ""),
            nome: "Aluno",
            turma: "Turma A",
            senha: senha
        };
        salvarDados();
        setTimeout(abrirPainel, 800);
    } finally {
        botao.disabled = false;
    }
}

function abrirPainel() {
    document.getElementById("login").classList.add("off");
    document.getElementById("painel").classList.remove("off");
    atualizarTela();
}

function atualizarTela() {
    const usr = banco.usuario;
    document.getElementById("nomeAluno").textContent = usr.nome;
    document.getElementById("raMostra").textContent = usr.ra;
    document.getElementById("turmaAluno").textContent = usr.turma;
    document.getElementById("letraNome").textContent = usr.nome[0].toUpperCase();
    
    document.getElementById("pend").textContent = banco.atividades.filter(a => a.status !== "concluido").length;
    document.getElementById("msg").textContent = banco.mensagens;
    document.getElementById("faltas").textContent = banco.faltas;
    document.getElementById("freq").textContent = banco.frequencia + "%";

    listarAtividades();
}

function cadastrarAtividade() {
    const tipo = document.getElementById("tipo").value;
    const titulo = document.getElementById("titulo").value.trim();
    const prazo = document.getElementById("prazo").value || "Sem prazo";
    const info = document.getElementById("info").value || "";
    const obs = document.getElementById("obs").value || "";

    if (!titulo) {
        alert("⚠️ Escreva o título da atividade!");
        return;
    }

    const nova = {
        id: Date.now(),
        tipo: tipo,
        titulo: titulo,
        prazo: prazo,
        info: info,
        obs: obs,
        inicio: Date.now(),
        tempoRestante: MIN_TEMPO,
        status: "pendente"
    };

    banco.atividades.push(nova);
    salvarDados();
    atualizarTela();
    iniciarCronometro(nova.id);

    document.getElementById("titulo").value = "";
    document.getElementById("prazo").value = "";
    document.getElementById("info").value = "";
    document.getElementById("obs").value = "";
}

function iniciarCronometro(id) {
    const ativ = banco.atividades.find(a => a.id === id);
    if (!ativ || ativ.status === "concluido") return;

    const contador = setInterval(() => {
        const decorrido = Date.now() - ativ.inicio;
        ativ.tempoRestante = Math.max(0, MIN_TEMPO - decorrido);

        if (ativ.tempoRestante <= 0) {
            clearInterval(contador);
            ativ.status = "pronta";
        }

        salvarDados();
        listarAtividades();
    }, 1000);
}

function listarAtividades() {
    const container = document.getElementById("listaAtividades");
    if (banco.atividades.length === 0) {
        container.innerHTML = `<div class="text-center text-sm py-6" style="color:var(--cinza)">Nenhuma atividade cadastrada ainda</div>`;
        return;
    }

    container.innerHTML = banco.atividades.map(ativ => {
        const minutos = Math.floor(ativ.tempoRestante / 60000);
        const segundos = Math.floor((ativ.tempoRestante % 60000) / 1000);
        const tempo = `${minutos}:${segundos.toString().padStart(2, "0")}`;

        return `
        <div class="item">
            <div class="flex flex-wrap justify-between items-center gap-2">
                <div>
                    <span style="color:${TIPOS_ATIV[ativ.tipo].cor};font-weight:600">${TIPOS_ATIV[ativ.tipo].nome}</span>
                    <span class="ml-2">${ativ.titulo}</span>
                </div>
                <span class="text-xs" style="color:var(--cinza)">Prazo: ${ativ.prazo}</span>
            </div>
            <div class="flex justify-between items-center mt-2">
                <span class="text-sm">${ativ.info || "Sem observação"}</span>
                ${ativ.status === "pendente" ? 
                    `<span class="cron">⏱️ ${tempo}</span>` : 
                    `<button onclick="mudarStatus(${ativ.id})" class="btnV text-xs py-1 px-3 w-auto">${ativ.status === "pronta" ? "Concluir" : "Concluída"}</button>`
                }
            </div>
        </div>`;
    }).join("");
}

function mudarStatus(id) {
    const ativ = banco.atividades.find(a => a.id === id);
    if (!ativ || ativ.status !== "pronta") return;

    ativ.status = "concluido";
    salvarDados();
    atualizarTela();
}

function salvarDados() {
    localStorage.setItem("sala_futuro_db", JSON.stringify(banco));
}

function sair() {
    banco.usuario = null;
    salvarDados();
    location.reload();
}

// Inicializa cronômetros das atividades já salvas
window.onload = () => {
    banco.atividades.filter(a => a.status === "pendente").forEach(ativ => iniciarCronometro(ativ.id));
};
</script>
</body>
</html>
