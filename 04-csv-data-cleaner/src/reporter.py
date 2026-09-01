from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any


def export_quality_report(
    report: dict[str, Any],
    output_path: Path,
    logger: logging.Logger,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    logger.info("Relatório de qualidade gerado: %s", output_path)
