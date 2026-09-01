from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.collector import GitHubRepositoryCollector
from src.exporter import export_data
from src.logger_config import configure_logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="api-data-collector",
        description=(
            "Coleta repositórios públicos da API REST do GitHub, "
            "normaliza os dados e exporta JSON, CSV e Excel."
        ),
    )

    parser.add_argument(
        "username",
        nargs="?",
        default="JoaoViana-bezerra",
        help="Usuário do GitHub que será consultado.",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        default="output",
        help="Diretório onde os arquivos serão gerados.",
    )

    parser.add_argument(
        "--format",
        choices=["all", "json", "csv", "xlsx"],
        default="all",
        help="Formato de exportação. Padrão: all.",
    )

    parser.add_argument(
        "--include-forks",
        action="store_true",
        help="Inclui repositórios que são forks.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Exibe logs detalhados no terminal.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = configure_logger(args.verbose)

    try:
        collector = GitHubRepositoryCollector(
            username=args.username,
            logger=logger,
            include_forks=args.include_forks,
        )

        repositories = collector.collect()

        if not repositories:
            logger.warning("Nenhum repositório encontrado para '%s'.", args.username)
            return 0

        output_dir = Path(args.output_dir).expanduser().resolve()

        export_data(
            repositories=repositories,
            output_dir=output_dir,
            username=args.username,
            export_format=args.format,
            logger=logger,
        )

        logger.info("Coleta finalizada com sucesso.")
        return 0

    except KeyboardInterrupt:
        logger.warning("Operação cancelada pelo usuário.")
        return 130
    except Exception as exc:
        logger.exception("Falha durante a coleta: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
