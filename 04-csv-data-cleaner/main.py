from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.cleaner import CsvDataCleaner
from src.logger_config import configure_logger
from src.reporter import export_quality_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="csv-data-cleaner",
        description=(
            "Limpa, padroniza e valida arquivos CSV, gerando uma base tratada "
            "e um relatório de qualidade dos dados."
        ),
    )

    parser.add_argument(
        "input",
        nargs="?",
        default="input/clientes_sujos.csv",
        help="Arquivo CSV de entrada.",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="output/clientes_limpos.csv",
        help="Arquivo CSV tratado.",
    )

    parser.add_argument(
        "--report",
        default="output/relatorio_qualidade.json",
        help="Arquivo JSON com métricas de qualidade.",
    )

    parser.add_argument(
        "--delimiter",
        default=";",
        help="Delimitador do CSV. Padrão: ;",
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
        cleaner = CsvDataCleaner(
            input_path=Path(args.input).expanduser().resolve(),
            output_path=Path(args.output).expanduser().resolve(),
            delimiter=args.delimiter,
            logger=logger,
        )

        cleaned_df, quality_report = cleaner.run()

        export_quality_report(
            report=quality_report,
            output_path=Path(args.report).expanduser().resolve(),
            logger=logger,
        )

        logger.info("Registros finais: %d", len(cleaned_df))
        logger.info("Processo concluído com sucesso.")
        return 0

    except KeyboardInterrupt:
        logger.warning("Operação cancelada pelo usuário.")
        return 130
    except Exception as exc:
        logger.exception("Falha no processamento: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
