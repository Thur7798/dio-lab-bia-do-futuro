import json
import pandas as pd
import os
import requests 
import streamlit as st

# CONFIGURAÇÃO
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODELO = "mistral:latest"


# CARREGAR DADOS
base_path = os.path.join(os.path.dirname(__file__), "..", "data")

perfil = json.load(open(os.path.join(base_path, "perfil_investidor.json")))
produtos = json.load(open(os.path.join(base_path, "produtos_financeiros.json")))
transacoes = pd.read_csv(os.path.join(base_path, "transacoes.csv"))
historico = pd.read_csv(os.path.join(base_path, "historico_atendimento.csv"))

# MONTAR CONTEXTO

contexto = f"""
    CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
    OBJETIVO: {perfil['objetivo_principal']}
    PATRIMÔNIO: R$ {perfil["patrimonio_total"]} | RESERVA: R$ {perfil["reserva_emergencia_atual"]}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT

SYSTEM_PROMPT = """Você é um agente financeiro inteligente especializado em educação financeira para iniciantes.
Seu objetivo é ajudar usuários a entender conceitos básicos de finanças pessoais, como reserva de emergência, orçamento e tipos de investimentos, sem dar recomendações específicas.

REGRAS:

Sempre baseie suas respostas nos dados fornecidos (perfil, transações, histórico).

Nunca invente informações financeiras ou valores.

Se não souber algo, admita e ofereça alternativas de aprendizado.

Use linguagem simples e acessível, sem jargões técnicos.

Não faça recomendações de produtos ou investimentos sem contexto do perfil.

Sempre incentive o usuário a aprender e ganhar autonomia.

"""

# CHAMAR OLLAMA

def perguntar(msg):
    try:
        prompt = f"""
        {SYSTEM_PROMPT}

        CONTEXTO DO CLIENTE:
        {contexto}

        Pergunta: {msg}"""

        r = requests.post(OLLAMA_URL, json={"model" : MODELO, "prompt": prompt, "stream": False})
        data = r.json()
        return data.get("response", f"Erro na resposta do Ollama: {data}")
    except Exception as e:
        return f"Falha na requisição ao Ollama : {e}"


# INTERFACE

st.title("ArielFIN, Seu educador financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
