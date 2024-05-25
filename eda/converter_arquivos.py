import os
import glob
import pandas as pd

input_folder = r"C:\\Users\\Usuario\\OneDrive\\Área de Trabalho\\data_engineering_internship\\eda"
output_folder = r"C:\\Users\\Usuario\\OneDrive\\Área de Trabalho\\data_engineering_internship\\eda"
#path = os.getcwd() 

# Define o tipo de arquivo de entrada e saída que deseja converter
input_extension = '*.xlsx'
output_extension = '.csv'

# Lista todos os arquivos de entrada
input_folder = os.path.join(os.path.expanduser('~'),'OneDrive\Área de Trabalho\data_engineering_internship\eda')
input_files = glob.glob(os.path.join(input_folder, '*.xlsx'))

# Cria o diretório de saída se não existir
os.makedirs(output_folder, exist_ok=True)
# Loop pelos arquivos de entrada
for file in input_files:
    # Lê todas as abas do arquivo xlsx com a biblioteca pandas
    xlsx = pd.ExcelFile(file)
    
    # Inicializa um DataFrame vazio para armazenar os dados concatenados
    all_data = pd.DataFrame()
    
    # Itera sobre as abas do arquivo, pulando as abas 1 e 2 (índices 0 e 1)
    for sheet_index, sheet_name in enumerate(xlsx.sheet_names):
        if sheet_index < 2:
            continue  # Pula as abas 1 e 2

        df = pd.read_excel(file, sheet_name=sheet_name)
        if not df.empty:
            # Concatena os dados da aba atual ao DataFrame geral
            df.head()
            all_data = pd.concat([all_data, df], ignore_index=True)
    
    # Define o nome e o caminho do arquivo de saída
    output_file = os.path.splitext(os.path.basename(file))[0] + output_extension
    output_path = os.path.join(output_folder, output_file)
    
    # Salva o DataFrame concatenado no arquivo de saída
    all_data.to_csv(output_path, sep=';', index=False, encoding='utf-8')
    print(f"Converted {file} to {output_path}")