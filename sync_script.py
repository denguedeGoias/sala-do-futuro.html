#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Sincronização - Sala do Futuro
Sincroniza dados de alunos, tarefas, faltas e frequência
"""

import requests
import json
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional
import os

class SalaDFuturoSync:
    """Classe para sincronização de dados da Sala do Futuro"""
    
    def __init__(self, api_url: str, api_key: str, db_path: str = "sala_futuro.db"):
        """
        Inicializa o sincronizador
        
        Args:
            api_url: URL base da API (ex: https://sala-do-futuro.com/api)
            api_key: Chave de autenticação da API
            db_path: Caminho do banco de dados SQLite
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.db_path = db_path
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
        
        # Inicializa o banco de dados
        self._init_database()
    
    def _init_database(self):
        """Cria as tabelas do banco de dados se não existirem"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabela de Alunos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY,
                ra TEXT UNIQUE NOT NULL,
                nome TEXT NOT NULL,
                serie TEXT NOT NULL,
                email TEXT,
                ultima_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de Tarefas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY,
                ra TEXT NOT NULL,
                titulo TEXT NOT NULL,
                descricao TEXT,
                data_entrega DATE,
                status TEXT DEFAULT 'pendente',
                criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ra) REFERENCES alunos(ra)
            )
        ''')
        
        # Tabela de Redações
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS redacoes (
                id INTEGER PRIMARY KEY,
                ra TEXT NOT NULL,
                titulo TEXT NOT NULL,
                tema TEXT,
                data_entrega DATE,
                status TEXT DEFAULT 'pendente',
                nota REAL,
                criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ra) REFERENCES alunos(ra)
            )
        ''')
        
        # Tabela de Frequência
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS frequencia (
                id INTEGER PRIMARY KEY,
                ra TEXT NOT NULL,
                data_aula DATE NOT NULL,
                presente BOOLEAN DEFAULT TRUE,
                criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ra) REFERENCES alunos(ra)
            )
        ''')
        
        # Tabela de Resumo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resumo_aluno (
                id INTEGER PRIMARY KEY,
                ra TEXT UNIQUE NOT NULL,
                tarefas_pendentes INTEGER DEFAULT 0,
                redacoes_pendentes INTEGER DEFAULT 0,
                total_faltas INTEGER DEFAULT 0,
                porcentagem_frequencia REAL DEFAULT 0.0,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ra) REFERENCES alunos(ra)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def _fazer_requisicao(self, endpoint: str, metodo: str = 'GET', dados: Dict = None) -> Optional[Dict]:
        """
        Faz uma requisição à API
        
        Args:
            endpoint: Endpoint da API (ex: /alunos)
            metodo: Método HTTP
            dados: Dados para POST/PUT
            
        Returns:
            Resposta JSON ou None se falhar
        """
        try:
            url = f"{self.api_url}{endpoint}"
            
            if metodo == 'GET':
                response = self.session.get(url, timeout=10)
            elif metodo == 'POST':
                response = self.session.post(url, json=dados, timeout=10)
            elif metodo == 'PUT':
                response = self.session.put(url, json=dados, timeout=10)
            else:
                raise ValueError(f"Método HTTP não suportado: {metodo}")
            
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro na requisição {endpoint}: {e}")
            return None
    
    def sincronizar_alunos(self):
        """Sincroniza lista de alunos da API"""
        print("🔄 Sincronizando alunos...")
        
        dados = self._fazer_requisicao('/alunos')
        if not dados:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            for aluno in dados.get('alunos', []):
                cursor.execute('''
                    INSERT OR REPLACE INTO alunos (ra, nome, serie, email)
                    VALUES (?, ?, ?, ?)
                ''', (
                    aluno['ra'],
                    aluno['nome'],
                    aluno['serie'],
                    aluno.get('email', '')
                ))
            
            conn.commit()
            print(f"✅ {len(dados.get('alunos', []))} alunos sincronizados")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao sincronizar alunos: {e}")
            return False
        finally:
            conn.close()
    
    def sincronizar_tarefas(self):
        """Sincroniza tarefas pendentes"""
        print("🔄 Sincronizando tarefas...")
        
        dados = self._fazer_requisicao('/tarefas/pendentes')
        if not dados:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            for tarefa in dados.get('tarefas', []):
                cursor.execute('''
                    INSERT OR REPLACE INTO tarefas (ra, titulo, descricao, data_entrega, status)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    tarefa['ra'],
                    tarefa['titulo'],
                    tarefa.get('descricao', ''),
                    tarefa.get('data_entrega'),
                    tarefa.get('status', 'pendente')
                ))
            
            conn.commit()
            print(f"✅ {len(dados.get('tarefas', []))} tarefas sincronizadas")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao sincronizar tarefas: {e}")
            return False
        finally:
            conn.close()
    
    def sincronizar_redacoes(self):
        """Sincroniza redações pendentes"""
        print("🔄 Sincronizando redações...")
        
        dados = self._fazer_requisicao('/redacoes/pendentes')
        if not dados:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            for redacao in dados.get('redacoes', []):
                cursor.execute('''
                    INSERT OR REPLACE INTO redacoes (ra, titulo, tema, data_entrega, status, nota)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    redacao['ra'],
                    redacao['titulo'],
                    redacao.get('tema', ''),
                    redacao.get('data_entrega'),
                    redacao.get('status', 'pendente'),
                    redacao.get('nota')
                ))
            
            conn.commit()
            print(f"✅ {len(dados.get('redacoes', []))} redações sincronizadas")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao sincronizar redações: {e}")
            return False
        finally:
            conn.close()
    
    def sincronizar_frequencia(self):
        """Sincroniza dados de frequência"""
        print("🔄 Sincronizando frequência...")
        
        dados = self._fazer_requisicao('/frequencia')
        if not dados:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            for registro in dados.get('frequencia', []):
                cursor.execute('''
                    INSERT OR IGNORE INTO frequencia (ra, data_aula, presente)
                    VALUES (?, ?, ?)
                ''', (
                    registro['ra'],
                    registro['data_aula'],
                    registro.get('presente', True)
                ))
            
            conn.commit()
            print(f"✅ {len(dados.get('frequencia', []))} registros de frequência sincronizados")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao sincronizar frequência: {e}")
            return False
        finally:
            conn.close()
    
    def calcular_resumo_alunos(self):
        """Calcula o resumo de cada aluno"""
        print("📊 Calculando resumo dos alunos...")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # Obtém todos os RAs
            cursor.execute('SELECT DISTINCT ra FROM alunos')
            alunos = cursor.fetchall()
            
            for (ra,) in alunos:
                # Conta tarefas pendentes
                cursor.execute(
                    'SELECT COUNT(*) FROM tarefas WHERE ra = ? AND status = ?',
                    (ra, 'pendente')
                )
                tarefas_pendentes = cursor.fetchone()[0]
                
                # Conta redações pendentes
                cursor.execute(
                    'SELECT COUNT(*) FROM redacoes WHERE ra = ? AND status = ?',
                    (ra, 'pendente')
                )
                redacoes_pendentes = cursor.fetchone()[0]
                
                # Conta faltas
                cursor.execute(
                    'SELECT COUNT(*) FROM frequencia WHERE ra = ? AND presente = ?',
                    (ra, False)
                )
                total_faltas = cursor.fetchone()[0]
                
                # Calcula porcentagem de frequência
                cursor.execute(
                    'SELECT COUNT(*) FROM frequencia WHERE ra = ?',
                    (ra,)
                )
                total_aulas = cursor.fetchone()[0]
                
                if total_aulas > 0:
                    porcentagem_frequencia = ((total_aulas - total_faltas) / total_aulas) * 100
                else:
                    porcentagem_frequencia = 0.0
                
                # Insere ou atualiza resumo
                cursor.execute('''
                    INSERT OR REPLACE INTO resumo_aluno 
                    (ra, tarefas_pendentes, redacoes_pendentes, total_faltas, porcentagem_frequencia)
                    VALUES (?, ?, ?, ?, ?)
                ''', (ra, tarefas_pendentes, redacoes_pendentes, total_faltas, porcentagem_frequencia))
            
            conn.commit()
            print(f"✅ Resumo de {len(alunos)} alunos calculado")
            return True
        
        except Exception as e:
            print(f"❌ Erro ao calcular resumo: {e}")
            return False
        finally:
            conn.close()
    
    def gerar_relatorio(self, ra: str = None) -> str:
        """
        Gera relatório em JSON
        
        Args:
            ra: RA do aluno (None para todos)
            
        Returns:
            String JSON formatada
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            relatorio = {
                'data_geracao': datetime.now().isoformat(),
                'alunos': []
            }
            
            if ra:
                query = 'SELECT * FROM alunos WHERE ra = ?'
                cursor.execute(query, (ra,))
            else:
                query = 'SELECT * FROM alunos'
                cursor.execute(query)
            
            alunos_list = cursor.fetchall()
            
            for aluno in alunos_list:
                aluno_id, aluno_ra, nome, serie, email, _ = aluno
                
                # Busca resumo
                cursor.execute(
                    'SELECT * FROM resumo_aluno WHERE ra = ?',
                    (aluno_ra,)
                )
                resumo = cursor.fetchone()
                
                # Busca tarefas
                cursor.execute(
                    'SELECT titulo, data_entrega, status FROM tarefas WHERE ra = ? AND status = ?',
                    (aluno_ra, 'pendente')
                )
                tarefas = [{'titulo': t[0], 'data_entrega': t[1], 'status': t[2]} for t in cursor.fetchall()]
                
                # Busca redações
                cursor.execute(
                    'SELECT titulo, data_entrega, status FROM redacoes WHERE ra = ? AND status = ?',
                    (aluno_ra, 'pendente')
                )
                redacoes = [{'titulo': r[0], 'data_entrega': r[1], 'status': r[2]} for r in cursor.fetchall()]
                
                aluno_data = {
                    'ra': aluno_ra,
                    'nome': nome,
                    'serie': serie,
                    'email': email,
                    'tarefas_pendentes': resumo[2] if resumo else 0,
                    'redacoes_pendentes': resumo[3] if resumo else 0,
                    'total_faltas': resumo[4] if resumo else 0,
                    'porcentagem_frequencia': round(resumo[5], 2) if resumo else 0.0,
                    'tarefas': tarefas,
                    'redacoes': redacoes
                }
                
                relatorio['alunos'].append(aluno_data)
            
            return json.dumps(relatorio, ensure_ascii=False, indent=2)
        
        finally:
            conn.close()
    
    def sincronizar_tudo(self):
        """Sincroniza todos os dados"""
        print("\n" + "="*50)
        print("🚀 INICIANDO SINCRONIZAÇÃO COMPLETA")
        print("="*50 + "\n")
        
        sucesso = True
        sucesso &= self.sincronizar_alunos()
        sucesso &= self.sincronizar_tarefas()
        sucesso &= self.sincronizar_redacoes()
        sucesso &= self.sincronizar_frequencia()
        sucesso &= self.calcular_resumo_alunos()
        
        if sucesso:
            print("\n✅ SINCRONIZAÇÃO CONCLUÍDA COM SUCESSO!\n")
        else:
            print("\n⚠️ SINCRONIZAÇÃO CONCLUÍDA COM ERROS!\n")
        
        return sucesso


def main():
    """Função principal"""
    
    # ⚙️ CONFIGURE AQUI:
    API_URL = "https://seu-servidor.com/api"  # Altere para sua URL
    API_KEY = "sua_chave_api_aqui"  # Altere para sua chave
    
    # Cria a instância do sincronizador
    sync = SalaDFuturoSync(API_URL, API_KEY)
    
    # Sincroniza tudo
    sync.sincronizar_tudo()
    
    # Gera e salva relatório
    relatorio = sync.gerar_relatorio()
    
    with open('relatorio_alunos.json', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print("📄 Relatório salvo em: relatorio_alunos.json")
    print("\n" + relatorio)


if __name__ == "__main__":
    main()
