# eda/03_conveter_arquivos.py

import pandas as pd
import os

def converter_xlsx_para_csv(input_dir, output_dir):
    """
    Converte arquivos .xlsx para .csv, excluindo a primeira coluna de cada arquivo
    e renomeando a primeira linha da primeira coluna.

    Args:
        input_dir (str): Caminho do diretório de entrada com os arquivos .xlsx.
        output_dir (str): Caminho do diretório de saída para os arquivos .csv.
    """
    # Iterar por todos os arquivos .xlsx no diretório de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith(".xlsx"):
            # Caminho completo do arquivo
            filepath = os.path.join(input_dir, filename)

            # Carregar o arquivo .xlsx como DataFrame
            df = pd.read_excel(filepath)

            # Excluir a primeira coluna
            df = df.iloc[:, 1:]

            # Renomear a primeira linha da primeira coluna
            if filename.startswith("01_"):
                df.columns = ["Pessoas que usaram internet por regiao"] + list(df.columns[1:])
            elif filename.startswith("02_"):
                df.columns = ["Acesso à internet por celular ou tablet"] + list(df.columns[1:])
            elif filename.startswith("03_"):
                df.columns = ["Pessoas que possuem celular por regiao"] + list(df.columns[1:])

            # Nome do arquivo de saída (sem a extensão .xlsx)
            output_filename = os.path.splitext(filename)[0] + ".csv"
            # Caminho completo do arquivo de saída
            output_filepath = os.path.join(output_dir, output_filename)

            # Salvar o DataFrame como arquivo .csv
            df.to_csv(output_filepath, index=False)

            print(f"Arquivo {filename} convertido para CSV e salvo em {output_filepath}")

# Diretorios
input_dir = "C:\\Users\\Usuario\\Downloads\\data_engineering_internship\\src\\arquivos\\entrada"
output_dir = "C:\\Users\\Usuario\\Downloads\\data_engineering_internship\\src\\arquivos\\saida"

converter_xlsx_para_csv(input_dir, output_dir)