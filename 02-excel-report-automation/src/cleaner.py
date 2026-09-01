from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = [
    "Pedido", "Data", "Vendedor", "Região", "Cliente", "Produto",
    "Categoria", "Quantidade", "Preço Unitário", "Desconto %", "Status",
]


def validate_columns(df: pd.DataFrame) -> None:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {', '.join(missing)}")


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    clean = df.copy().dropna(how="all")
    clean = clean.drop_duplicates(subset=["Pedido"], keep="first")

    for col in ["Pedido", "Vendedor", "Região", "Cliente", "Produto", "Categoria", "Status"]:
        clean[col] = clean[col].fillna("").astype(str).str.strip()

    clean["Data"] = pd.to_datetime(clean["Data"], errors="coerce")
    clean["Quantidade"] = pd.to_numeric(clean["Quantidade"], errors="coerce").fillna(0)
    clean["Preço Unitário"] = pd.to_numeric(clean["Preço Unitário"], errors="coerce").fillna(0)
    clean["Desconto %"] = pd.to_numeric(clean["Desconto %"], errors="coerce").fillna(0)

    clean.loc[clean["Desconto %"] > 1, "Desconto %"] /= 100

    clean["Quantidade"] = clean["Quantidade"].clip(lower=0)
    clean["Preço Unitário"] = clean["Preço Unitário"].clip(lower=0)
    clean["Desconto %"] = clean["Desconto %"].clip(lower=0, upper=1)

    clean = clean.dropna(subset=["Data"])
    clean = clean[clean["Pedido"] != ""]

    return clean.reset_index(drop=True)
