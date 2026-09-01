from __future__ import annotations

import argparse
import logging
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

APP_NAME = "File Organizer"
DEFAULT_LOG_DIR = Path(__file__).resolve().parent / "logs"

FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".ico"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"},
    "Spreadsheets": {".xls", ".xlsx", ".xlsm", ".ods", ".csv"},
    "Presentations": {".ppt", ".pptx", ".odp"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"},
    "Videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm", ".m4v"},
    "Executables": {".exe", ".msi", ".bat", ".cmd", ".ps1", ".sh"},
    "Code": {".py", ".js", ".ts", ".html", ".css", ".java", ".cs", ".cpp", ".c", ".php", ".sql", ".json", ".xml", ".yml", ".yaml"},
}

@dataclass
class OrganizationResult:
    moved: int = 0
    skipped: int = 0
    errors: int = 0


def setup_logger(verbose: bool = False) -> logging.Logger:
    DEFAULT_LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(formatter)

    log_file = DEFAULT_LOG_DIR / f"file-organizer-{datetime.now():%Y%m%d}.log"
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


def get_category(file_path: Path) -> str:
    extension = file_path.suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def build_unique_destination(destination_dir: Path, filename: str) -> Path:
    target = destination_dir / filename
    if not target.exists():
        return target

    original = Path(filename)
    stem, suffix = original.stem, original.suffix
    counter = 1
    while True:
        candidate = destination_dir / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize_files(source_dir: Path, *, dry_run: bool = False, recursive: bool = False, logger: logging.Logger) -> OrganizationResult:
    result = OrganizationResult()

    if not source_dir.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"O caminho informado não é uma pasta: {source_dir}")

    logger.info("Iniciando organização em: %s", source_dir)
    logger.info("Modo recursivo: %s", "sim" if recursive else "não")
    logger.info("Simulação: %s", "sim" if dry_run else "não")

    entries = list(source_dir.rglob("*")) if recursive else list(source_dir.iterdir())
    category_names = set(FILE_CATEGORIES) | {"Others"}

    for item in entries:
        if not item.is_file() or item.name.startswith("."):
            continue

        if recursive:
            try:
                relative_parts = item.relative_to(source_dir).parts
                if relative_parts and relative_parts[0] in category_names:
                    result.skipped += 1
                    continue
            except ValueError:
                pass

        category = get_category(item)
        destination_dir = source_dir / category
        destination = build_unique_destination(destination_dir, item.name)

        try:
            if dry_run:
                logger.info("[SIMULAÇÃO] %s -> %s", item.name, destination.relative_to(source_dir))
            else:
                destination_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(item), str(destination))
                logger.info("Movido: %s -> %s", item.name, destination.relative_to(source_dir))
            result.moved += 1
        except (OSError, shutil.Error) as exc:
            logger.exception("Erro ao mover '%s': %s", item, exc)
            result.errors += 1

    logger.info("Finalizado | Movidos: %d | Ignorados: %d | Erros: %d", result.moved, result.skipped, result.errors)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="file-organizer", description="Organiza arquivos automaticamente por tipo.")
    parser.add_argument("path", nargs="?", default=".", help="Pasta que será organizada. Padrão: diretório atual.")
    parser.add_argument("--dry-run", action="store_true", help="Mostra as alterações sem mover nenhum arquivo.")
    parser.add_argument("--recursive", action="store_true", help="Inclui arquivos de subpastas.")
    parser.add_argument("--verbose", action="store_true", help="Exibe logs detalhados no terminal.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = setup_logger(args.verbose)
    source_dir = Path(args.path).expanduser().resolve()

    try:
        result = organize_files(source_dir, dry_run=args.dry_run, recursive=args.recursive, logger=logger)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as exc:
        logger.error("%s", exc)
        return 1
    except KeyboardInterrupt:
        logger.warning("Operação cancelada pelo usuário.")
        return 130

    return 0 if result.errors == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
