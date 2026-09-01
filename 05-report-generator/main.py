from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.logger_config import configure_logger
from src.pipeline import ReportPipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="report-generator",
        description=(
            "Gera relatório executivo em PDF e HTML a partir de um CSV tratado."
        ),
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="input/vendas_tratadas.csv",
        help="CSV de entrada.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="output",
        help="Diretório de saída.",
    )
    parser.add_argument(
        "--delimiter",
        default=";",
        help="Delimitador do CSV. Padrão: ;",
    )
    parser.add_argument(
        "--title",
        default="Relatório Executivo de Vendas",
        help="Título exibido no relatório.",
    )
    parser.add_argument(
        "--format",
        choices=["all", "pdf", "html"],
        default="all",
        help="Formato de saída. Padrão: all.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Exibe logs detalhados.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = configure_logger(args.verbose)

    try:
        ReportPipeline(
            input_path=Path(args.input).expanduser().resolve(),
            output_dir=Path(args.output_dir).expanduser().resolve(),
            delimiter=args.delimiter,
            title=args.title,
            export_format=args.format,
            logger=logger,
        ).run()
        return 0
    except KeyboardInterrupt:
        logger.warning("Operação cancelada pelo usuário.")
        return 130
    except Exception as exc:
        logger.exception("Falha ao gerar relatório: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
