from __future__ import annotations

from typing import Any

import pandas as pd


REQUIRED_COLUMNS = [
    "pedido",
    "data",
    "vendedor",
    "regiao",
    "produto",
    "categoria",
    "quantidade",
    "receita_liquida",
    "status",
]


def load_and_validate(path, delimiter: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=delimiter, encoding="utf-8-sig")

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes: " + ", ".join(missing)
        )

    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce").fillna(0)
    df["receita_liquida"] = pd.to_numeric(
        df["receita_liquida"], errors="coerce"
    ).fillna(0)

    df = df.dropna(subset=["data"]).copy()
    df["ano_mes"] = df["data"].dt.to_period("M").astype(str)

    return df


def analyze(df: pd.DataFrame) -> dict[str, Any]:
    completed = df[df["status"].str.casefold() == "concluído".casefold()].copy()

    revenue = float(completed["receita_liquida"].sum())
    completed_orders = int(completed["pedido"].nunique())

    kpis = {
        "Total de pedidos": int(df["pedido"].nunique()),
        "Pedidos concluídos": completed_orders,
        "Pedidos pendentes": int(
            (df["status"].str.casefold() == "pendente").sum()
        ),
        "Pedidos cancelados": int(
            (df["status"].str.casefold() == "cancelado").sum()
        ),
        "Receita líquida": revenue,
        "Ticket médio": revenue / completed_orders if completed_orders else 0,
        "Itens vendidos": int(completed["quantidade"].sum()),
    }

    sellers = (
        completed.groupby("vendedor", as_index=False)
        .agg(
            pedidos=("pedido", "nunique"),
            receita=("receita_liquida", "sum"),
        )
        .sort_values("receita", ascending=False)
    )

    products = (
        completed.groupby("produto", as_index=False)
        .agg(
            quantidade=("quantidade", "sum"),
            receita=("receita_liquida", "sum"),
        )
        .sort_values("receita", ascending=False)
    )

    regions = (
        completed.groupby("regiao", as_index=False)
        .agg(
            pedidos=("pedido", "nunique"),
            receita=("receita_liquida", "sum"),
        )
        .sort_values("receita", ascending=False)
    )

    monthly = (
        completed.groupby("ano_mes", as_index=False)
        .agg(
            pedidos=("pedido", "nunique"),
            receita=("receita_liquida", "sum"),
        )
        .sort_values("ano_mes")
    )

    return {
        "kpis": kpis,
        "sellers": sellers,
        "products": products,
        "regions": regions,
        "monthly": monthly,
    }
