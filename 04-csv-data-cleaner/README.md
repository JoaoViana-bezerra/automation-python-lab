# CSV Data Cleaner

Projeto em Python para limpar, padronizar e validar arquivos CSV, gerando uma base tratada e um relatório de qualidade dos dados.

## Objetivo

Demonstrar um processo de tratamento de dados aplicado a um cenário real:

```text
CSV bruto
   |
   v
Validação de estrutura
   |
   v
Remoção de duplicados
   |
   v
Padronização
   |
   v
Validação de campos
   |
   v
Correção de dados
   |
   v
CSV limpo
   +
Relatório de qualidade
```

O projeto faz parte do **Automation Python Lab** e demonstra competências em Python, Pandas e qualidade de dados.

## Stack

- Python
- Pandas
- CSV
- JSON
- Regular Expressions
- Logging
- Argparse

## Funcionalidades

- leitura de CSV
- validação de colunas obrigatórias
- remoção de duplicados
- padronização de nomes
- padronização de cidades
- normalização de estados
- normalização de status
- conversão de e-mails para minúsculas
- validação de e-mails
- limpeza de telefones
- formatação de telefones
- validação de telefones
- conversão e validação de datas
- tratamento de valores monetários brasileiros e internacionais
- correção de valores negativos
- tratamento de campos ausentes
- ordenação por ID
- geração de CSV limpo
- geração de relatório JSON de qualidade
- logs de execução

## Estrutura

```text
04-csv-data-cleaner/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── logger_config.py
│   ├── normalizers.py
│   ├── quality.py
│   ├── reporter.py
│   └── validators.py
│
├── input/
│   └── clientes_sujos.csv
│
├── output/
└── logs/
```

## Base de exemplo

O projeto inclui uma base propositalmente inconsistente:

```text
input/clientes_sujos.csv
```

Ela contém exemplos de problemas comuns:

- espaços extras
- letras maiúsculas e minúsculas inconsistentes
- e-mails inválidos
- telefones em formatos diferentes
- datas inválidas
- duplicidades
- campos vazios
- valores monetários em formatos diferentes
- valores negativos
- status não padronizados

## Entrada

Colunas esperadas:

```text
id
nome
email
telefone
cidade
estado
data_cadastro
valor_compras
status
```

## Saída

Após o processamento:

```text
output/
├── clientes_limpos.csv
└── relatorio_qualidade.json
```

## Exemplo de transformação

Entrada:

```text
"  ana lima  "
"ANA.LIMA@EMAIL.COM "
"(98) 99999-1001"
"sao luis"
"ma"
"1.250,50"
"ativo"
```

Saída:

```text
"Ana Lima"
"ana.lima@email.com"
"(98) 99999-1001"
"Sao Luis"
"MA"
1250.50
"Ativo"
```

## Relatório de qualidade

O JSON registra métricas como:

```json
{
  "input_rows": 13,
  "output_rows": 12,
  "removed_duplicates": 1,
  "invalid_emails": 1,
  "invalid_phones": 1,
  "invalid_dates": 1,
  "negative_values_corrected": 1
}
```

Os valores reais dependem da base processada.

## Instalação

Crie o ambiente virtual:

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
python main.py "C:\dados\clientes.csv"
```

Outro destino:

```bash
python main.py "C:\dados\clientes.csv" -o "C:\dados\clientes_limpos.csv"
```

Outro delimitador:

```bash
python main.py arquivo.csv --delimiter ","
```

Modo detalhado:

```bash
python main.py --verbose
```

## Arquitetura

```text
main.py
   |
   v
cleaner.py
   |
   +---- normalizers.py
   |
   +---- validators.py
   |
   +---- quality.py
   |
   +---- reporter.py
```

### `cleaner.py`

Coordena a limpeza dos dados.

### `normalizers.py`

Concentra regras de padronização.

### `validators.py`

Valida campos como e-mail e telefone.

### `quality.py`

Calcula métricas de qualidade.

### `reporter.py`

Exporta o relatório final.

## Competências demonstradas

Este projeto demonstra:

```text
Python
+
Pandas
+
Data Cleaning
+
Data Quality
+
Regex
+
CSV
+
JSON
+
Automação
```

## Próximas melhorias

- configuração por JSON
- regras de validação por coluna
- tratamento de CPF/CNPJ
- detecção de outliers
- relatório HTML
- testes automatizados
- interface gráfica
- processamento em lote
- integração com banco de dados

## Autor

João Viana

**Desenvolvimento de Software | Automação | Dados**
