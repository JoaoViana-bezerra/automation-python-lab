from __future__ import annotations

from datetime import datetime
from typing import Any

from src.http_client import GitHubHttpClient


class GitHubRepositoryCollector:
    def __init__(
        self,
        username: str,
        logger,
        include_forks: bool = False,
    ) -> None:
        self.username = username.strip()
        self.logger = logger
        self.include_forks = include_forks
        self.client = GitHubHttpClient(logger=logger)

        if not self.username:
            raise ValueError("O nome do usuário do GitHub não pode ser vazio.")

    def collect(self) -> list[dict[str, Any]]:
        self.logger.info("Coletando repositórios públicos de: %s", self.username)

        raw_repositories = self._fetch_all_repositories()
        self.logger.info("Repositórios recebidos da API: %d", len(raw_repositories))

        normalized = []

        for repo in raw_repositories:
            if repo.get("fork") and not self.include_forks:
                self.logger.debug("Fork ignorado: %s", repo.get("name"))
                continue

            normalized.append(self._normalize_repository(repo))

        normalized.sort(
            key=lambda item: item.get("updated_at") or "",
            reverse=True,
        )

        self.logger.info("Repositórios após filtros: %d", len(normalized))
        return normalized

    def _fetch_all_repositories(self) -> list[dict[str, Any]]:
        repositories: list[dict[str, Any]] = []
        page = 1

        while True:
            self.logger.debug("Consultando página %d...", page)

            response = self.client.get(
                f"/users/{self.username}/repos",
                params={
                    "per_page": 100,
                    "page": page,
                    "sort": "updated",
                    "direction": "desc",
                    "type": "owner",
                },
            )

            current_page = response.json()

            if not current_page:
                break

            repositories.extend(current_page)

            if len(current_page) < 100:
                break

            page += 1

        return repositories

    @staticmethod
    def _normalize_repository(repo: dict[str, Any]) -> dict[str, Any]:
        license_data = repo.get("license") or {}

        return {
            "id": repo.get("id"),
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "description": repo.get("description") or "",
            "html_url": repo.get("html_url"),
            "language": repo.get("language") or "Não informado",
            "visibility": repo.get("visibility"),
            "is_fork": bool(repo.get("fork")),
            "is_archived": bool(repo.get("archived")),
            "default_branch": repo.get("default_branch"),
            "stars": repo.get("stargazers_count", 0),
            "watchers": repo.get("watchers_count", 0),
            "forks": repo.get("forks_count", 0),
            "open_issues": repo.get("open_issues_count", 0),
            "size_kb": repo.get("size", 0),
            "license": license_data.get("spdx_id") or "",
            "created_at": repo.get("created_at"),
            "updated_at": repo.get("updated_at"),
            "pushed_at": repo.get("pushed_at"),
            "homepage": repo.get("homepage") or "",
            "topics": ", ".join(repo.get("topics") or []),
            "collected_at": datetime.now().isoformat(timespec="seconds"),
        }
