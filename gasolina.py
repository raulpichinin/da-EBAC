import pandas as pd
import seaborn as sns

df_gasolina = pd.read_csv('gasolina.csv')

with sns.axes_style ('whitegrid'):
  grafico = sns.lineplot(df_gasolina, x="dia", y="venda")
  grafico.set(title="Preço médio da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021",xlabel="Dia", ylabel="Preço")


fig = grafico.get_figure()
fig.savefig('gasolina.png', dpi=300)
