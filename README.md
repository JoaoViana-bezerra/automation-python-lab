# Automation Python Lab

Coleção de projetos práticos em Python com foco em **automação de processos, tratamento de dados, integração com APIs e geração de relatórios**.

O objetivo deste repositório é demonstrar aplicações reais de Python em cenários de produtividade, dados e integração entre sistemas.

---

## Visão geral

```text
automation-python-lab/
│
├── 01-file-organizer/
├── 02-excel-report-automation/
├── 03-api-data-collector/
├── 04-csv-data-cleaner/
├── 05-report-generator/
│
└── README.md
```

Cada projeto foi estruturado de forma independente, com documentação própria, código modular e instruções de execução.

---

## Projetos

### 01 — File Organizer

Automação para organizar arquivos automaticamente por categoria.

**Principais funcionalidades**
- classificação por extensão
- criação automática de pastas
- prevenção contra sobrescrita
- renomeação de arquivos duplicados
- modo `--dry-run`
- modo recursivo
- logs de execução

**Tecnologias**

`Python` `pathlib` `shutil` `argparse` `logging`

**Fluxo**

```text
Pasta com arquivos
       |
       v
Leitura
       |
       v
Identificação da extensão
       |
       v
Classificação
       |
       v
Movimentação automática
```

[Ver projeto](./01-file-organizer)

---

### 02 — Excel Report Automation

Automação para transformar uma planilha bruta de vendas em um relatório Excel estruturado.

**Principais funcionalidades**
- leitura de Excel
- validação de colunas
- limpeza e padronização
- cálculo de indicadores
- ranking de vendedores
- ranking de produtos
- análise regional
- evolução mensal
- gráficos no Excel

**Tecnologias**

`Python` `Pandas` `OpenPyXL`

**Fluxo**

```text
Excel bruto
    |
    v
Limpeza
    |
    v
Tratamento
    |
    v
Indicadores
    |
    v
Relatório Excel
```

[Ver projeto](./02-excel-report-automation)

---

### 03 — API Data Collector

Integração com a API REST do GitHub para coleta, tratamento e exportação de dados de repositórios.

**Principais funcionalidades**
- consumo de API REST
- requisições HTTP
- paginação automática
- retries
- tratamento de erros
- controle de rate limit
- autenticação opcional via token
- normalização de JSON
- exportação para JSON, CSV e Excel

**Tecnologias**

`Python` `Requests` `Pandas` `OpenPyXL` `REST API` `JSON`

**Fluxo**

```text
GitHub REST API
       |
       v
HTTP Request
       |
       v
JSON
       |
       v
Normalização
       |
       v
JSON + CSV + Excel
```

[Ver projeto](./03-api-data-collector)

---

### 04 — CSV Data Cleaner

Pipeline de limpeza, padronização e validação de arquivos CSV.

**Principais funcionalidades**
- remoção de duplicados
- tratamento de campos vazios
- padronização de nomes
- validação de e-mail
- normalização de telefone
- validação de datas
- tratamento monetário
- correção de valores inválidos
- relatório de qualidade em JSON

**Tecnologias**

`Python` `Pandas` `Regex` `CSV` `JSON`

**Fluxo**

```text
CSV bruto
   |
   v
Validação
   |
   v
Data Cleaning
   |
   v
Padronização
   |
   v
CSV limpo
   +
Relatório de qualidade
```

[Ver projeto](./04-csv-data-cleaner)

---

### 05 — Report Generator

Geração automática de relatórios executivos em PDF e HTML a partir de dados tratados.

**Principais funcionalidades**
- cálculo de KPIs
- análise de vendas
- ranking de vendedores
- ranking de produtos
- evolução mensal
- gráficos automáticos
- dashboard HTML
- relatório PDF paginado

**Tecnologias**

`Python` `Pandas` `Matplotlib` `ReportLab` `HTML` `CSS`

**Fluxo**

