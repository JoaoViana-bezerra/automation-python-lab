from __future__ import annotations

import re
import unicodedata

import pandas as pd


STATE_MAP = {
    "MA": "MA",
    "MARANHAO": "MA",
    "MARANHÃO": "MA",
}


def normalize_text(value) -> str:
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def title_case(value) -> str:
    text = normalize_text(value)
    return text.title()


def normalize_email(value) -> str:
    return normalize_text(value).lower()


def normalize_state(value) -> str:
    text = normalize_text(value).upper()
    return STATE_MAP.get(text, text)


def normalize_status(value) -> str:
    text = normalize_text(value).lower()

    mapping = {
        "ativo": "Ativo",
        "inativo": "Inativo",
        "pendente": "Pendente",
    }

    return mapping.get(text, "Não informado" if not text else text.title())


def normalize_currency(value) -> float:
    if pd.isna(value):
        return 0.0

    text = str(value).strip().replace("R$", "").replace(" ", "")

    if not text:
        return 0.0

    # Handles:
    # 1.250,50
    # 850.00
    # 1,599.90
    # 3200
    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        text = text.replace(".", "").replace(",", ".")

    try:
        return float(text)
    except ValueError:
        return 0.0


def normalize_date(value):
    if pd.isna(value) or str(value).strip() == "":
        return pd.NaT

    return pd.to_datetime(
        value,
        errors="coerce",
        dayfirst=True,
    )
