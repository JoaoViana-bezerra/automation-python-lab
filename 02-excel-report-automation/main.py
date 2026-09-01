from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.logger_config import configure_logger
from src.pipeline import ExcelReportPipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="excel-report-automation",
        description="Limpa, transforma e consolida uma planilha de vendas.",
    )
    parser.add_argument("input", nargs="?", default="input/vendas_exemplo.xlsx")
    parser.add_argument("-o", "--output", default="output/relatorio_vendas.xlsx")
    parser.add_argument("--sheet", default="Vendas")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = configure_logger(args.verbose)

    try:
        ExcelReportPipeline(
            input_path=Path(args.input).expanduser().resolve(),
            output_path=Path(args.output).expanduser().resolve(),
            sheet_name=args.sheet,
            logger=logger,
        ).run()
    except KeyboardInterrupt:
        logger.warning("Operação cancelada pelo usuário.")
        return 130
    except Exception as exc:
        logger.exception("Falha na automação: %s", exc)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
