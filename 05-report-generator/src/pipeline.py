from __future__ import annotations

import logging
from pathlib import Path

from src.analyzer import analyze, load_and_validate
from src.charts import create_charts
from src.html_report import generate_html
from src.pdf_report import generate_pdf


class ReportPipeline:
    def __init__(
        self,
        input_path: Path,
        output_dir: Path,
        delimiter: str,
        title: str,
        export_format: str,
        logger: logging.Logger,
    ) -> None:
        self.input_path = input_path
        self.output_dir = output_dir
        self.delimiter = delimiter
        self.title = title
        self.export_format = export_format
        self.logger = logger

    def run(self) -> None:
        if not self.input_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.input_path}")

        self.output_dir.mkdir(parents=True, exist_ok=True)
        assets_dir = self.output_dir / "assets"

        self.logger.info("Lendo e validando: %s", self.input_path)
        df = load_and_validate(self.input_path, self.delimiter)

        self.logger.info("Calculando indicadores...")
        analysis = analyze(df)

        self.logger.info("Gerando gráficos...")
        charts = create_charts(analysis, assets_dir)

        if self.export_format in {"all", "html"}:
            html_path = self.output_dir / "relatorio_executivo.html"
            generate_html(html_path, self.title, analysis, charts)
            self.logger.info("HTML gerado: %s", html_path)

        if self.export_format in {"all", "pdf"}:
            pdf_path = self.output_dir / "relatorio_executivo.pdf"
            generate_pdf(pdf_path, self.title, analysis, charts)
            self.logger.info("PDF gerado: %s", pdf_path)

        self.logger.info("Processo finalizado com sucesso.")
