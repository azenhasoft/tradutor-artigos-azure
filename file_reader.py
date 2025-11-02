# Funções para extrair texto de arquivos PDF, DOCX e TXT
# Tudo que for enviado pelo usuário passa por aqui

import fitz  # PyMuPDF para PDF
import docx  # para arquivos .docx

def extrair_texto(arquivo):
    # Decide o tipo de arquivo e chama a função certa
    if arquivo.name.endswith(".pdf"):
        return extrair_pdf(arquivo)
    elif arquivo.name.endswith(".docx"):
        return extrair_docx(arquivo)
    else:
        return arquivo.read().decode("utf-8")  # texto puro

def extrair_pdf(arquivo):
    # Lê o PDF e junta o texto de todas as páginas
    doc = fitz.open(stream=arquivo.read(), filetype="pdf")
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

def extrair_docx(arquivo):
    # Lê o DOCX e junta os parágrafos
    doc = docx.Document(arquivo)
    return "\n".join([p.text for p in doc.paragraphs])
