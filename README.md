# Tradutor de artigos técnicos com Azure Translator

Este é um protótipo em Python com uma interface Streamlit. Ele recebe um PDF, DOCX ou TXT, extrai o texto e envia o conteúdo ao Azure Translator. O resultado aparece na tela.

O usuário escolhe o idioma de destino entre português, inglês, espanhol, francês e alemão. O projeto não guarda o histórico das traduções.

## Como executar

Requer Python e uma conta com acesso ao Azure Translator.

Crie e ative um ambiente virtual. No Windows, usando PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Configure estas variáveis de ambiente antes de iniciar o aplicativo:

- `AZURE_TRANSLATOR_KEY`: chave do recurso;
- `AZURE_TRANSLATOR_ENDPOINT`: endpoint do recurso.

No PowerShell:

```powershell
$env:AZURE_TRANSLATOR_KEY = "sua-chave"
$env:AZURE_TRANSLATOR_ENDPOINT = "endpoint-do-seu-recurso"
streamlit run app.py
```

No Linux ou macOS:

```bash
export AZURE_TRANSLATOR_KEY="sua-chave"
export AZURE_TRANSLATOR_ENDPOINT="endpoint-do-seu-recurso"
streamlit run app.py
```

Não coloque a chave no código nem a envie para o GitHub. O arquivo `.gitignore` do projeto ignora arquivos `.env`, mas o aplicativo lê as configurações diretamente das variáveis de ambiente.

## O que ainda falta

O protótipo não tem testes automatizados nem tratamento próprio para falhas de conexão com o serviço. Também não permite escolher o idioma de origem.

Como o texto dos arquivos é enviado ao Azure para tradução, use apenas documentos que você tem autorização para processar dessa forma.