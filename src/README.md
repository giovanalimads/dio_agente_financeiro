# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Antes de começar

Este agente usa o OLLAMA. Será necessário instalar e ativar primeiro antes de executar o agente. Este projeto depende do Ollama rodando localmente.

### Instalação do Ollama
https://ollama.com/download

Após instalar, o comando ollama deve funcionar no terminal:
```bash
ollama --version
```

### Subir o serviço

```bash
ollama serve
```

Inicia um servidor HTTP. Escuta por padrão na porta 11434 e fica rodando em background

### Baixar o modelo
Com o serviço rodando, você baixa o modelo:
```bash
ollama pull gpt-oss:20b-cloud
```

Faz download do modelo e salva localmente. Dependendo de sua conexão, pode demorar.

## Como Rodar o agente

```bash
# Instalar dependências
pip install -r requirements.txt
```

# Rodar a aplicação
```
streamlit run app.py
```
