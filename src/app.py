# app.py
import streamlit as st
from agente import carregar_dados, montar_contexto, perguntar

# Carrega dados
perfil, transacoes, historico, produtos = carregar_dados()

# Monta contexto
contexto = montar_contexto(perfil, transacoes, historico, produtos)

# Interface Streamlit
st.title("Tostão, seu guia financeiro")

if pergunta_texto := st.chat_input("Sua dúvida sobre suas finanças..."):
    st.chat_message("user").write(pergunta_texto)
    with st.spinner("..."):
        resposta = perguntar(pergunta_texto, contexto)
        st.chat_message("assistant").write(resposta)
