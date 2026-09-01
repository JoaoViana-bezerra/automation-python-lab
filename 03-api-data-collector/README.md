# API Data Collector

Projeto em Python para consumir a API REST pública do GitHub, coletar informações de repositórios, normalizar os dados e exportar os resultados em JSON, CSV e Excel.

## Objetivo

Demonstrar um fluxo real de integração com API:

```text
GitHub REST API
       |
       v
Requisição HTTP
       |
       v
JSON
       |
       v
Paginação
       |
       v
Normalização
       |
       v
Análise
       |
       v
JSON + CSV + Excel
```

O projeto foi desenvolvido como parte do **Automation Python Lab**, com foco em automação, integração entre sistemas e tratamento de dados.

## Stack

- Python
- Requests
- Pandas
- OpenPyXL
- GitHub REST API
- JSON
- CSV
- Logging
- Argparse

## Funcionalidades

- Consumo de API REST
- Requisições HTTP com `requests`
- Suporte a autenticação opcional
- Uso de variável de ambiente
- Paginação automática
- Tratamento de erros HTTP
- Retentativas automáticas
- Controle de rate limit
- Normalização de JSON
- Exclusão opcional de forks
- Ordenação por atualização
- Geração de resumo
- Contagem de linguagens
- Exportação para JSON
- Exportação para CSV
- Exportação para Excel
- Logs de execução

## Estrutura

```text
03-api-data-collector/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── analytics.py
│   ├── collector.py
│   ├── exporter.py
│   ├── http_client.py
│   └── logger_config.py
│
├── output/
└── logs/
```

## API utilizada

O projeto utiliza a API REST pública do GitHub.

Endpoint principal:

```text
GET /users/{username}/repos
```

Exemplo:

```text
GET /users/JoaoViana-bezerra/repos
```

## Dados coletados

Para cada repositório são extraídos campos como:

- ID
- Nome
- Nome completo
- Descrição
- URL
- Linguagem
- Visibilidade
- Fork
- Arquivado
- Branch padrão
- Stars
- Watchers
- Forks
- Issues abertas
- Tamanho
- Licença
- Data de criação
- Última atualização
- Último push
- Homepage
- Topics

## Instalação

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Por padrão o projeto consulta:

```text
JoaoViana-bezerra
```

Execute:

```bash
python main.py
```

Para consultar outro usuário:

```bash
python main.py microsoft
```

ou:

```bash
python main.py torvalds
```

## Formatos de saída

Todos:

```bash
python main.py JoaoViana-bezerra --format all
```

Somente JSON:

```bash
python main.py JoaoViana-bezerra --format json
```

Somente CSV:

```bash
python main.py JoaoViana-bezerra --format csv
```

Somente Excel:

```bash
python main.py JoaoViana-bezerra --format xlsx
```

## Incluir forks

Por padrão, forks não são incluídos.

Para incluí-los:

```bash
python main.py JoaoViana-bezerra --include-forks
```

## Diretório de saída

Padrão:

```text
output/
```

Outro diretório:

```bash
python main.py JoaoViana-bezerra -o "C:\relatorios\github"
```

## Arquivos gerados

Exemplo:

```text
output/
├── JoaoViana-bezerra_repositories.json
├── JoaoViana-bezerra_repositories.csv
└── JoaoViana-bezerra_repositories.xlsx
```

## Excel

O arquivo Excel possui:

```text
Repositorios
Resumo
Linguagens
```

### Resumo

Contém indicadores como:

- Total de repositórios
- Total de stars
- Total de forks
- Issues abertas
- Repositórios arquivados
- Linguagem mais utilizada

## Token opcional

A API do GitHub pode ser utilizada sem autenticação para consultas públicas.

Para aumentar o limite de requisições, é possível definir:

```text
GITHUB_TOKEN
```

Nunca salve tokens diretamente no código.

Exemplo no Windows PowerShell:

```powershell
$env:GITHUB_TOKEN="SEU_TOKEN"
python main.py
```

O arquivo `.env.example` é apenas uma referência e não contém credenciais.

## Arquitetura

```text
main.py
   |
   v
collector.py
   |
   v
http_client.py
   |
   v
GitHub REST API

collector.py
   |
   +---- analytics.py
   |
   +---- exporter.py
```

### `http_client.py`

Responsável pela comunicação HTTP, retries, headers, autenticação e rate limit.

### `collector.py`

Responsável pela paginação, coleta, filtros e normalização.

### `analytics.py`

Responsável pelos indicadores consolidados.

### `exporter.py`

Responsável pela geração dos arquivos JSON, CSV e Excel.

## Por que este projeto é relevante

Aplicações reais frequentemente precisam buscar informações em serviços externos.

Este projeto demonstra competências em:

```text
API REST
+
HTTP
+
JSON
+
Python
+
Tratamento de dados
+
Automação
+
Exportação
```

Também demonstra separação de responsabilidades e organização modular do código.

## Próximas melhorias

- Testes automatizados
- Cache local
- Coleta de commits
- Coleta de linguagens por repositório
- Coleta de contributors
- Processamento assíncrono
- Dashboard
- Banco de dados
- Agendamento automático
- Docker

## Autor

João Viana

**Desenvolvimento de Software | Automação | Dados**
