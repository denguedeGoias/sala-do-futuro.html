import express from 'express';
import axios from 'axios';
import cors from 'cors';

const app = express();
const PORT = process.env.PORT || 3000;
const URL_BASE = "https://saladofuturo.educacao.sp.gov.br";

// Configurações básicas
app.use(cors());
app.use(express.json({ limit: '15mb' }));

// Rota de login
app.post('/api/login', async (req, res) => {
  try {
    const { ra, senha } = req.body;
    const resposta = await axios.post(`${URL_BASE}/api/login`, { ra, senha }, {
      timeout: 20000,
      headers: { 'Content-Type': 'application/json' }
    });
    res.json({ sucesso: true, dados: resposta.data });
  } catch (erro) {
    res.json({ sucesso: false, mensagem: erro.response?.data?.mensagem || "Falha na conexão" });
  }
});

// Rota para buscar tarefas
app.post('/api/tarefas', async (req, res) => {
  try {
    const { ra, senha } = req.body;
    const resposta = await axios.get(`${URL_BASE}/api/tarefas?ra=${ra}&senha=${senha}`, { timeout: 20000 });
    res.json({ sucesso: true, lista: resposta.data || [] });
  } catch {
    res.json({ sucesso: false, lista: [] });
  }
});

// Rota para buscar redações
app.post('/api/redacoes', async (req, res) => {
  try {
    const { ra, senha } = req.body;
    const resposta = await axios.get(`${URL_BASE}/api/redacao-paulista?ra=${ra}&senha=${senha}`, { timeout: 20000 });
    res.json({ sucesso: true, lista: resposta.data || [] });
  } catch {
    res.json({ sucesso: false, lista: [] });
  }
});

// Rota para enviar tarefa
app.post('/api/enviar-tarefa', async (req, res) => {
  try {
    const resposta = await axios.post(`${URL_BASE}/api/enviar-tarefa`, req.body, { timeout: 20000 });
    res.json({ sucesso: true, resposta: resposta.data });
  } catch {
    res.json({ sucesso: false });
  }
});

// Rota para enviar redação
app.post('/api/enviar-redacao', async (req, res) => {
  try {
    const resposta = await axios.post(`${URL_BASE}/api/enviar-redacao`, req.body, { timeout: 20000 });
    res.json({ sucesso: true, resposta: resposta.data });
  } catch {
    res.json({ sucesso: false });
  }
});

app.listen(PORT, () => console.log(`✅ Servidor intermediário rodando na porta ${PORT}`));
