import pandas as pd
import matplotlib.pyplot as plt

PATH = '/content/pre-os-gasolina/gasolina.csv'
df = pd.read_csv(PATH)

df.plot(kind='line', x='dia', y='venda')
plt.title('Valor de Venda Diaria da Gasolina')
plt.xlabel('Dia')
plt.ylabel('Valor')
plt.savefig('gasolina.png')
