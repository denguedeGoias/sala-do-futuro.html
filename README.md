<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#000000">
    <title>Sala do Futuro | Teste Funcional</title>
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='12' fill='%23000000'/%3E%3Ctext x='50' y='65' font-size='50' font-weight='bold' fill='%23E50914' text-anchor='middle'%3ESF%3C/text%3E%3C/svg%3E">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        preto: '#050505',
                        card: '#0F0F0F',
                        borda: '#1A1A1A',
                        vermelho: '#B00006',
                        sangue: '#E50914',
                        texto: '#F0F0F0',
                        cinza: '#888888'
                    },
                    fontFamily: {
                        sans: ['Segoe UI', 'Roboto', 'sans-serif']
                    }
                }
            }
        }
    </script>

    <style type="text/tailwindcss">
        @layer utilities {
            .conteudo {
                @apply max-w-5xl mx-auto px-4;
            }
            .card-estilo {
                @apply bg-card border border-borda rounded-xl border-t-2 border-vermelho;
            }
            .botao-vermelho {
                @apply bg-vermelho hover:bg-sangue text-white font-medium py-2 px-4 rounded-lg transition-colors disabled:opacity-40 disabled:cursor-not-allowed;
            }
            .input-estilo {
                @apply bg-card border border-borda text-texto rounded-lg px-3 py-2 w-full focus:outline-none focus:border-sangue;
            }
            .texto-sangue {
                @apply text-sangue font-semibold;
            }
            .barra-lateral {
                @apply w-1 bg-vermelho h-5 inline-block mr-2 rounded-sm;
            }
        }

        * {
            scrollbar-width: thin;
            scrollbar-color: #B00006 #050505;
        }
        html, body {
            @apply bg-preto text-texto min-h-screen;
        }
    </style>
</head>
<body>

<!-- TELA DE LOGIN -->
<div id="tela-login" class="min-h-screen flex flex-col justify-center">
    <div class="conteudo w-full max-w-sm">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-black texto-sangue">SALA DO FUTURO</h1>
            <p class="text-cinza text-sm mt-1">Ambiente de Teste e Desenvolvimento</p>
        </div>

        <div class="card-estilo p-5">
            <div id="aviso" class="bg-sangue/10 border border-sangue/30 text-sangue text-center text-sm p-2 rounded mb-4">
                Digite seu RA e senha para acessar
            </div>

            <div class="mb-4">
                <label class="text-cinza text-xs block mb-1">RA com dígito e UF</label>
                <input type="text" id="ra" class="input-estilo" placeholder="Ex: 123456789 0 SP">
            </div>

            <div class="mb-5">
                <label class="text-cinza text-xs block mb-1">Senha</label>
                <input type="password" id="senha" class="input-estilo" placeholder="Sua senha">
            </div>

            <button onclick="entrar()" id="botao-entrar" class="botao-vermelho w-full py-3">ENTRAR</button>
        </div>
    </div>
</div>

