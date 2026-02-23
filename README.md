# Projeto CRUD - Cadastro de contatos.
Projeto desenvolvido para a disciplina Software Product: Analysis, Specification, Project & Implementation com arquitetura em 3 camadas (Front-end, Back-end e Banco de Dados).

## Integrantes
Gabriel Joia Costa - RA: 2400853
Josafa Victor da Costa - RA: 2402270

## Tecnologias Utilizadas
- Python
- FLask
- MySQL
- HTML5
- CSS

# Estrutura do Projeto
Sprint1/
├── static/
├── templates/
├── .gitignore
├── appsp1.py
├── dbsp1.py
├── README.md
└── requirements.txt

## Pré-requisitos
Antes de executar, instale:
- Python 3.x
- MySQL Server
- pip

## Como executar o Projeto
1. Instalar dependências:
    pip install -r requirements.txt

2. Executar aplicação:
    python appsp1.py

3. Acessar no navegador:
    http://127.0.0.1:5000

## Configuração do Banco
1. Crie o banco no MySQL:
```sql
CREATE DATABASE projeto;

2. Crie a tabela:
CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    observacoes TEXT
);

3. Ajuste as credenciais em:
dbsp1.py