```text
Dados tratados
      |
      v
Análise
      |
      v
KPIs
      |
      v
Visualizações
      |
      v
PDF + HTML
```

[Ver projeto](./05-report-generator)

---

## Stack utilizada

### Linguagem

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" alt="Python" title="Python">
</p>

### Bibliotecas e tecnologias

- Pandas
- OpenPyXL
- Requests
- Matplotlib
- ReportLab
- JSON
- CSV
- REST APIs
- Regular Expressions
- Logging
- Argparse

### Ferramentas

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="42" alt="Git" title="Git">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="42" alt="GitHub" title="GitHub">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="42" alt="VS Code" title="VS Code">
</p>

---

## Competências demonstradas

Este laboratório foi estruturado para demonstrar competências em:

```text
Python
+
Automação
+
Manipulação de arquivos
+
Tratamento de dados
+
APIs REST
+
Integração entre sistemas
+
Excel
+
CSV
+
JSON
+
Visualização de dados
+
Geração de relatórios
+
Arquitetura modular
```

---

## Evolução dos projetos

Os projetos seguem uma progressão técnica:

| Etapa | Projeto | Foco |
|---|---|---|
| 01 | File Organizer | Automação de arquivos |
| 02 | Excel Report Automation | Excel e tratamento de dados |
| 03 | API Data Collector | APIs e integração |
| 04 | CSV Data Cleaner | Data Cleaning e qualidade |
| 05 | Report Generator | Análise e geração de relatórios |

---

## Arquitetura e boas práticas

Ao longo dos projetos são aplicados conceitos como:

- separação de responsabilidades
- modularização
- funções reutilizáveis
- tratamento de exceções
- logs
- configuração por linha de comando
- ambientes virtuais
- dependências controladas
- documentação
- arquivos `.gitignore`
- variáveis de ambiente
- validação de entrada
- organização de código

---

## Como executar os projetos

Clone o repositório:

```bash
git clone https://github.com/JoaoViana-bezerra/automation-python-lab.git
```

Entre na pasta:

```bash
cd automation-python-lab
```

Escolha um projeto:

```bash
cd 02-excel-report-automation
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

Consulte o `README.md` de cada projeto para instruções específicas.

---

## Estrutura recomendada do repositório

```text
automation-python-lab/
│
├── 01-file-organizer/
│   ├── main.py
│   ├── README.md
│   └── ...
│
├── 02-excel-report-automation/
│   ├── main.py
│   ├── src/
│   ├── README.md
│   └── ...
│
├── 03-api-data-collector/
│   ├── main.py
│   ├── src/
│   ├── README.md
│   └── ...
│
├── 04-csv-data-cleaner/
│   ├── main.py
│   ├── src/
│   ├── README.md
│   └── ...
│
├── 05-report-generator/
│   ├── main.py
│   ├── src/
│   ├── README.md
│   └── ...
│
└── README.md
```

---

## Próximos projetos

O laboratório pode evoluir com novas automações como:

- envio automático de e-mails
- integração com banco de dados
- Web Scraping
- processamento em lote
- automação de documentos
- integração com Google Sheets
- agendamentos
- dashboards interativos
- ETL
- Docker
- testes automatizados

---

## Sobre o projeto

Este repositório faz parte do meu portfólio profissional e tem como objetivo demonstrar aplicações práticas de Python em problemas reais.

Meu foco está na construção de soluções que combinem:

**Desenvolvimento de Software | Automação | Dados**

---

## Contato

<p>
  <a href="https://www.linkedin.com/in/jo%C3%A3o-viana-0b6096246/">
    <img src="https://img.shields.io/badge/LinkedIn-João%20Viana-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>

  <a href="">
    <img src="https://img.shields.io/badge/Email-Contato-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail">
  </a>

  <a href="https://github.com/JoaoViana-bezerra">
    <img src="https://img.shields.io/badge/GitHub-JoaoViana--bezerra-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

---

<p align="center">
  <strong>Automação aplicada a problemas reais.</strong>
</p>
