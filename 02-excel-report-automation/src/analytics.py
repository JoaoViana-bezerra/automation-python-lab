from __future__ import annotations

import pandas as pd


def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["Receita Bruta"] = result["Quantidade"] * result["Preço Unitário"]
    result["Valor Desconto"] = result["Receita Bruta"] * result["Desconto %"]
    result["Receita Líquida"] = result["Receita Bruta"] - result["Valor Desconto"]
    result["Ano-Mês"] = result["Data"].dt.to_period("M").astype(str)
    return result


def completed_sales(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Status"].str.casefold() == "concluído".casefold()].copy()


def build_summary(df: pd.DataFrame) -> dict[str, float | int]:
    concluded = completed_sales(df)
    completed = len(concluded)
    net = float(concluded["Receita Líquida"].sum())

    return {
        "Total de Pedidos": int(len(df)),
        "Pedidos Concluídos": int(completed),
        "Pedidos Pendentes": int((df["Status"].str.casefold() == "pendente").sum()),
        "Pedidos Cancelados": int((df["Status"].str.casefold() == "cancelado").sum()),
        "Receita Bruta": float(concluded["Receita Bruta"].sum()),
        "Descontos Concedidos": float(concluded["Valor Desconto"].sum()),
        "Receita Líquida": net,
        "Ticket Médio": float(net / completed) if completed else 0.0,
    }


def group_by_seller(df: pd.DataFrame) -> pd.DataFrame:
    data = completed_sales(df)
    return (
        data.groupby("Vendedor", as_index=False)
        .agg(Pedidos=("Pedido", "nunique"),
             Quantidade=("Quantidade", "sum"),
             Receita_Liquida=("Receita Líquida", "sum"))
        .sort_values("Receita_Liquida", ascending=False)
    )


def group_by_product(df: pd.DataFrame) -> pd.DataFrame:
    data = completed_sales(df)
    return (
        data.groupby(["Produto", "Categoria"], as_index=False)
        .agg(Pedidos=("Pedido", "nunique"),
             Quantidade=("Quantidade", "sum"),
             Receita_Liquida=("Receita Líquida", "sum"))
        .sort_values("Receita_Liquida", ascending=False)
    )


def group_by_region(df: pd.DataFrame) -> pd.DataFrame:
    data = completed_sales(df)
    return (
        data.groupby("Região", as_index=False)
        .agg(Pedidos=("Pedido", "nunique"),
             Receita_Liquida=("Receita Líquida", "sum"))
        .sort_values("Receita_Liquida", ascending=False)
    )


def group_by_month(df: pd.DataFrame) -> pd.DataFrame:
    data = completed_sales(df)
    return (
        data.groupby("Ano-Mês", as_index=False)
        .agg(Pedidos=("Pedido", "nunique"),
             Receita_Liquida=("Receita Líquida", "sum"))
        .sort_values("Ano-Mês")
    )
