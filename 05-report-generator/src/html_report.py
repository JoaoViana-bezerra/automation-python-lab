from __future__ import annotations

import base64
from pathlib import Path


def _money(value: float) -> str:
    text = f"{value:,.2f}"
    text = text.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {text}"


def _image_data_uri(path: Path | None) -> str:
    if not path or not path.exists():
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def generate_html(
    output_path: Path,
    title: str,
    analysis: dict,
    charts: dict,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    kpis = analysis["kpis"]
    seller_img = _image_data_uri(charts.get("sellers"))
    monthly_img = _image_data_uri(charts.get("monthly"))

    top_sellers = "".join(
        f"<tr><td>{row.vendedor}</td><td>{int(row.pedidos)}</td><td>{_money(row.receita)}</td></tr>"
        for row in analysis["sellers"].head(8).itertuples(index=False)
    )

    top_products = "".join(
        f"<tr><td>{row.produto}</td><td>{int(row.quantidade)}</td><td>{_money(row.receita)}</td></tr>"
        for row in analysis["products"].head(8).itertuples(index=False)
    )

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{
  --bg:#f3f6fa; --surface:#ffffff; --navy:#0f172a; --blue:#2563eb;
  --muted:#64748b; --border:#e2e8f0; --green:#059669;
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:Arial,Helvetica,sans-serif; background:var(--bg); color:var(--navy); }}
.container {{ width:min(1120px,calc(100% - 32px)); margin:36px auto; }}
.header {{ padding:34px; border-radius:22px; background:var(--navy); color:#fff; }}
.header small {{ color:#93c5fd; text-transform:uppercase; letter-spacing:.08em; }}
.header h1 {{ margin:8px 0 6px; font-size:34px; }}
.header p {{ margin:0; color:#cbd5e1; }}
.kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:18px; }}
.kpi {{ background:var(--surface); border:1px solid var(--border); border-radius:16px; padding:20px; }}
.kpi span {{ color:var(--muted); font-size:13px; }}
.kpi strong {{ display:block; margin-top:8px; font-size:24px; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-top:18px; }}
.card {{ background:var(--surface); border:1px solid var(--border); border-radius:18px; padding:22px; }}
.card h2 {{ margin:0 0 16px; font-size:19px; }}
.card img {{ width:100%; border-radius:10px; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; }}
th,td {{ padding:11px 8px; text-align:left; border-bottom:1px solid var(--border); }}
th {{ color:var(--muted); font-size:12px; text-transform:uppercase; }}
.footer {{ margin:26px 0 10px; text-align:center; color:var(--muted); font-size:12px; }}
@media(max-width:820px) {{
 .kpis,.grid {{ grid-template-columns:1fr 1fr; }}
}}
@media(max-width:560px) {{
 .kpis,.grid {{ grid-template-columns:1fr; }}
}}
</style>
</head>
<body>
<div class="container">
<section class="header">
  <small>Automation Python Lab</small>
  <h1>{title}</h1>
  <p>Relatório gerado automaticamente a partir de dados estruturados.</p>
</section>

<section class="kpis">
  <div class="kpi"><span>Receita líquida</span><strong>{_money(kpis["Receita líquida"])}</strong></div>
  <div class="kpi"><span>Pedidos concluídos</span><strong>{kpis["Pedidos concluídos"]}</strong></div>
  <div class="kpi"><span>Ticket médio</span><strong>{_money(kpis["Ticket médio"])}</strong></div>
  <div class="kpi"><span>Itens vendidos</span><strong>{kpis["Itens vendidos"]}</strong></div>
</section>

<section class="grid">
  <div class="card"><h2>Receita por vendedor</h2><img src="{seller_img}" alt="Receita por vendedor"></div>
  <div class="card"><h2>Evolução mensal</h2><img src="{monthly_img}" alt="Evolução mensal"></div>
</section>

<section class="grid">
  <div class="card">
    <h2>Ranking de vendedores</h2>
    <table><thead><tr><th>Vendedor</th><th>Pedidos</th><th>Receita</th></tr></thead><tbody>{top_sellers}</tbody></table>
  </div>
  <div class="card">
    <h2>Produtos em destaque</h2>
    <table><thead><tr><th>Produto</th><th>Qtd.</th><th>Receita</th></tr></thead><tbody>{top_products}</tbody></table>
  </div>
</section>

<div class="footer">João Viana - Desenvolvimento de Software | Automação | Dados</div>
</div>
</body>
</html>"""

    output_path.write_text(html, encoding="utf-8")
