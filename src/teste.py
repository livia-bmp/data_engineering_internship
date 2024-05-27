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

    #extracao dos dados
    # Definido o caminho para download
    diretorio_entrada = r"C:\Users\Usuario\OneDrive\Área de Trabalho\data_engineering_internship\src\arquivos\entrada"

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

    # Função para clicar em um elemento pelo XPath
    def clicar_elemento(xpath):
        text_box = driver.find_element(by=By.XPATH, value=xpath)
        text_box.click()
        time.sleep(3)

    # Clicar nos elementos na sequência correta
    clicar_elemento("/html/body/main/section/div[2]/div/div/section/div/div[2]/ul/li/ul/li[1]") 
    clicar_elemento("/html/body/main/section/div[2]/div/div/section/div/div[2]/ul/li/ul/li[1]/ul/li[6]/div")
    clicar_elemento('//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados_anchor"]')
    clicar_elemento('//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx_anchor"]')
    clicar_elemento('//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor"]')

    # Clicar nos arquivos específicos
    clicar_elemento('//*[@id="j1_745_anchor"]') # arquivo01
    clicar_elemento('//*[@id="j1_746_anchor"]') # arquivo02
    clicar_elemento('//*[@id="j1_747_anchor"]') # arquivo03

    driver.quit()