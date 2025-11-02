# Função que chama a API do Azure Translator
# Precisa da chave e do endpoint configurados via variável de ambiente

import requests
import os

def traduzir_texto(texto, idioma_destino="pt"):
    chave = os.getenv("AZURE_TRANSLATOR_KEY")  # chave da API
    endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")  # endpoint da API
    url = f"{endpoint}/translate?api-version=3.0&to={idioma_destino}"

    headers = {
        'Ocp-Apim-Subscription-Key': chave,
        'Content-Type': 'application/json'
    }

    body = [{'text': texto}]  # corpo da requisição

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()  # se der erro, levanta exceção

    # retorna só o texto traduzido
    return response.json()[0]['translations'][0]['text']
