import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = [
   61, 65, 43, 53, 55, 51, 58, 59, 56, 59,
   52, 63, 49, 68, 51, 50, 67, 62, 64, 48,
   53, 48, 56, 45, 54, 51, 53, 52, 55, 55,
   53, 46, 54, 51, 71, 57, 55, 54, 55, 48,
   55, 46, 57, 54, 48, 63, 57, 52, 55, 51
]

#TABELA DE DISTRIBUIÇÃO DE FRENQUENCIA:
amplitude = 5
classes = 7
intervalo_min = min(dados)
intervalo_max = intervalo_min + classes * amplitude
intervalos = pd.interval_range(start=intervalo_min, end=intervalo_max, freq=amplitude)
frequencias = pd.cut(dados, bins=intervalos).value_counts().sort_index()

tabela_freq = pd.DataFrame({
   'Intervalo': [str(i) for i in frequencias.index],
   'Frequência': frequencias.values
})

print("Tabela de Distribuição de Frequência:")
print(tabela_freq)

media = np.mean(dados) #CALCULO DA MÉDIA, MODA E MEDIANA:
moda = pd.Series(dados).mode()[0]
mediana = np.median(dados)

print(f"\nMédia: {media}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")

desvio_padrao = np.std(dados, ddof=1) #3.CÁLCULO DO DESVIO PADRÃO:

print(f"\nDesvio Padrão: {desvio_padrao}")

q1 = np.percentile(dados, 25) #QUANTIS.
d3 = np.percentile(dados, 30) #DECIS.
d7 = np.percentile(dados, 70) #DECIS.
p15 = np.percentile(dados, 15) #PERCENTIS.
p90 = np.percentile(dados, 90) #PERCENTIS.

print(f"\nQ1 (25º percentil): {q1}")
print(f"D3 (30º percentil): {d3}")
print(f"D7 (70º percentil): {d7}")
print(f"P15 (15º percentil): {p15}")
print(f"P90 (90º percentil): {p90}")

plt.figure(figsize=(10, 6)) #CONSTRUÇÃO DE UM GRÁFICO DE TABELA:
sns.barplot(x='Intervalo', y='Frequência', data=tabela_freq)
plt.title('Distribuição de Frequência')
plt.xlabel('Intervalos')
plt.ylabel('Frequência')
plt.show()