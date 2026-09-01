from __future__ import annotations

import os
import time
from typing import Any

import requests


class GitHubHttpClient:
    BASE_URL = "https://api.github.com"

    def __init__(self, logger, timeout: int = 20, max_retries: int = 3) -> None:
        self.logger = logger
        self.timeout = timeout
        self.max_retries = max_retries

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "User-Agent": "automation-python-lab-api-data-collector",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )

        token = os.getenv("GITHUB_TOKEN")
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
            self.logger.debug("GITHUB_TOKEN detectado e configurado.")
        else:
            self.logger.debug("Executando sem autenticação.")

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> requests.Response:
        url = f"{self.BASE_URL}{endpoint}"

        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.session.get(
                    url,
                    params=params,
                    timeout=self.timeout,
                )

                self._log_rate_limit(response)

                if response.status_code == 403 and response.headers.get("X-RateLimit-Remaining") == "0":
                    reset_timestamp = response.headers.get("X-RateLimit-Reset")
                    raise RuntimeError(
                        "Limite de requisições da API do GitHub atingido. "
                        f"Reset informado pela API: {reset_timestamp}"
                    )

                if response.status_code == 404:
                    raise ValueError("Usuário ou recurso não encontrado na API do GitHub.")

                response.raise_for_status()
                return response

            except requests.RequestException as exc:
                if attempt == self.max_retries:
                    raise RuntimeError(
                        f"Erro após {self.max_retries} tentativas ao acessar {url}: {exc}"
                    ) from exc

                wait_seconds = 2 ** (attempt - 1)
                self.logger.warning(
                    "Falha na requisição. Nova tentativa em %ss (%d/%d).",
                    wait_seconds,
                    attempt,
                    self.max_retries,
                )
                time.sleep(wait_seconds)

        raise RuntimeError("Falha inesperada na camada HTTP.")

    def _log_rate_limit(self, response: requests.Response) -> None:
        remaining = response.headers.get("X-RateLimit-Remaining")
        limit = response.headers.get("X-RateLimit-Limit")

        if remaining is not None and limit is not None:
            self.logger.debug(
                "GitHub API rate limit: %s/%s requisições restantes.",
                remaining,
                limit,
            )
