from __future__ import annotations

from typing import Any

import pandas as pd


def build_quality_report(
    original: pd.DataFrame,
    cleaned: pd.DataFrame,
    invalid_emails: int,
    invalid_phones: int,
    invalid_dates: int,
    duplicate_rows: int,
    negative_values: int,
) -> dict[str, Any]:
    missing_before = int(original.isna().sum().sum())
    missing_after = int(cleaned.replace("", pd.NA).isna().sum().sum())

    return {
        "input_rows": int(len(original)),
        "output_rows": int(len(cleaned)),
        "removed_duplicates": int(duplicate_rows),
        "invalid_emails": int(invalid_emails),
        "invalid_phones": int(invalid_phones),
        "invalid_dates": int(invalid_dates),
        "negative_values_corrected": int(negative_values),
        "missing_values_before": missing_before,
        "missing_values_after": missing_after,
        "columns": list(cleaned.columns),
    }
