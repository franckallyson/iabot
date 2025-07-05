# 🤖 IABot



**IABot** é um chatbot inteligente desenvolvido para responder perguntas relacionadas ao tema **Inteligência Artificial (IA)**. Ele pode ser utilizado via terminal ou através de uma interface web. O projeto conta com um modelo treinável, testes automatizados e uma estrutura de fácil instalação.

---


## 📦 Requisitos

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/) [![ChatterBot](https://img.shields.io/badge/ChatterBot-1.2.7-blue?logo=pypi)](https://pypi.org/project/ChatterBot/) [![Flask](https://img.shields.io/badge/Flask-3.1.1-lightgrey?logo=flask)](https://flask.palletsprojects.com/) [![pytz](https://img.shields.io/badge/pytz-2025.2-green?logo=pypi)](https://pypi.org/project/pytz/) [![Node.js](https://img.shields.io/badge/Node.js-14+-green?logo=node.js)](https://nodejs.org/) [![Express](https://img.shields.io/badge/Express-4.17.1-black?logo=express)](https://expressjs.com/) [![Socket.io](https://img.shields.io/badge/socket.io-3.0.3-white?logo=socket.io)](https://socket.io/)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/franckallyson/iabot.git
cd iabot
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```


### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 4. Baixe o modelo de linguagem do spaCy

```bash
python -m spacy download en_core_web_sm
```

---

## 🧠 Treinamento do Chatbot

Antes de iniciar o treinamento, **verifique a constante `CONVERSAS` no arquivo `treinamento.py`**, certificando-se de que ela aponta corretamente para os arquivos `.json` com os exemplos de perguntas e respostas.

Após isso, execute o script de treinamento:

```bash
python treinamento.py
```

Esse passo treina o modelo para reconhecer e responder às perguntas definidas.

---

## 💬 Executando o Chatbot

### Interação via Terminal

```bash
python robo.py
```

### Interação via Web

#### 1. Inicie o backend

```bash
python servico.py
```

#### 2. Inicie o frontend (pasta `chat/`)

```bash
cd chat
npm install
npm start
```

> ⚠️ **Importante**: Verifique a porta em que o backend foi iniciado. Altere a constante `URL_IABOT` no arquivo `chat/index.js` se necessário.

---

## ✅ Testes Automatizados

Para rodar os testes automatizados:

```bash
python testes.py
```

---

## 📁 Estrutura do Projeto

```
.
├── chat/               # Frontend (React)
├── conversas/             # Dados de treinamento
├── robo.py             # Execução via terminal
├── servico.py          # Backend
├── treinamento.py      # Treinamento do modelo
├── testes.py           # Testes automatizados
├── requirements.txt    # Dependências Python
└── README.md           # Este arquivo
```

---

## 🧠 Sobre o IABot

O IABot foi criado com foco educacional, sendo uma ferramenta útil para estudantes, curiosos e entusiastas da inteligência artificial. Ele utiliza Chatterbot, NLP (Processamento de Linguagem Natural) com spaCy e outras bibliotecas populares em Python.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.




