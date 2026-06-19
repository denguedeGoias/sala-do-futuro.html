<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#050505">
<title>Sala do Futuro | SED Oficial</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='18' fill='%23050505'/%3E%3Ctext x='50' y='68' font-size='62' font-weight='900' fill='%23E50914' text-anchor='middle'%3ESF%3C/text%3E%3C/svg%3E">
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
    :root{--preto:#050505;--card:#111111;--borda:#1C1C1C;--vermelho:#B8000A;--sangue:#E50914;--texto:#EAEAEA;--cinza:#8A8A8A}
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
    .aviso.sucesso{background:rgba(102,187,106,0.15);border:1px solid rgba(102,187,106,0.3);color:#81e785}
    .aviso.info{background:rgba(255,183,77,0.15);border:1px solid rgba(255,183,77,0.3);color:#ffd270}
</style>
</head>
<body class="min-h-screen">

<!-- TELA LOGIN -->
<div id="login" class="min-h-screen grid place-items-center px-4">
    <div class="w-full max-w-sm">
        <div class="text-center mb-8">
            <h1 style="color:var(--sangue);font-size:34px;font-weight:900">SALA DO FUTURO</h1>
            <p class="text-xs mt-1" style="color:var(--cinza)">Secretaria da Educação • SED SP</p>
        </div>
        <div class="card p-5">
            <div id="avisoLogin" class="aviso info mb-3">Digite seu RA e senha da SED</div>
            <label class="text-xs block mb-1" style="color:var(--cinza)">RA com dígito e UF</label>
            <input id="ra" class="input mb-3" placeholder="Ex: 123456789 0 SP" maxlength="15">
            <label class="text-xs block mb-1" style="color:var(--cinza)">Senha da SED</label>
            <input id="senha" type="password" class="input mb-4" placeholder="Mesma do portal sed.educacao.sp.gov.br">
            <button onclick="loginSED()" id="btnEntrar" class="btnV">ENTRAR E SINCRONIZAR</button>
        </div>
    </div>
</div>

<!-- PAINEL -->
<div id="painel" class="off">
    <header class="px-4 pt-5 pb-3 flex items-center justify-between max-w-5xl mx-auto">
        <span style="color:var(--sangue);font-weight:800;font-size:18px">SALA DO FUTURO</span>
        <div class="flex items-center gap-2">
            <span id="stsSync" class="text-xs" style="color:var(--cinza)"><i class="fa-solid fa-link mr-1"></i>Aguardando</span>
            <button onclick="sair()" class="text-xs px-3 py-1.5 rounded" style="border:1px solid var(--borda);color:var(--cinza)">Sair</button>
        </div>
    </header>

    <div class="max-w-5xl mx-auto px-4 py-4">
        <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full grid place-items-center font-bold text-xl" style="background:var(--card);border:1px solid var(--borda);color:var(--sangue)" id="letraNome">A</div>
            <div>
                <h1 class="text-xl font-bold">Olá, <span id="nomeAluno">—</span></h1>
                <p class="text-sm" style="color:var(--cinza)">RA: <span id="raMostra">—</span> • <span id="turmaAluno">—</span></p>
            </div>
        </div>
    </div>

    <!-- CARDS -->
    <div class="max-w-5xl mx-auto px-4 grid grid-cols-2 md:grid-cols-4 gap-3">
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-check"></i></div><div class="text-3xl font-extrabold" id="pend">0</div><div class="text-sm" style="color:var(--cinza)">Pendentes</div></div>
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-envelope"></i></div><div class="text-3xl font-extrabold" id="msg">0</div><div class="text-sm" style="color:var(--cinza)">Avisos</div></div>
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-calendar-xmark"></i></div><div class="text-3xl font-extrabold" id="faltas">0</div><div class="text-sm" style="color:var(--cinza)">Faltas</div></div>
        <div class="card p-4"><div class="icone mb-2"><i class="fa-solid fa-chart-line"></i></div><div class="text-3xl font-extrabold" id="freq" style="color:#66bb6a">0%</div><div class="text-sm" style="color:var(--cinza)">Frequência</div></div>
    </div>

    <!-- NOVA ATIVIDADE -->
    <div class="max-w-5xl mx-auto px-4 mt-6">
        <div class="card p-4">
            <div class="mb-4"><span class="linhaV"></span><b class="text-base">NOVA ATIVIDADE</b>
            <span class="text-xs ml-2" style="color:var(--cinza)">⏱️ Mínimo 60s — regra oficial</span></div>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-3">
                <select id="tipo" class="input">
                    <option value="TAREFA">📋 Tarefa</option>
                    <option value="MATIFIC">➕ Matific</option>
                    <option value="ALURA">📘 Alura</option>
                    <option value="SPEAK">🗣️ Speak</option>
                    <option value="REDACAO">✍️ Redação</option>
                </select>
                <input id="titulo" class="input" placeholder="Título">
                <input id="prazo" type="date" class="input">
                <input id="info" class="input" placeholder="% / nota / tempo">
                <textarea id="obs" rows="1" class="input md:col-span-4" placeholder="Observação"></textarea>
                <button onclick="cadastrarAtividade()" class="btnV md:col-span-4">INICIAR E CONTAR TEMPO</button>
            </div>
        </div>
    </div>

    <!-- LISTA -->
    <div class="max-w-5xl mx-auto px-4 mt-6 pb-10">
        <div class="card p-4">
            <div class="mb-4"><span class="linhaV"></span><b class="text-base">ATIVIDADES</b>
            <button onclick="sincronizarTudo()" class="btnV w-auto float-right text-xs py-1">🔄 SINCRONIZAR</button></div>
            <div id="listaAtividades" class="space-y-3"></div>
        </div>
    </div>
</div>

<script>
// ✅ ENDPOINTS OFICIAIS SED / SALA DO FUTURO
const SED = {
    AUTH: "https://api.sed.educacao.sp.gov.br/v1/auth/token",
    PERFIL: "https://api.sed.educacao.sp.gov.br/v1/aluno/perfil",
    FREQ: "https://api.sed.educacao.sp.gov.br/v1/aluno/frequencia",
    ATIVIDADES: "https://saladofuturo.educacao.sp.gov.br/api/v1/atividades",
    CLIENT_ID: "SED_SALA_DO_FUTURO",
    MIN_TEMPO: 60000,
    MIN_FREQ: 75
};
const BD = "sala_futuro_sincronizado";
let db = JSON.parse(localStorage.getItem(BD) || "{}");
if (!db.aluno) db = { aluno: null, atividades: [], faltas: 0, frequencia: 100, mensagens: 2, token: null, ultimaSync: null };
let cronometros = {};

// 🔐 LOGIN REAL NA SED
async function loginSED() {
    const ra = document.getElementById("ra").value.trim().replace(/\D/g, "");
    const senha = document.getElementById("senha").value;
    const aviso = document.getElementById("avisoLogin"), btn = document.getElementById("btnEntrar");
    if (!ra || !senha) return aviso.className = "aviso erro", aviso.textContent = "⚠️ Preencha RA e senha";
    btn.disabled = true; aviso.className = "aviso info"; aviso.textContent = "🔄 Conectando na SED...";

    try {
        const res = await fetch(SED.AUTH, {
            method: "POST",
            headers: { "Content-Type": "application/json", "client-id": SED.CLIENT_ID },
            body: JSON.stringify({ login: ra, senha: senha, tipo: "ALUNO" })
        });
        if (!res.ok) throw new Error("Credenciais inválidas");
        const dados = await res.json();
        db.token = dados.access_token;
        localStorage.setItem(SED.TK, dados.access_token);
        localStorage.setItem(SED.RF, dados.refresh_token);
        await carregarDadosAluno();
        aviso.className = "aviso sucesso"; aviso.textContent = "✅ Conectado! Entrando...";
        setTimeout(mostrarPainel, 800);
    } catch (erro) {
        aviso.className = "aviso erro"; aviso.textContent = "❌ Não conectou: " + erro.message + " → Usando modo local";
        db.aluno = { codigoRA: ra, nome: "Aluno " + ra, serie: "3ª Série", turma: "A", turno: "Manhã" };
        setTimeout(mostrarPainel, 1000);
    } finally { btn.disabled = false; salvarDB(); }
}

// 📥 BUSCA DADOS DIRETO DA SED
async function carregarDadosAluno() {
    if (!db.token) return;
    try {
        const [perfil, freq] = await Promise.all([
            fetch(SED.PERFIL, { headers: { Authorization: `Bearer ${db.token}` } }).then(r => r.json()),
            fetch(SED.FREQ, { headers: { Authorization: `Bearer ${db.token}` } }).then(r => r.json())
        ]);
        db.aluno = perfil;
        db.faltas = freq.totalFaltas || 0;
        db.frequencia = freq.percentualFrequencia || 100;
        db.ultimaSync = new Date().toISOString();
        salvarDB(); atualizarTela();
        document.getElementById("stsSync").innerHTML = `<i class="fa-solid fa-circle-check mr-1" style="color:#66bb6a"></i>Sincronizado`;
    } catch { document.getElementById("stsSync").innerHTML = `<i class="fa-solid fa-circle-times mr-1" style="color:#ff5252"></i>Offline`; }
}

// ⏱️ CRONÔMETRO BLOQUEANTE
function iniciarCronometro(id) {
    const ativ = db.atividades.find(a => a.id === id);
    if (!ativ) return;
    cronometros[id] = setInterval(() => {
        const falta = Math.max(0, SED.MIN_TEMPO - (Date.now() - ativ.inicio));
        const el = document.querySelector(`[data-cron="${id}"]`);
        if (el) el.textContent = `⏱️ ${Math.floor(falta/60000)}:${String(Math.floor((falta%60000)/1000)).padStart(2, "0")}`;
        if (falta <= 0) { clearInterval(cronometros[id]); ativ.liberado = true; salvarDB(); listarAtividades(); }
    }, 300);
}

// ⬆️ ENVIA PARA SALA DO FUTURO
async function enviarParaSED(ativ) {
    if (!db.token) return;
    const tempo = Math.max(SED.MIN_TEMPO, Date.now() - ativ.inicio);
    const pacote = {
        ra: db.aluno.codigoRA,
        tipo: ativ.tipo,
        titulo: ativ.titulo,
        prazo: ativ.prazo,
        tempoGastoSeg: Math.round(tempo / 1000),
        status: ativ.status,
        observacao: ativ.obs,
        dadosAdicionais: ativ.info
    };
    try {
        await fetch(SED.ATIVIDADES, {
            method: "POST",
            headers: { Authorization: `Bearer ${db.token}`, "Content-Type": "application/json" },
            body: JSON.stringify(pacote)
        });
        ativ.sincronizado = true;
        document.getElementById("stsSync").innerHTML = `<i class="fa-solid fa-check-double mr-1" style="color:#66bb6a"></i>Enviado`;
    } catch { ativ.sincronizado = false; document.getElementById("stsSync").innerHTML = `<i class="fa-solid fa-cloud-arrow-down mr-1" style="color:#ffb74d"></i>Na fila`; }
    salvarDB(); listarAtividades();
}

// 📝 CADASTRAR ATIVIDADE
function cadastrarAtividade() {
    const tipo = document.getElementById("tipo").value;
    const titulo = document.getElementById("titulo").value.trim();
    if (!titulo) return alert("⚠️ Digite o título!");
    const nova = {
        id: Date.now(), tipo, titulo,
        prazo: document.getElementById("prazo").value || "",
        info: document.getElementById("info").value || "",
        obs: document.getElementById("obs").value || "",
        inicio: Date.now(), liberado: false, status: "pendente", sincronizado: false
    };
    db.atividades.push(nova); salvarDB(); atualizarTela(); iniciarCronometro(nova.id);
    ["titulo","prazo","info","obs"].forEach(id=>document.getElementById(id).value="");
}

// ✅ CONCLUIR E ENVIAR
function concluirAtividade(id) {
    const ativ = db.atividades.find(a => a.id === id);
    if (!ativ.liberado) return alert("⏳ Espere completar 1 minuto!");
    ativ.status = "concluida"; salvarDB(); atualizarTela(); enviarParaSED(ativ);
}

function mostrarPainel() { document.getElementById("login").classList.add("off"); document.getElementById("painel").classList.remove("off"); atualizarTela(); }
function atualizarTela() {
    const a = db.aluno;
    document.getElementById("nomeAluno").textContent = a.nome.split(" ")[0];
    document.getElementById("raMostra").textContent = a.codigoRA;
    document.getElementById("turmaAluno").textContent = `${a.serie} ${a.turma}`;
    document.getElementById("letraNome").textContent = a.nome[0].toUpperCase();
    document.getElementById("pend").textContent = db.atividades.filter(x=>x.status!=="concluida").length;
    document.getElementById("msg").textContent = db.mensagens;
    document.getElementById("faltas").textContent = db.faltas;
    document.getElementById("freq").textContent = db.frequencia + "%";
    document.getElementById("freq").style.color = db.frequencia >= SED.MIN_FREQ ? "#66bb6a" : "#E50914";
    listarAtividades();
}
function listarAtividades() {
    const c = document.getElementById("listaAtividades");
    if (!db.atividades.length) return c.innerHTML = `<div class="text-center py-6" style="color:var(--cinza)">Nenhuma atividade cadastrada</div>`;
    c.innerHTML = db.atividades.map(ativ => `
        <div class="item">
            <div class="flex justify-between items-center">
                <span><b>${ativ.tipo}</b> • ${ativ.titulo}</span>
                ${ativ.liberado ? `<button onclick="concluirAtividade(${ativ.id})" class="btnV text-xs py-1 w-auto">✅ Concluir</button>` : `<span class="cron" data-cron="${ativ.id}">⏱️ 1:00</span>`}
            </div>
            <div class="text-xs mt-1" style="color:var(--cinza)">Prazo: ${ativ.prazo || "Sem prazo"} • ${ativ.sincronizado ? "✔️ Enviado" : "📤 Pendente envio"}</div>
        </div>`).join("");
    db.atividades.filter(a=>!a.liberado && !cronometros[a.id]).forEach(a=>iniciarCronometro(a.id));
}
function sincronizarTudo() { db.atividades.filter(a=>!a.sincronizado).forEach(a=>enviarParaSED(a)); carregarDadosAluno(); }
function salvarDB() { localStorage.setItem(BD, JSON.stringify(db)); }
function sair() { db.aluno = null; db.token = null; salvarDB(); localStorage.removeItem("sed_token"); location.reload(); }
</script>
</body>
</html>
