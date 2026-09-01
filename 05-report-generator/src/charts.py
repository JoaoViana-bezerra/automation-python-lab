from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def create_charts(analysis: dict, assets_dir: Path) -> dict[str, Path]:
    assets_dir.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, Path] = {}

    sellers = analysis["sellers"].head(6)
    if not sellers.empty:
        path = assets_dir / "receita_vendedores.png"
        fig, ax = plt.subplots(figsize=(8.4, 4.6))
        ax.barh(sellers["vendedor"][::-1], sellers["receita"][::-1])
        ax.set_title("Receita líquida por vendedor")
        ax.set_xlabel("Receita")
        ax.grid(axis="x", alpha=0.2)
        fig.tight_layout()
        fig.savefig(path, dpi=160, bbox_inches="tight")
        plt.close(fig)
        outputs["sellers"] = path

    monthly = analysis["monthly"]
    if not monthly.empty:
        path = assets_dir / "evolucao_mensal.png"
        fig, ax = plt.subplots(figsize=(8.4, 4.6))
        ax.plot(monthly["ano_mes"], monthly["receita"], marker="o")
        ax.set_title("Evolução mensal da receita")
        ax.set_xlabel("Mês")
        ax.set_ylabel("Receita")
        ax.grid(alpha=0.2)
        ax.tick_params(axis="x", rotation=35)
        fig.tight_layout()
        fig.savefig(path, dpi=160, bbox_inches="tight")
        plt.close(fig)
        outputs["monthly"] = path

    return outputs
