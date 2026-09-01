# Report Generator

Projeto em Python para transformar dados tratados em um relatório executivo profissional, com KPIs, gráficos, rankings e exportação para **PDF e HTML**.

## Objetivo

Esta etapa fecha o fluxo iniciado nos projetos anteriores do Automation Python Lab:

```text
Dados brutos
    |
    v
Limpeza / tratamento
    |
    v
Análise
    |
    v
Indicadores
    |
    v
Visualizações
    |
    v
Relatório executivo
    |
    +---- PDF
    |
    +---- HTML
```

O objetivo é demonstrar como Python pode automatizar não apenas o tratamento dos dados, mas também a apresentação final das informações.

## Stack

- Python
- Pandas
- Matplotlib
- ReportLab
- HTML/CSS
- CSV
- Logging
- Argparse

## Funcionalidades

- leitura de CSV tratado
- validação de estrutura
- cálculo de KPIs
- análise de pedidos por status
- receita líquida
- ticket médio
- quantidade de itens vendidos
- ranking de vendedores
- ranking de produtos
- análise por região
- evolução mensal
- geração automática de gráficos
- geração de relatório HTML responsivo
- geração de relatório PDF
- paginação no PDF
- tabelas formatadas
- logs de execução
- parâmetros via linha de comando

## Estrutura

```text
05-report-generator/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── charts.py
│   ├── html_report.py
│   ├── logger_config.py
│   ├── pdf_report.py
│   └── pipeline.py
│
├── input/
│   └── vendas_tratadas.csv
│
├── output/
└── logs/
```

## Entrada

O projeto inclui uma base fictícia pronta para teste:

```text
input/vendas_tratadas.csv
```

Colunas esperadas:

```text
pedido
data
vendedor
regiao
produto
categoria
quantidade
receita_liquida
status
```

## KPIs

O relatório calcula:

- Total de pedidos
- Pedidos concluídos
- Pedidos pendentes
- Pedidos cancelados
- Receita líquida
- Ticket médio
- Itens vendidos

## Visualizações

São criados automaticamente:

### Receita por vendedor

Gráfico horizontal mostrando o desempenho dos vendedores.

### Evolução mensal

Gráfico de linha demonstrando a evolução da receita ao longo dos meses.

## Saídas

Ao executar:

```bash
python main.py
```

serão gerados:

```text
output/
├── relatorio_executivo.html
├── relatorio_executivo.pdf
└── assets/
    ├── receita_vendedores.png
    └── evolucao_mensal.png
```

## Instalação

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instale:

```bash
pip install -r requirements.txt
```

## Executar

Com a base de exemplo:

```bash
python main.py
```

Outro arquivo:

```bash
python main.py "C:\dados\vendas_tratadas.csv"
```

Somente PDF:

```bash
python main.py --format pdf
```

Somente HTML:

```bash
python main.py --format html
```

Alterar o título:

```bash
python main.py --title "Relatório Comercial - 2026"
```

Outro diretório:

```bash
python main.py -o "C:\relatorios"
```

Logs detalhados:

```bash
python main.py --verbose
```

## Arquitetura

```text
main.py
   |
   v
pipeline.py
   |
   +---- analyzer.py
   |
   +---- charts.py
   |
   +---- html_report.py
   |
   +---- pdf_report.py
   |
   +---- logger_config.py
```

### `analyzer.py`

Valida a base e cria indicadores e agregações.

### `charts.py`

Produz as visualizações com Matplotlib.

### `html_report.py`

Monta um dashboard HTML responsivo.

### `pdf_report.py`

Gera um documento PDF paginado utilizando ReportLab.

### `pipeline.py`

Orquestra todo o fluxo.

## Competências demonstradas

```text
Python
+
Pandas
+
Data Analysis
+
Data Visualization
+
Automação
+
HTML
+
PDF
+
Arquitetura modular
```

## Relação com as etapas anteriores

O Automation Python Lab passa a demonstrar um fluxo completo:

```text
01 File Organizer
        |
02 Excel Report Automation
        |
03 API Data Collector
        |
04 CSV Data Cleaner
        |
05 Report Generator
```

## Próximas melhorias

- template configurável
- logotipo no relatório
- gráficos adicionais
- comparação entre períodos
- envio automático por e-mail
- armazenamento em nuvem
- dashboard interativo
- integração com banco de dados
- agendamento
- testes automatizados

## Autor

João Viana

**Desenvolvimento de Software | Automação | Dados**
