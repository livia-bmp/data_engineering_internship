# eda/02_tratamento_dados.py

import pandas as pd
import os
import re

def limpar_dados_xlsx(diretorio):
    """
    Identifica os headers e limpa os dados em branco ou nulo de todos os arquivos XLSX em um diretório.

    Args:
        diretorio: O caminho do diretório que contém os arquivos XLSX.

    Returns:
        Uma lista de DataFrames Pandas com os dados limpos.
    """

    dataframes_limpos = []
    for filename in os.listdir(diretorio):
        if filename.endswith(".xlsx"):
            caminho_do_arquivo = os.path.join(diretorio, filename)
            try:
                # Carrega o arquivo XLSX em um DataFrame Pandas
                df = pd.read_excel(caminho_do_arquivo, sheet_name=None)

                # Mantém apenas a terceira aba
                abas = list(df.keys())
                if len(abas) >= 3:
                    df = {abas[2]: df[abas[2]]}  # Seleciona a terceira aba
                    aba_nome = list(df.keys())[0]  # Obtém o nome da aba do dicionário
                    df_aba = df[aba_nome]  # Obtém o DataFrame da aba

                # Remove as quatro primeiras linhas
                df_aba = df_aba.iloc[4:].reset_index(drop=True)

                # Limpa os dados em branco ou nulo
                # Só aplica dropna para arquivos que não começam com "02_"
                if not filename.startswith("02_"):
                    df_aba.dropna(inplace=True)
                df_aba.replace('', pd.NA, inplace=True)

                # Exclui a última linha para arquivos que começam com "02_"
                if filename.startswith("02_"):
                    df_aba = df_aba.iloc[:-2]  # Remove a última linha

                # Substitui acentos e normaliza o encoding
                df_aba = df_aba.applymap(lambda x: re.sub(r'[áàãâäÁÀÃÂÄ]', 'a', str(x)))
                df_aba = df_aba.applymap(lambda x: re.sub(r'[éèêëÉÈÊË]', 'e', str(x)))
                df_aba = df_aba.applymap(lambda x: re.sub(r'[íìîïÍÌÎÏ]', 'i', str(x)))
                df_aba = df_aba.applymap(lambda x: re.sub(r'[óòõôöÓÒÕÔÖ]', 'o', str(x)))
                df_aba = df_aba.applymap(lambda x: re.sub(r'[úùûüÚÙÛÜ]', 'u', str(x)))
                df_aba = df_aba.applymap(lambda x: re.sub(r'[çÇ]', 'c', str(x)))
                df_aba = df_aba.applymap(lambda x: str(x).encode('latin-1', 'ignore').decode('utf-8'))

                # Complementa o header com as informações nas colunas existentes
                novas_colunas = ['Brasil', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro_Oeste']
                for i, coluna in enumerate(novas_colunas, start=1):
                         if i > 0:  
                             df_aba.rename(columns={df_aba.columns[i]: coluna}, inplace=True)

                # Exclui colunas após a 7ª coluna
                df_aba = df_aba.iloc[:, :7]
                              
                # **Ajustando a parte para deixar os dados nulos em branco:**
                df_aba.fillna('', inplace=True)

                # Salva o DataFrame no arquivo original
                df_aba.to_excel(caminho_do_arquivo, index=True)                  
          
                dataframes_limpos.append(df_aba)
            except FileNotFoundError:
                print(f"O arquivo {filename} não foi encontrado.")

    return dataframes_limpos

# Difinir diretório
diretorio = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\entrada"
dataframes_limpos = limpar_dados_xlsx(diretorio)

# Ao final indicar que foi concluido!
print('Arquivos limpos com sucesso!')