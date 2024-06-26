from extracao_dados import extrair_dados
from tratamento_dados import limpar_dados_xlsx
from conveter_arquivos import converter_xlsx_para_csv
from visualizar_dados import analisar_dados
import time 

   # CASO O MAIN NÃO FUNCIONE DE PRIMEIRA:
   # RODAR POR PRIMEIRO ARQUIVO SECUNDÁRIO planoB.py seguir as mesmas instruções que para o arquivo extracao_dados.py
   # CLICAR PARA RODAR O **MAIN** NOVAMENTE

def main():
    # Extrai os dados do site do IBGE
    extrair_dados()

    # Inicialmente era pra ele fazer scroll down automaticamente até achar os botões em que precisa clicar no site
    # nao foi possivel até o momento configurar por completo essa função portanto
    # É NECESSÁRIO QUANDO INICIAR O CHROME: `fazer scrolldown manualmente até os botões aparecerem na pagina do IBGE`

    # Aguarda 30 segundos antes de continuar
    time.sleep(30)

    # Limpa os dados dos arquivos XLSX
    diretorio_entrada = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\entrada"
    limpar_dados_xlsx(diretorio_entrada)

    # Converte os arquivos XLSX para CSV
    diretorio_saida = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\saida"
    converter_xlsx_para_csv(diretorio_entrada, diretorio_saida)

    # Analisa os dados dos arquivos CSV
    analisar_dados(diretorio_saida)

    print("Processamento concluído com sucesso!")

if __name__ == "__main__":
    main()