<!-- TELA PRINCIPAL -->
<div id="tela-principal" class="hidden min-h-screen">
    <!-- CABEÇALHO -->
    <header class="conteudo flex justify-between items-center py-4 border-b border-borda">
        <h2 class="text-xl font-bold texto-sangue">SALA DO FUTURO</h2>
        <div class="flex items-center gap-3">
            <span class="text-xs text-cinza">Modo de Teste Ativo</span>
            <button onclick="sair()" class="text-cinza hover:text-texto text-sm border border-borda px-3 py-1 rounded">Sair</button>
        </div>
    </header>

    <!-- RESUMO DO ALUNO -->
    <section class="conteudo mt-6">
        <div class="flex items-center gap-4">
            <div class="w-14 h-14 rounded-full bg-card border border-borda flex items-center justify-center texto-sangue text-xl font-bold" id="inicial-nome">A</div>
            <div>
                <h3 class="text-xl font-semibold">Olá, <span id="nome-aluno">Aluno</span></h3>
                <p class="text-cinza text-sm">RA: <span id="ra-mostrado">000000000</span></p>
            </div>
        </div>
    </section>

    <!-- CARDS DE INFORMAÇÕES -->
    <section class="conteudo mt-6 grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="card-estilo p-4">
            <div class="w-10 h-10 bg-vermelho rounded-lg flex items-center justify-center mb-3">
                <i class="fa fa-list text-white"></i>
            </div>
            <p class="text-2xl font-bold" id="qtd-pendentes">0</p>
            <p class="text-cinza text-sm">Atividades Pendentes</p>
        </div>

        <div class="card-estilo p-4">
            <div class="w-10 h-10 bg-vermelho rounded-lg flex items-center justify-center mb-3">
                <i class="fa fa-check text-white"></i>
            </div>
            <p class="text-2xl font-bold" id="qtd-concluidas">0</p>
            <p class="text-cinza text-sm">Concluídas</p>
        </div>

        <div class="card-estilo p-4">
            <div class="w-10 h-10 bg-vermelho rounded-lg flex items-center justify-center mb-3">
                <i class="fa fa-clock-o text-white"></i>
            </div>
            <p class="text-2xl font-bold" id="tempo-total">00:00</p>
            <p class="text-cinza text-sm">Tempo Gasto</p>
        </div>

        <div class="card-estilo p-4">
            <div class="w-10 h-10 bg-vermelho rounded-lg flex items-center justify-center mb-3">
                <i class="fa fa-percent text-white"></i>
            </div>
            <p class="text-2xl font-bold texto-sangue">100%</p>
            <p class="text-cinza text-sm">Desempenho</p>
        </div>
    </section>

    <!-- ÁREA DE NOVA ATIVIDADE -->
    <section class="conteudo mt-8">
        <div class="card-estilo p-5">
            <h3 class="text-lg font-semibold mb-4">
                <span class="barra-lateral"></span> Nova Atividade
            </h3>

            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div>
                    <label class="text-cinza text-xs block mb-1">Categoria</label>
                    <select id="categoria" class="input-estilo">
                        <option value="tarefa">📋 Tarefa Comum</option>
                        <option value="matific">➕ Matific</option>
                        <option value="alura">📘 Alura</option>
                        <option value="speak">🗣️ Speak</option>
                        <option value="redacao">✍️ Redação</option>
                    </select>
                </div>

                <div>
                    <label class="text-cinza text-xs block mb-1">Título / Assunto</label>
                    <input type="text" id="titulo" class="input-estilo" placeholder="Ex: Atividade de Matemática">
                </div>

                <div>
                    <label class="text-cinza text-xs block mb-1">Tempo (mínimo 1 minuto)</label>
                    <input type="number" id="tempo" min="1" value="1" class="input-estilo" placeholder="Minutos">
                </div>

                <div>
                    <label class="text-cinza text-xs block mb-1">Prazo</label>
                    <input type="date" id="prazo" class="input-estilo">
                </div>

                <div class="md:col-span-2 lg:col-span-4">
                    <label class="text-cinza text-xs block mb-1">Observações</label>
                    <textarea id="observacao" rows="2" class="input-estilo" placeholder="Detalhes adicionais..."></textarea>
                </div>

                <div class="lg:col-span-4">
                    <button onclick="adicionarAtividade()" class="botao-vermelho w-full py-2.5">Adicionar e Iniciar</button>
                </div>
            </div>
        </div>
    </section>

    <!-- LISTA DE ATIVIDADES -->
    <section class="conteudo mt-8 mb-12">
        <div class="card-estilo p-5">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-lg font-semibold">
                    <span class="barra-lateral"></span> Minhas Atividades
                </h3>
                <button onclick="atualizarLista()" class="text-cinza hover:text-texto text-sm border border-borda px-2 py-1 rounded">
                    <i class="fa fa-refresh mr-1"></i> Atualizar
                </button>
            </div>

            <div id="lista-atividades" class="space-y-4">
                <div class="text-center py-8 text-cinza">
                    Nenhuma atividade cadastrada ainda. Comece adicionando uma acima!
                </div>
            </div>
        </div>
    </section>
