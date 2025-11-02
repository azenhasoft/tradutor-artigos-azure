# Interface principal com Streamlit
# Aqui o usuário envia o arquivo e escolhe o idioma da tradução

import streamlit as st
from file_reader import extrair_texto
from azure_translator import traduzir_texto

st.title("🧠 Tradutor de Artigos Técnicos com Azure AI")

# Upload do arquivo
arquivo = st.file_uploader("Envie seu artigo técnico", type=["pdf", "docx", "txt"])

# Idioma de destino (padrão: português)
idioma = st.selectbox("Idioma de destino", ["pt", "en", "es", "fr", "de"])

# Quando o usuário clicar em traduzir
if arquivo and st.button("Traduzir"):
    texto = extrair_texto(arquivo)  # extrai o texto do arquivo
    traducao = traduzir_texto(texto, idioma)  # envia pra API do Azure
    st.subheader("Tradução:")
    st.text_area("Resultado", traducao, height=400)  # mostra o resultado
