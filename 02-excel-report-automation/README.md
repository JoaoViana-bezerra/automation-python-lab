# Excel Report Automation

Automação em Python para transformar uma planilha bruta de vendas em um relatório Excel estruturado, com limpeza de dados, indicadores, rankings e gráficos.

## Objetivo

Demonstrar um fluxo prático de automação empresarial:

```text
Planilha bruta
      |
      v
Validação
      |
      v
Limpeza e padronização
      |
      v
Cálculos
      |
      v
Indicadores e rankings
      |
      v
Relatório Excel final
```

## Stack

- Python
- Pandas
- OpenPyXL
- Argparse
- Logging

## Funcionalidades

- leitura de `.xlsx`
- validação de colunas
- remoção de duplicados
- tratamento de nulos
- normalização de datas
- padronização de textos
- tratamento de números
- cálculo de receita bruta
- cálculo de desconto
- cálculo de receita líquida
- indicadores executivos
- ranking de vendedores
- ranking de produtos
- análise por região
- evolução mensal
- múltiplas abas
- formatação automática
- gráficos no Excel
- logs de execução

## Estrutura

```text
02-excel-report-automation/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── analytics.py
│   ├── cleaner.py
│   ├── exporter.py
│   ├── logger_config.py
│   └── pipeline.py
├── input/
│   └── vendas_exemplo.xlsx
├── output/
└── logs/
```

## Entrada

A aba `Vendas` possui:

`Pedido`, `Data`, `Vendedor`, `Região`, `Cliente`, `Produto`, `Categoria`, `Quantidade`, `Preço Unitário`, `Desconto %` e `Status`.

Uma base fictícia já está incluída em:

```text
input/vendas_exemplo.xlsx
```

## Saída

O relatório final possui:

- `Resumo`
- `Dados Tratados`
- `Vendedores`
- `Produtos`
- `Regiões`
- `Mensal`

### KPIs

- Total de Pedidos
- Pedidos Concluídos
- Pedidos Pendentes
- Pedidos Cancelados
- Receita Bruta
- Descontos Concedidos
- Receita Líquida
- Ticket Médio

## Instalação

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

## Executar

Com a base de exemplo:

```bash
python main.py
```

Saída:

```text
output/relatorio_vendas.xlsx
```

Outro arquivo:

```bash
python main.py "C:\dados\vendas.xlsx"
```

Outro destino:

```bash
python main.py "C:\dados\vendas.xlsx" -o "C:\relatorios\relatorio.xlsx"
```

Outra aba:

```bash
python main.py "C:\dados\vendas.xlsx" --sheet "Base Vendas"
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
   +---- cleaner.py
   +---- analytics.py
   +---- exporter.py
   +---- logger_config.py
```

A separação por módulos facilita manutenção, testes e evolução do projeto.

## Próximas melhorias

- dashboard executivo
- processamento em lote
- configuração via JSON
- envio automático por e-mail
- integração com APIs
- exportação para PDF
- testes automatizados
- agendamento
- interface gráfica

## Autor

João Viana

**Desenvolvimento de Software | Automação | Dados**
