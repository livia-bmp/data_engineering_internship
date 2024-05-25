# Importando a biblioteca necessária
import pandas as pd

# Leitura do arquivo Excel
wb = pd.read_excel('01_Utilizacao_da_Internet.xlsx')

# Conversão da planilha para DataFrame
df = pd.DataFrame(wb)

# Salvar o DataFrame como arquivo CSV
df.to_csv('01_Utilizacao_da_Internet.csv', sep=';', index=False, encoding='utf-8')