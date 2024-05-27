# eda/01_extracao_dados.py

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def extrair_dados():
    """
    Extrai os arquivos de dados do site do IBGE.
    """
    
    # Definido o caminho para download alterar conforme o usuário
    diretorio_entrada = r"C:\Users\Usuario\Downloads\data_engineering_internship\src\arquivos\entrada"

    # Configura o Chrome e definir a pasta de download
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": diretorio_entrada,
        "download.prompt_for_download": False,  # Não pedir confirmação para download
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Inicializar o WebDriver do Chrome com as opções configuradas
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html")
    driver.implicitly_wait(5)


    # Maximiza a janela do navegador
    # driver.maximize_window()  # Você pode remover essa linha se não precisar maximizar
    time.sleep(4)

    #inicialmente era pra ele fazer scroll down automaticamente até achar os botões em que precisa clicar
    #nao foi possivel até o momento configurar por completo essa função por isso 
    # É NECESSÁRIO QUANDO INICIAR O CHROME: `fazer scrolldown manualmente até os botões aparecerem na pagina do IBGE`

    # Função para clicar em um elemento
    def scroll_and_click(xpath):
        text_box = driver.find_element(by=By.XPATH, value=xpath)
        text_box.click()

    # Primeiro clique 
    text_box = driver.find_element(by=By.XPATH, value="/html/body/main/section/div[2]/div/div/section/div/div[2]/ul/li/ul/li[1]")
    text_box.click()
    time.sleep(5)

    # Cliques com scroll 
    scroll_and_click('//*[@id="Acesso_a_internet_e_posse_celular/2015"]/div')
    scroll_and_click('//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados_anchor"]')
    scroll_and_click('//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx_anchor"]')
    scroll_and_click('//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor"]')
    time.sleep(3)
    scroll_and_click('//*[@id="j1_745_anchor"]')
    scroll_and_click('//*[@id="j1_746_anchor"]')
    scroll_and_click('//*[@id="j1_747_anchor"]')

    time.sleep(8)  # Aguardar o download
    
    driver.quit()