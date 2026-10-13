# Chatbot com IA

Aplicação web de chatbot desenvolvida em Python com Streamlit. A interface de chat mantém o histórico da conversa durante a sessão e envia as mensagens a um modelo de linguagem do Google Gemini, acessado por meio da biblioteca oficial da OpenAI através do endpoint compatível com a API da OpenAI.

## Visão geral

O projeto implementa um chat simples no navegador:

1. O usuário digita uma mensagem no campo de entrada.
2. A mensagem é exibida na tela e adicionada ao histórico da sessão.
3. O histórico completo é enviado ao modelo de IA, o que permite respostas com contexto das mensagens anteriores.
4. A resposta do modelo é exibida e também guardada no histórico.

## Tecnologias utilizadas

- Python 3
- [Streamlit](https://streamlit.io/): interface web e componentes de chat
- [OpenAI Python SDK](https://github.com/openai/openai-python): cliente para a API de chat completions
- [Google Gemini API](https://ai.google.dev/) via endpoint compatível com OpenAI


## Pré-requisitos

- Python 3
- Uma chave de API do Google Gemini, que pode ser gerada no Google AI Studio: https://aistudio.google.com/apikey

## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/angelomoraes/ChatBot-Python.git
cd ChatBot-Python
```

Instale as dependências:

```bash
pip install streamlit openai
```

## Configuração da chave de API

O código lê a chave a partir do mecanismo de segredos do Streamlit:

```python
API_KEY = st.secrets["API_KEY"]
```
Crie o arquivo `.streamlit/secrets.toml` na raiz do projeto com o seguinte conteúdo:

```toml
API_KEY = "sua-chave-de-api-aqui"
```

## Como executar

Na raiz do projeto, execute:

```bash
streamlit run main.py
```

O Streamlit abrirá a aplicação no navegador, normalmente em `http://localhost:8501`.
