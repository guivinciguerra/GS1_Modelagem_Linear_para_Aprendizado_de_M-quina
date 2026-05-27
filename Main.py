import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("satcat.csv")
coluna1 = "launch_year"
intervalos = [1956, 1970, 1984, 1998, 2012, 2026]
freq1 = pd.cut(
    df[coluna1],
    bins=intervalos
).value_counts().sort_index()
tabela1 = pd.DataFrame({
    "Ano de lancamento": freq1.index.astype(str),
    "Frequencia": freq1.values,
    "Freq. Relativa (%)":
        (freq1.values / freq1.values.sum()) * 100
})
tabela1["Freq. Relativa (%)"] = \
    tabela1["Freq. Relativa (%)"].round(2)
print(f"\nTabela de frequencia - ano de lancamento dos satelites")
print(tabela1)

coluna2 = "inclination_deg"
freq2 = pd.cut(
    df[coluna2],
    bins=5
).value_counts().sort_index()
tabela2 = pd.DataFrame({
    "Faixa em graus ": freq2.index.astype(str),
    "Frequencia": freq2.values,
    "Freq. Relativa (%)":
        (freq2.values / freq2.values.sum()) * 100
})
tabela2["Freq. Relativa (%)"] = \
    tabela2["Freq. Relativa (%)"].round(2)
print(f"Inclinacao dos satelites em relacao a terra ")
print(tabela2)


df = pd.read_csv("satcat.csv")
frequencia = df["state"].value_counts()
top8 = frequencia.head(8)
outros = frequencia.iloc[8:].sum()
top8["Outros"] = outros
nomes = {
    "US": "Estados Unidos",
    "SU": "Uniao Sovietica",
    "CN": "China",
    "RU": "Russia",
    "IN": "India",
    "J": "Japao",
    "F": "Franca",
    "UK": "Reino Unido",
    "Outros": "Outros"
}
labels = [nomes.get(i, i) for i in top8.index]
plt.figure(figsize=(8,8))
plt.pie(
    top8,
    labels=labels,
    autopct='%1.1f%%'
)
plt.title("Países que mais lancaram satelites artificiais na historia")
plt.show()

df = df[df["launch_year"] >= 1992]
frequencia = df["state"].value_counts()
top8 = frequencia.head(7)
outros = frequencia.iloc[7:].sum()
top8["Outros"] = outros
nomes = {
    "US": "Estados Unidos",
    "SU": "Uniao Sovietica",
    "RU": "Russia",
    "CN": "China",
    "IN": "India",
    "J": "Japao",
    "F": "Franca",
    "UK": "Reino Unido",
    "Outros": "Outros"
}
labels = [nomes.get(i, i) for i in top8.index]
plt.figure(figsize=(8,8))
plt.pie(
    top8,
    labels=labels,
    autopct='%1.1f%%'
)
plt.title("Países que mais lancaram satelites artificiais apos Guerra Fria (1991 - dias atuais)")
plt.show()
df = pd.read_csv("satcat.csv")
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=["perigee_km", "apogee_km"])
df = df[
    (df["perigee_km"] >= 0) &
    (df["apogee_km"] >= 0)
]


colunas = ["perigee_km", "apogee_km"]
for nome in colunas:
    coluna = df[nome]
    nomes = {
    "perigee_km": "Menor ponto de distancia entre o satelite e a Terra",
    "apogee_km": "Maior ponto de distancia entre o satelite e a Terra"
}
    print("\n===================================")
    print   (nomes[nome])
    print("===================================")
    media = coluna.mean()
    mediana = coluna.median()
    moda = coluna.mode()[0]
    print("\nMEDIDAS DE TENDENCIA CENTRAL")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda:.2f}")
    maximo = coluna.max()
    minimo = coluna.min()
    amplitude = maximo - minimo
    variancia = coluna.var()
    desvio_padrao = coluna.std()
    coef_variacao = (desvio_padrao / media) * 100
    print("\nMEDIDAS DE DISPERSAO")
    print(f"Maximo: {maximo:.2f}")
    print(f"Minimo: {minimo:.2f}")
    print(f"Amplitude: {amplitude:.2f}")
    print(f"Variancia: {variancia:.2f}")
    print(f"Desvio Padrao: {desvio_padrao:.2f}")
    print(f"Coeficiente de Variacao: {coef_variacao:.2f}%")
    quartis = coluna.quantile([0.25, 0.50, 0.75])
    print("\nMEDIDAS SEPARATRIZES")
    print(f"Q1 (25%): {quartis[0.25]:.2f}")
    print(f"Q2 (50%): {quartis[0.50]:.2f}")
    print(f"Q3 (75%): {quartis[0.75]:.2f}")