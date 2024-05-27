from extracao_dados import extrair_dados
from tratamento_dados import limpar_dados_xlsx
from conveter_arquivos import converter_xlsx_para_csv
from visualizar_dados import analisar_dados

def main():
    # Extrai os dados do site do IBGE
    extrair_dados()

    # Limpa os dados dos arquivos XLSX
    diretorio_entrada = r"C:\\Users\\Usuario\Downloads\\data_engineering_internship\\src\\arquivos\\entrada"
    limpar_dados_xlsx(diretorio_entrada)

    # Converte os arquivos XLSX para CSV
    diretorio_saida = r"C:\\Users\\Usuario\\Downloads\\data_engineering_internship\\src\\arquivos\\saida"
    converter_xlsx_para_csv(diretorio_entrada, diretorio_saida)

    # Analisa os dados dos arquivos CSV
    analisar_dados(diretorio_saida)

    print("Processamento concluído com sucesso!")

if __name__ == "__main__":
    main()