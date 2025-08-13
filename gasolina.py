
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

plt.title('Preço da gasolina por dia', fontsize=16)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)
plt.grid(True)

plt.savefig('gasolina.png')

plt.show()
