from __future__ import annotations

from collections import Counter
from typing import Any


def build_summary(repositories: list[dict[str, Any]]) -> dict[str, Any]:
    languages = [
        repo["language"]
        for repo in repositories
        if repo.get("language") and repo["language"] != "Não informado"
    ]

    language_counts = Counter(languages)

    return {
        "total_repositories": len(repositories),
        "total_stars": sum(repo.get("stars", 0) for repo in repositories),
        "total_forks": sum(repo.get("forks", 0) for repo in repositories),
        "total_open_issues": sum(repo.get("open_issues", 0) for repo in repositories),
        "archived_repositories": sum(
            1 for repo in repositories if repo.get("is_archived")
        ),
        "languages": dict(language_counts.most_common()),
        "most_used_language": (
            language_counts.most_common(1)[0][0]
            if language_counts
            else "Não informado"
        ),
    }
