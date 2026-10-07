library(dplyr)
library(ggplot2)

set.seed(123)

df_peso <- tibble(
  peso = rnorm(n = 1500, mean = 70, sd = 10)
)

ggplot(df_peso, aes(x = peso)) +
  geom_histogram(aes(y = after_stat(density)),
                  bins = 30, fill = "steelblue", color = "white") +
  stat_function(fun = dnorm,
                args = list(mean = mean(df_peso$peso), sd = sd(df_peso$peso)),
                color = "darkred", linewidth = 1) +
  labs(title = "Histograma da variável Peso",
       subtitle = "Simulação de distribuição normal (n = 1500)",
       x = "Peso",
       y = "Densidade") +
  theme_minimal()
