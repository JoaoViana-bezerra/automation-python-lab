from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)


NAVY = colors.HexColor("#0F172A")
BLUE = colors.HexColor("#2563EB")
MUTED = colors.HexColor("#64748B")
LIGHT = colors.HexColor("#F1F5F9")
BORDER = colors.HexColor("#E2E8F0")
WHITE = colors.white


def money(value: float) -> str:
    text = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {text}"


def generate_pdf(
    output_path: Path,
    title: str,
    analysis: dict,
    charts: dict,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=17 * mm,
        leftMargin=17 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title=title,
        author="João Viana",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=23,
        leading=28,
        textColor=NAVY,
        alignment=TA_LEFT,
        spaceAfter=5,
    )
    kicker_style = ParagraphStyle(
        "Kicker",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10,
        textColor=BLUE,
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=10,
        leading=15,
        textColor=MUTED,
        spaceAfter=16,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=17,
        textColor=NAVY,
        spaceBefore=10,
        spaceAfter=8,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13,
        textColor=NAVY,
    )

    story = [
        Paragraph("AUTOMATION PYTHON LAB", kicker_style),
        Paragraph(title, title_style),
        Paragraph(
            "Relatório executivo gerado automaticamente a partir de dados estruturados.",
            subtitle_style,
        ),
    ]

    k = analysis["kpis"]
    kpi_data = [
        [
            Paragraph("<b>Receita líquida</b>", body_style),
            Paragraph("<b>Pedidos concluídos</b>", body_style),
            Paragraph("<b>Ticket médio</b>", body_style),
            Paragraph("<b>Itens vendidos</b>", body_style),
        ],
        [
            money(k["Receita líquida"]),
            str(k["Pedidos concluídos"]),
            money(k["Ticket médio"]),
            str(k["Itens vendidos"]),
        ],
    ]

    kpi_table = Table(kpi_data, colWidths=[42 * mm] * 4, rowHeights=[10 * mm, 13 * mm])
    kpi_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("TEXTCOLOR", (0, 1), (-1, 1), NAVY),
        ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 1), (-1, 1), 13),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story += [kpi_table, Spacer(1, 7 * mm)]

    if charts.get("sellers"):
        story.append(
            KeepTogether([
                Paragraph("Receita por vendedor", section_style),
                Image(str(charts["sellers"]), width=170 * mm, height=93 * mm),
                Spacer(1, 4 * mm),
            ])
        )

    if charts.get("monthly"):
        story.append(
            KeepTogether([
                Paragraph("Evolução mensal", section_style),
                Image(str(charts["monthly"]), width=170 * mm, height=93 * mm),
            ])
        )
        story.append(PageBreak())

    story.append(Paragraph("Ranking de vendedores", section_style))
    seller_data = [["Vendedor", "Pedidos", "Receita"]]
    seller_data.extend([
        [row.vendedor, int(row.pedidos), money(row.receita)]
        for row in analysis["sellers"].head(10).itertuples(index=False)
    ])

    seller_table = Table(seller_data, colWidths=[80 * mm, 35 * mm, 55 * mm], repeatRows=1)
    seller_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [seller_table, Spacer(1, 7 * mm)]

    story.append(Paragraph("Produtos em destaque", section_style))
    product_data = [["Produto", "Quantidade", "Receita"]]
    product_data.extend([
        [row.produto, int(row.quantidade), money(row.receita)]
        for row in analysis["products"].head(10).itertuples(index=False)
    ])

    product_table = Table(product_data, colWidths=[80 * mm, 35 * mm, 55 * mm], repeatRows=1)
    product_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [product_table]

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(
            17 * mm,
            9 * mm,
            "João Viana - Desenvolvimento de Software | Automação | Dados",
        )
        canvas.drawRightString(
            A4[0] - 17 * mm,
            9 * mm,
            f"Página {doc.page}",
        )
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
