# File Organizer

Automação em Python para organizar arquivos automaticamente em pastas por categoria, com suporte a simulação, logs, tratamento de conflitos de nomes e modo recursivo.

## Objetivo

Demonstrar uma automação prática para reduzir o trabalho manual de organização de arquivos em pastas como Downloads, Área de Trabalho ou diretórios compartilhados.

## Exemplo

Antes:

```text
Downloads/
├── contrato.pdf
├── dashboard.xlsx
├── foto.png
├── video.mp4
├── script.py
└── backup.zip
```

Depois:

```text
Downloads/
├── Archives/backup.zip
├── Code/script.py
├── Documents/contrato.pdf
├── Images/foto.png
├── Spreadsheets/dashboard.xlsx
└── Videos/video.mp4
```

## Funcionalidades

- Organização automática por extensão
- Criação automática das pastas de destino
- Categoria `Others` para extensões não mapeadas
- Prevenção contra sobrescrita
- Renomeação automática em caso de duplicidade
- Modo de simulação com `--dry-run`
- Organização opcional de subpastas com `--recursive`
- Logs em arquivo
- Tratamento de erros
- Interface por linha de comando

## Tecnologias

- Python 3
- `pathlib`
- `shutil`
- `argparse`
- `logging`
- `dataclasses`

O projeto usa apenas a biblioteca padrão do Python.

## Como executar

```bash
git clone https://github.com/JoaoViana-bezerra/automation-python-lab.git
cd automation-python-lab/01-file-organizer
```

Teste primeiro sem mover arquivos:

```bash
python main.py "C:\Users\SeuUsuario\Downloads" --dry-run
```

Depois execute de verdade:

```bash
python main.py "C:\Users\SeuUsuario\Downloads"
```

Modo recursivo:

```bash
python main.py "C:\Users\SeuUsuario\Downloads" --recursive
```

Logs detalhados:

```bash
python main.py "C:\Users\SeuUsuario\Downloads" --verbose
```

## Segurança

Antes de usar em uma pasta real, execute sempre com `--dry-run`. Assim você vê o destino de cada arquivo antes da movimentação.

## Tratamento de duplicidade

Se já existir:

```text
Documents/relatorio.pdf
```

e outro arquivo com o mesmo nome for movido, o resultado será:

```text
Documents/relatorio.pdf
Documents/relatorio (1).pdf
```

Nenhum arquivo existente é sobrescrito.

## Estrutura

```text
01-file-organizer/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── sample/
└── logs/
```

## Próximas melhorias

- Configuração personalizada por JSON
- Regras por data e tamanho
- Interface gráfica
- Agendamento automático
- Testes automatizados
- Empacotamento como executável

## Autor

João Viana  
Desenvolvimento de Software | Automação | Dados
