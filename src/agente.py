# agente.py
import pandas as pd
import json
import requests
from config import OLLAMA_URL, MODELO

def carregar_dados():
    perfil = json.load(open('../data/perfil_investidor.json'))
    transacoes = pd.read_csv('../data/transacoes.csv')
    historico = pd.read_csv('../data/historico_atendimento.csv')
    produtos = json.load(open('../data/produtos_financeiros.json'))
    return perfil, transacoes, historico, produtos

def montar_contexto(perfil, transacoes, historico, produtos):
    contexto = f"""
    CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
    OBJETIVO: {perfil['objetivo_principal']}
    PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

    TRANSÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
    """
    return contexto

SYSTEM_PROMPT = """Você é o Tostão, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
1. NUNCA recomende investimentos específicos - apenas explique como funciona;
2. JAMAIS responda a perguntas fora do tema de ensino de finanças pessoais. Quando ocorrer, responda lembrando seu papel de educador financeiro;
3. Use os dados fornecidos para dar exemplos personalizados;
4. Linguagem simples;
5. Se não souber algo, admita: "Não tenho essa informação, mas posso te explicar...";
6. Responda de forma simples e direta.
"""

def perguntar(msg, contexto):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
    """

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json().get('response', "Erro ao obter resposta.")
