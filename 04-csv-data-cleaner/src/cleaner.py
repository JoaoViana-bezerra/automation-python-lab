from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from src.normalizers import (
    normalize_currency,
    normalize_date,
    normalize_email,
    normalize_state,
    normalize_status,
    title_case,
)
from src.quality import build_quality_report
from src.validators import (
    is_valid_email,
    is_valid_phone,
    normalize_phone,
)


REQUIRED_COLUMNS = [
    "id",
    "nome",
    "email",
    "telefone",
    "cidade",
    "estado",
    "data_cadastro",
    "valor_compras",
    "status",
]


class CsvDataCleaner:
    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        delimiter: str,
        logger: logging.Logger,
    ) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.delimiter = delimiter
        self.logger = logger

    def run(self):
        if not self.input_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.input_path}")

        self.logger.info("Lendo arquivo: %s", self.input_path)

        original = pd.read_csv(
            self.input_path,
            sep=self.delimiter,
            dtype=str,
            encoding="utf-8-sig",
        )

        self._validate_columns(original)

        duplicate_rows = int(original.duplicated(subset=["id"]).sum())

        df = original.drop_duplicates(subset=["id"], keep="first").copy()

        # Padronização textual
        df["nome"] = df["nome"].apply(title_case)
        df["email"] = df["email"].apply(normalize_email)
        df["cidade"] = df["cidade"].apply(title_case)
        df["estado"] = df["estado"].apply(normalize_state)
        df["status"] = df["status"].apply(normalize_status)

        # E-mail
        invalid_email_mask = ~df["email"].apply(is_valid_email)
        invalid_emails = int(invalid_email_mask.sum())
        df.loc[invalid_email_mask, "email"] = ""

        # Telefone
        original_phone = df["telefone"].fillna("").astype(str)
        invalid_phone_mask = ~original_phone.apply(is_valid_phone)
        invalid_phones = int(invalid_phone_mask.sum())
        df["telefone"] = original_phone.apply(normalize_phone)
        df.loc[invalid_phone_mask, "telefone"] = ""

        # Datas
        parsed_dates = df["data_cadastro"].apply(normalize_date)
        invalid_dates = int(parsed_dates.isna().sum())
        df["data_cadastro"] = parsed_dates.dt.strftime("%Y-%m-%d").fillna("")

        # Valores
        df["valor_compras"] = df["valor_compras"].apply(normalize_currency)
        negative_mask = df["valor_compras"] < 0
        negative_values = int(negative_mask.sum())
        df.loc[negative_mask, "valor_compras"] = 0.0

        # Campos ausentes
        df["nome"] = df["nome"].replace("", "Não informado")
        df["cidade"] = df["cidade"].replace("", "Não informado")
        df["estado"] = df["estado"].replace("", "Não informado")

        # Tipagem e ordenação
        df["id"] = pd.to_numeric(df["id"], errors="coerce").astype("Int64")
        df = df.sort_values("id", na_position="last").reset_index(drop=True)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(
            self.output_path,
            sep=";",
            index=False,
            encoding="utf-8-sig",
            float_format="%.2f",
        )

        self.logger.info("Arquivo tratado gerado: %s", self.output_path)

        report = build_quality_report(
            original=original,
            cleaned=df,
            invalid_emails=invalid_emails,
            invalid_phones=invalid_phones,
            invalid_dates=invalid_dates,
            duplicate_rows=duplicate_rows,
            negative_values=negative_values,
        )

        return df, report

    @staticmethod
    def _validate_columns(df: pd.DataFrame) -> None:
        missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]

        if missing:
            raise ValueError(
                "Colunas obrigatórias ausentes: "
                + ", ".join(missing)
            )
