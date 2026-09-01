from __future__ import annotations

import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(value: str) -> bool:
    if not value:
        return False
    return bool(EMAIL_PATTERN.fullmatch(value))


def normalize_phone(value: str) -> str:
    digits = re.sub(r"\D", "", value or "")

    if len(digits) == 11:
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
    if len(digits) == 10:
        return f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"

    return digits


def is_valid_phone(value: str) -> bool:
    digits = re.sub(r"\D", "", value or "")
    return len(digits) in {10, 11}
