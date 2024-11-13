import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

intervalos = [(300, 400), (400, 500), (500, 600), (600, 700), (700, 800),
              (800, 900), (900, 1000), (1000, 1100), (1100, 1200)]
frequencias = [14, 46, 58, 76, 68, 62, 48, 22, 6]

#CONSTRUÇÃO DA TABELA:
marcas_de_classe = [(limite[0] + limite[1]) / 2 for limite in intervalos]
dados_expandidos = []
for marca, freq in zip(marcas_de_classe, frequencias):
 dados_expandidos.extend([marca] * freq)

df_dados = pd.DataFrame(dados_expandidos, columns=['Área'])


media = df_dados['Área'].mean() #CALCULO DA MÉDIA, MODA E MEDIANA:
moda = df_dados['Área'].mode()[0]  #OBS: Pode haver mais de uma moda; pegamos a primeira.
mediana = df_dados['Área'].median()

print(f"Média: {media}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")

desvio_padrao = df_dados['Área'].std() #AQUI CALCULA O DESVIO PADRÃO.
print(f"Desvio Padrão: {desvio_padrao}")

q1 = df_dados['Área'].quantile(0.25) #CALCULO DOS QUANTIS, DECIS, PERCENTIS:
d3 = df_dados['Área'].quantile(0.3)
d7 = df_dados['Área'].quantile(0.7)
p15 = df_dados['Área'].quantile(0.15)
p90 = df_dados['Área'].quantile(0.9)

print(f"\nQ1 (25º percentil): {q1}")
print(f"D3 (30º percentil): {d3}")
print(f"D7 (70º percentil): {d7}")
print(f"P15 (15º percentil): {p15}")
print(f"P90 (90º percentil): {p90}")

plt.figure(figsize=(10, 6)) #AQUI VAMOS CONTRUIR O GRÁFICO:
sns.barplot(x=[f"{lim[0]} - {lim[1]}" for lim in intervalos], y=frequencias)
plt.title("Distribuição de Frequência das Áreas dos Lotes")
plt.xlabel("Intervalos de Área (m²)")
plt.ylabel("Número de Lotes")
plt.show()