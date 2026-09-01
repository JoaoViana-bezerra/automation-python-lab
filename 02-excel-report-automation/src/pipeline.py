from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from src.analytics import (
    add_calculated_columns, build_summary, group_by_month,
    group_by_product, group_by_region, group_by_seller,
)
from src.cleaner import clean_sales_data
from src.exporter import export_report


class ExcelReportPipeline:
    def __init__(self, input_path: Path, output_path: Path, sheet_name: str, logger: logging.Logger):
        self.input_path = input_path
        self.output_path = output_path
        self.sheet_name = sheet_name
        self.logger = logger

    def run(self) -> None:
        if not self.input_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.input_path}")

        self.logger.info("Lendo: %s", self.input_path)
        raw = pd.read_excel(self.input_path, sheet_name=self.sheet_name)
        self.logger.info("Linhas carregadas: %d", len(raw))

        clean = clean_sales_data(raw)
        treated = add_calculated_columns(clean)

        self.logger.info("Gerando consolidações...")
        export_report(
            self.output_path,
            treated,
            build_summary(treated),
            group_by_seller(treated),
            group_by_product(treated),
            group_by_region(treated),
            group_by_month(treated),
        )

        self.logger.info("Relatório gerado: %s", self.output_path)
