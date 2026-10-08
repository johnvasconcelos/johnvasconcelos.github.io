"""Identidade visual do projeto para gráficos (matplotlib/seaborn) e tabelas (Great Tables).

Uso no primeiro bloco de cada .qmd:

    from helpers import CORES, PALETA, aplicar_tema, tabela, rotular_fim_linha
    aplicar_tema()
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ---- Cores da marca (iguais ao custom.scss) ---------------------------------
CORES = {
    "verde": "#154734",
    "laranja": "#ED7D31",
    "laranja_escuro": "#E87500",
    "menta": "#5FE0B7",
    "tinta": "#171B18",
    "cinza_1": "#3A413C",
    "cinza_2": "#636B64",
    "cinza_3": "#9AA199",
    "cinza_4": "#D8DBD4",
    "verde_claro": "#EEF5F0",
    "laranja_claro": "#FDF1E3",
}

# ---- Paleta categórica para gráficos -----------------------------------------
# Verde e laranja da marca, ajustados para a faixa de luminosidade de dados,
# mais azul e magenta. Validada para daltonismo (ΔE ≥ 9,6 entre vizinhas).
# Use SEMPRE nesta ordem; não gere uma 5ª cor — agrupe em "Outros".
# O laranja tem contraste < 3:1 com o branco: rotule as séries diretamente.
PALETA = ["#14805A", "#E87500", "#3F6DD0", "#B8457E"]

# Sequencial (magnitude): um só matiz, claro → escuro
SEQUENCIAL = LinearSegmentedColormap.from_list(
    "verde_seq", ["#EEF5F0", "#9CCBB2", "#14805A", "#154734"])
# Divergente (polaridade): laranja ↔ cinza neutro ↔ verde
DIVERGENTE = LinearSegmentedColormap.from_list(
    "laranja_verde", ["#E87500", "#F2F2EF", "#14805A"])

FONTE = ["Georgia", "Gelasio", "DejaVu Serif"]


def aplicar_tema():
    """Aplica o tema a todos os gráficos matplotlib/seaborn da sessão."""
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": FONTE,
        "font.size": 11,
        "text.color": CORES["tinta"],
        "axes.prop_cycle": mpl.cycler(color=PALETA),
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        "axes.edgecolor": CORES["cinza_4"],
        "axes.labelcolor": CORES["cinza_1"],
        "axes.titlecolor": CORES["verde"],
        "axes.titleweight": "bold",
        "axes.titlesize": 14,
        "axes.titlelocation": "left",
        "axes.titlepad": 14,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "axes.axisbelow": True,
        "grid.color": "#ECEEEA",
        "grid.linewidth": 0.8,
        "xtick.color": CORES["cinza_2"],
        "ytick.color": CORES["cinza_2"],
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "lines.linewidth": 2,
        "lines.markersize": 7,
        "patch.linewidth": 0,
        "legend.frameon": False,
        "image.cmap": "verde_seq",
        "savefig.bbox": "tight",
    })
    try:
        mpl.colormaps.register(SEQUENCIAL)
        mpl.colormaps.register(DIVERGENTE)
    except ValueError:
        pass  # já registrados


def rotular_fim_linha(ax, x, ys, nomes, fmt="{:,.0f}", espaco_min=0.06):
    """Rótulo direto no fim de cada linha, afastando rótulos que colidiriam.
    Chame DEPOIS de definir os limites do eixo y.
    espaco_min = distância mínima entre rótulos, em fração da altura do eixo."""
    y0, y1 = ax.get_ylim()
    minimo = espaco_min * (y1 - y0)
    deslocamento_x = (x[-1] - x[0]) * 0.03
    itens = sorted(zip([y[-1] for y in ys], nomes, PALETA), key=lambda t: t[0])
    ultimo = None
    for valor, nome, cor in itens:
        pos = valor if ultimo is None else max(valor, ultimo + minimo)
        ultimo = pos
        ax.plot(x[-1], valor, "o", color=cor, markersize=7, markeredgecolor="white",
                markeredgewidth=2, zorder=5, clip_on=False)
        ax.annotate(f"{nome}  {fmt.format(valor)}", xy=(x[-1], valor),
                    xytext=(x[-1] + deslocamento_x, pos), textcoords="data",
                    va="center", ha="left", fontsize=10, color=CORES["tinta"],
                    annotation_clip=False)


def tabela(df, titulo=None, subtitulo=None, fonte=None, moeda=None, decimais=0):
    """Tabela Great Tables no padrão dos slides: cabeçalho verde, filete laranja,
    linhas alternadas em laranja-claro.

    moeda: lista de colunas para formatar como número com separador de milhar.
    """
    from great_tables import GT, style, loc

    gt = GT(df)
    if titulo:
        gt = gt.tab_header(title=titulo, subtitle=subtitulo)
    if moeda:
        gt = gt.fmt_number(columns=moeda, decimals=decimais, use_seps=True)
    if fonte:
        gt = gt.tab_source_note(fonte)
    return (
        gt.opt_table_font(font=FONTE + ["serif"])
        .opt_row_striping()
        .tab_options(
            table_font_color=CORES["tinta"],
            table_font_size="14px",
            table_border_top_color=CORES["verde"],
            table_border_top_width="2px",
            heading_align="left",
            heading_title_font_size="18px",
            heading_title_font_weight="bold",
            heading_subtitle_font_size="13px",
            heading_border_bottom_color="white",
            column_labels_font_weight="bold",
            column_labels_border_bottom_color=CORES["laranja"],
            column_labels_border_bottom_width="2px",
            column_labels_border_top_color="white",
            row_striping_background_color=CORES["laranja_claro"],
            table_body_hlines_color="white",
            table_body_border_bottom_color=CORES["verde"],
            source_notes_font_size="12px",
        )
        .tab_style(style.text(color=CORES["verde"], weight="bold"), loc.title())
        .tab_style(style.text(color=CORES["cinza_2"]), loc.subtitle())
        .tab_style(style.text(color=CORES["verde"]), loc.column_labels())
    )