</div>

<!-- SCRIPT DE FUNCIONAMENTO -->
<script>
    // Configurações gerais
    const TEMPO_MINIMO = 60; // segundos
    let bancoDados = JSON.parse(localStorage.getItem("sala_futuro_teste") || "{}");

    // Inicializa o banco vazio se não existir
    if (!bancoDados.usuario) {
        bancoDados = {
            usuario: null,
            atividades: []
        };
        salvarDados();
    }

    // ------------------- LOGIN -------------------
    function entrar() {
        const ra = document.getElementById("ra").value.trim();
        const senha = document.getElementById("senha").value.trim();

        if (!ra || !senha) {
            document.getElementById("aviso").textContent = "Preencha todos os campos!";
            return;
        }

        // Para teste: aceita qualquer RA e senha válidos
        bancoDados.usuario = {
            ra: ra,
            nome: "Aluno " + ra.slice(0, 3),
            senha: senha
        };

        salvarDados();
        mostrarTelaPrincipal();
    }

    function mostrarTelaPrincipal() {
        document.getElementById("tela-login").classList.add("hidden");
        document.getElementById("tela-principal").classList.remove("hidden");

        document.getElementById("nome-aluno").textContent = bancoDados.usuario.nome;
        document.getElementById("ra-mostrado").textContent = bancoDados.usuario.ra;
        document.getElementById("inicial-nome").textContent = bancoDados.usuario.nome[0].toUpperCase();

        atualizarTela();
    }

    function sair() {
        if (confirm("Deseja realmente sair?")) {
            salvarDados();
            location.reload();
        }
    }

    // ------------------- GERENCIAMENTO DE ATIVIDADES -------------------
    function adicionarAtividade() {
        const categoria = document.getElementById("categoria").value;
        const titulo = document.getElementById("titulo").value.trim();
        const tempoMin = parseInt(document.getElementById("tempo").value);
        const prazo = document.getElementById("prazo").value || "Sem prazo";
        const observacao = document.getElementById("observacao").value;

        // Validação do tempo mínimo
        if (tempoMin < 1) {
            alert("⏱️ O tempo mínimo permitido é de 1 minuto!");
            return;
        }

        if (!titulo) {
            alert("Digite um título para a atividade!");
            return;
        }

        const tempoSeg = tempoMin * 60;

        const novaAtividade = {
            id: Date.now(),
            categoria: categoria,
            titulo: titulo,
            tempoTotal: tempoSeg,
            tempoRestante: tempoSeg,
            prazo: prazo,
            observacao: observacao,
            status: "pendente",
            inicio: null
        };

        bancoDados.atividades.push(novaAtividade);
        salvarDados();
        atualizarTela();

        // Limpa os campos
        document.getElementById("titulo").value = "";
        document.getElementById("tempo").value = "1";
        document.getElementById("prazo").value = "";
        document.getElementById("observacao").value = "";
    }

    function iniciarAtividade(id) {
        const atividade = bancoDados.atividades.find(a => a.id === id);
        if (!atividade || atividade.status !== "pendente") return;

        atividade.inicio = Date.now();
        atividade.status = "em andamento";
        salvarDados();

        // Inicia contagem regressiva
        const contador = setInterval(() => {
            const decorrido = Math.floor((Date.now() - atividade.inicio) / 1000);
            atividade.tempoRestante = Math.max(0, atividade.tempoTotal - decorrido);

            if (atividade.tempoRestante <= 0) {
                clearInterval(contador);
                atividade.status = "pronta";
            }

            salvarDados();
            atualizarLista();
        }, 1000);
    }

    function concluirAtividade(id) {
        const atividade = bancoDados.atividades.find(a => a.id === id);
        if (!atividade || atividade.status !== "pronta") return;

        atividade.status = "concluida";
        salvarDados();
        atualizarTela();
    }

    // ------------------- ATUALIZAÇÃO DA INTERFACE -------------------
    function atualizarTela() {
        const pendentes = bancoDados.atividades.filter(a => a.status === "pendente" || a.status === "em andamento").length;
        const concluidas = bancoDados.atividades.filter(a => a.status === "concluida").length;
        const tempoTotal = bancoDados.atividades.reduce((total, a) => total + (a.tempoTotal / 60), 0);

        document.getElementById("qtd-pendentes").textContent = pendentes;
        document.getElementById("qtd-concluidas").textContent = concluidas;
        document.getElementById("tempo-total").textContent = `${Math.floor(tempoTotal / 60)}h ${Math.round(tempoTotal % 60)}m`;

        atualizarLista();
    }

    function atualizarLista() {
        const lista = document.getElementById("lista-atividades");
        if (bancoDados.atividades.length === 0) {
            lista.innerHTML = `<div class="text-center py-8 text-cinza">Nenhuma atividade cadastrada ainda. Comece adicionando uma acima!</div>`;
            return;
        }

        lista.innerHTML = bancoDados.atividades.map(ativ => {
            const minutosRest = Math.floor(ativ.tempoRestante / 60);
            const segundosRest = ativ.tempoRestante % 60;
            const tempoTexto = `${minutosRest}:${segundosRest.toString().padStart(2, "0")}`;

            const icones = {
                tarefa: "📋",
                matific: "➕",
                alura: "📘",
                speak: "🗣️",
                redacao: "✍️"
            };

            const statusCor = {
                pendente: "text-cinza",
                "em andamento": "texto-sangue font-semibold",
                pronta: "text-yellow-400",
                concluida: "text-green-500"
            };

            const statusTexto = {
                pendente: "Aguardando",
                "em andamento": "Em execução",
                pronta: "Finalizar",
                concluida: "Concluída"
            };

            return `
            <div class="card-estilo p-4">
                <div class="flex flex-wrap justify-between items-center gap-3">
                    <div>
                        <span class="text-lg mr-2">${icones[ativ.categoria]}</span>
                        <span class="font-medium">${ativ.titulo}</span>
                        <span class="text-xs text-cinza ml-2">Prazo: ${ativ.prazo}</span>
                    </div>
                    <span class="${statusCor[ativ.status]} text-sm">${statusTexto[ativ.status]}</span>
                </div>

                <div class="mt-3 flex flex-wrap justify-between items-center border-t border-borda pt-3">
                    <div class="text-sm text-cinza">
                        Tempo definido: ${Math.round(ativ.tempoTotal / 60)} minuto(s)
                        ${ativ.status === "em andamento" ? ` • Restante: <span class="texto-sangue font-mono">${tempoTexto}</span>` : ""}
                    </div>

                    <div class="mt-2 md:mt-0">
                        ${ativ.status === "pendente" ?
                            `<button onclick="iniciarAtividade(${ativ.id})" class="botao-vermelho text-xs py-1.5 px-3">Começar</button>` : ""
                        }
                        ${ativ.status === "pronta" ?
                            `<button onclick="concluirAtividade(${ativ.id})" class="bg-green-600 hover:bg-green-700 text-white text-xs py-1.5 px-3 rounded">Confirmar Conclusão</button>` : ""
                        }
                        ${ativ.status === "concluida" ?
                            `<span class="text-xs text-green-500"><i class="fa fa-check mr-1"></i> Enviada com sucesso</span>` : ""
                        }
                    </div>
                </div>

                ${ativ.observacao ? `<div class="mt-2 text-xs text-cinza italic">Observação: ${ativ.observacao}</div>` : ""}
            </div>
            `;
        }).join("");
    }

    function salvarDados() {
        localStorage.setItem("sala_futuro_teste", JSON.stringify(bancoDados));
    }

    // Ao carregar a página
    window.onload = () => {
        if (bancoDados.usuario) {
            mostrarTelaPrincipal();
        }
    };
</script>

</body>
</html>

