# Identidade visual do projeto para gráficos (ggplot2) e tabelas (gt).
# Carregado por _setup-r.qmd. Mesmas cores de custom.scss e helpers.py.
library(ggplot2)

cores <- c(
  verde = "#154734", laranja = "#ED7D31", laranja_escuro = "#E87500",
  menta = "#5FE0B7", tinta = "#171B18", cinza_1 = "#3A413C",
  cinza_2 = "#636B64", cinza_3 = "#9AA199", cinza_4 = "#D8DBD4",
  verde_claro = "#EEF5F0", laranja_claro = "#FDF1E3", grade = "#ECEEEA"
)

# Paleta categórica validada para daltonismo. Sempre nesta ordem; máximo 4 séries.
paleta <- c("#14805A", "#E87500", "#3F6DD0", "#B8457E")

# Georgia se existir no sistema; senão Gelasio; senão a serifa padrão
.familias <- systemfonts::system_fonts()$family
fonte <- if ("Georgia" %in% .familias) "Georgia" else if ("Gelasio" %in% .familias) "Gelasio" else "serif"

theme_projeto <- function(base_size = 11) {
  theme_minimal(base_family = fonte, base_size = base_size) +
    theme(
      text                = element_text(color = cores[["tinta"]]),
      plot.title          = element_text(face = "bold", color = cores[["verde"]],
                                         size = rel(1.27), margin = margin(b = 10)),
      plot.title.position = "plot",
      plot.subtitle       = element_text(color = cores[["cinza_2"]]),
      plot.caption        = element_text(color = cores[["cinza_2"]], hjust = 0),
      axis.title          = element_text(color = cores[["cinza_1"]]),
      axis.text           = element_text(color = cores[["cinza_2"]]),
      panel.grid.minor    = element_blank(),
      panel.grid.major.x  = element_blank(),
      panel.grid.major.y  = element_line(color = cores[["grade"]], linewidth = 0.4),
      legend.position     = "top",
      legend.justification = "left",
      legend.title        = element_blank()
    )
}

theme_set(theme_projeto())
options(
  ggplot2.discrete.colour   = paleta,
  ggplot2.discrete.fill     = paleta,
  ggplot2.continuous.colour = function(...) scale_colour_gradient(low = cores[["verde_claro"]], high = cores[["verde"]], ...),
  ggplot2.continuous.fill   = function(...) scale_fill_gradient(low = cores[["verde_claro"]], high = cores[["verde"]], ...)
)
update_geom_defaults("bar",  list(fill = paleta[1]))
update_geom_defaults("col",  list(fill = paleta[1]))
update_geom_defaults("line", list(colour = paleta[1], linewidth = 0.9))
update_geom_defaults("point", list(colour = paleta[1]))

# Tabela gt no padrão dos slides: cabeçalho verde, filete laranja, linhas alternadas.
tabela <- function(dados, titulo = NULL, subtitulo = NULL, fonte_dados = NULL,
                   numeros = NULL, decimais = 0) {
  t <- gt::gt(dados)
  if (!is.null(titulo)) t <- gt::tab_header(t, title = titulo, subtitle = subtitulo)
  if (!is.null(numeros)) t <- gt::fmt_number(t, columns = dplyr::all_of(numeros),
                                             decimals = decimais, use_seps = TRUE)
  if (!is.null(fonte_dados)) t <- gt::tab_source_note(t, fonte_dados)
  t |>
    gt::opt_table_font(font = c("Georgia", "Gelasio", "serif")) |>
    gt::opt_row_striping() |>
    gt::tab_options(
      table.font.color = cores[["tinta"]],
      table.font.size = gt::px(14),
      table.border.top.color = cores[["verde"]],
      table.border.top.width = gt::px(2),
      heading.align = "left",
      heading.title.font.size = gt::px(18),
      heading.title.font.weight = "bold",
      heading.subtitle.font.size = gt::px(13),
      heading.border.bottom.color = "white",
      column_labels.font.weight = "bold",
      column_labels.border.top.color = "white",
      column_labels.border.bottom.color = cores[["laranja"]],
      column_labels.border.bottom.width = gt::px(2),
      row.striping.background_color = cores[["laranja_claro"]],
      table_body.hlines.color = "white",
      table_body.border.bottom.color = cores[["verde"]],
      source_notes.font.size = gt::px(12)
    ) |>
    gt::tab_style(gt::cell_text(color = cores[["verde"]]),
                  locations = list(gt::cells_title(), gt::cells_column_labels()))
}
