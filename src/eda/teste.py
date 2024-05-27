from extracao_dados import extrair_dados
from tratamento_dados import limpar_dados_xlsx
from conveter_arquivos import converter_xlsx_para_csv
from visualizar_dados import analisar_dados
import time
import os

def main():
    # Define os diretórios de entrada e saída
    diretorio_entrada = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\entrada"
    diretorio_saida = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\saida"

    # Cria os diretórios de entrada e saída se eles não existirem
    os.makedirs(diretorio_entrada, exist_ok=True)
    os.makedirs(diretorio_saida, exist_ok=True)

    # Extrai os dados do site do IBGE
    extrair_dados()

    # Inicialmente era pra ele fazer scroll down automaticamente até achar os botões em que precisa clicar no site
    # nao foi possivel até o momento configurar por completo essa função portanto
    # É NECESSÁRIO QUANDO INICIAR O CHROME: `fazer scrolldown manualmente até os botões aparecerem na pagina do IBGE`

    # Aguarda 30 segundos antes de continuar
    time.sleep(30)

    # Limpa os dados dos arquivos XLSX
    limpar_dados_xlsx(diretorio_entrada)

    # Converte os arquivos XLSX para CSV
    converter_xlsx_para_csv(diretorio_entrada, diretorio_saida)

    # Analisa os dados dos arquivos CSV
    analisar_dados(diretorio_saida)

    print("Processamento concluído com sucesso!")

if __name__ == "__main__":
    main()