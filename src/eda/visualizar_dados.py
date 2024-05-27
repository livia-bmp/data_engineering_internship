# eda/04_visualizar_dados.py
import pandas as pd
import os

def analisar_internet(df, writer):
    """
    Análise do arquivo 01_Utilizacao_da_Internet.csv.

    Args:
        df (pd.DataFrame): DataFrame com os dados do arquivo CSV.
        writer (pd.ExcelWriter): Objeto ExcelWriter para salvar os resultados.
    """
    df.rename(columns={'Brasil': 'Total'}, inplace=True)
    print(f"\n## Análise para 01_Utilizacao_da_Internet.csv (Pessoas que usaram internet por região)")

    # Seleciona as linhas a partir da linha 13 e todas as colunas
    df_temp = df.iloc[13:]

    # Salva a tabela na aba "Internet por Região H e M"
    df_temp.to_excel(writer, sheet_name='Internet por Região H e M', index=False)

    print(df_temp)


def analisar_celular(df, writer):
    """
    Análise do arquivo 03_Posse_de_Telefone_Movel_Celular.csv.

    Args:
        df (pd.DataFrame): DataFrame com os dados do arquivo CSV.
        writer (pd.ExcelWriter): Objeto ExcelWriter para salvar os resultados.
    """
    df.rename(columns={'Brasil': 'Total'}, inplace=True)
    print(f"\n## Análise para 03_Posse_de_Telefone_Movel_Celular.csv (Pessoas que possuem celular por região)")

    # Seleciona as linhas a partir da linha 13 e todas as colunas
    df_temp = df.iloc[13:]

    # Salva a tabela na aba "Celular por Região H e M"
    df_temp.to_excel(writer, sheet_name='Celular por Região H e M', index=False)

    print(df_temp)


def analisar_acesso_internet(df, writer):
    """
    Análise do arquivo 02_Equipamento_Utlizado_para_Acessar_a_Internet.csv.

    Args:
        df (pd.DataFrame): DataFrame com os dados do arquivo CSV.
        writer (pd.ExcelWriter): Objeto ExcelWriter para salvar os resultados.
    """
    df.rename(columns={'Brasil': 'Total'}, inplace=True)
    print(f"\n## Análise para 02_Equipamento_Utlizado_para_Acessar_a_Internet.csv (Acesso à internet por celular ou tablet)")

    # Seleciona as linhas 8, 9 e 10 e as colunas 'Total', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro_Oeste'
    df_temp = df.iloc[6:9, [0, 1, 2, 3, 4, 5, 6]]

    # Salva a tabela na aba "Internet por Celular ou Tablet"
    df_temp.to_excel(writer, sheet_name='Internet por Celular ou Tablet', index=False)

    print(df_temp)


def analisar_dados(diretorio):
    """
    Realiza análise exploratória dos dados em arquivos CSV e salva os resultados em um arquivo Excel.

    Args:
        diretorio: O caminho do diretório que contém os arquivos CSV.
    """

    writer = pd.ExcelWriter('analise_exploratoria.xlsx', engine='xlsxwriter')

    for filename in os.listdir(diretorio):
        if filename.endswith(".csv"):
            caminho_do_arquivo = os.path.join(diretorio, filename)
            df = pd.read_csv(caminho_do_arquivo)

            if filename == "01_Utilizacao_da_Internet.csv":
                analisar_internet(df, writer)
            elif filename == "03_Posse_de_Telefone_Movel_Celular.csv":
                analisar_celular(df, writer)
            elif filename == "02_Equipamento_Utlizado_para_Acessar_a_Internet.csv":
                analisar_acesso_internet(df, writer)

    writer.close()
    print(f"\nResultados salvos em analise_exploratoria.xlsx")

# Indicar diretório
diretorio_dados = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\saida"
analisar_dados(diretorio_dados)