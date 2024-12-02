import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Dados dos rendimentos para cada fertilizante
grupo_A = [20, 22, 19, 21, 20]
grupo_B = [25, 27, 26, 24, 28]
grupo_C = [22, 23, 21, 20, 24]

# 1. Estatística ANOVA
F, p_value = stats.f_oneway(grupo_A, grupo_B, grupo_C)

# 2. Resultados
print("Estatística F:", F)
print("Valor p:", p_value)

# Decisão
alpha = 0.05
if p_value < alpha:
    print("Rejeitamos a hipótese nula: Existe diferença significativa entre os grupos.")
else:
    print("Não rejeitamos a hipótese nula: Não há evidência suficiente para diferenças significativas entre os grupos.")

# 3. Visualização dos dados (boxplot)
plt.figure(figsize=(8, 6))
plt.boxplot([grupo_A, grupo_B, grupo_C], labels=["Fertilizante A", "Fertilizante B", "Fertilizante C"])
plt.title("Distribuição dos Rendimentos por Grupo")
plt.ylabel("Rendimentos (ton/ha)")
plt.xlabel("Grupos")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
