from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

# Primeiro clique
text_box = driver.find_element(by=By.XPATH, value="/html/body/main/section/div[2]/div/div/section/div/div[2]/ul/li/ul/li[1]")
text_box.click()

# Segundo clique
text_box = driver.find_element(by=By.XPATH, value="/html/body/main/section/div[2]/div/div/section/div/div[2]/ul/li/ul/li[1]/ul/li[6]/div")
text_box.click()

# Terceiro clique
text_box = driver.find_element(by=By.XPATH, value='//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados_anchor"]')
time.sleep(3)
text_box.click()

# Quarto clique 
text_box = driver.find_element(by=By.XPATH, value='//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx_anchor"]')
time.sleep(3)
text_box.click()

# Quinto clique
text_box = driver.find_element(by=By.XPATH, value='//*[@id="Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/xlsx/01_Pessoas_de_10_Anos_ou_Mais_de_Idade_anchor"]')
text_box.click()
time.sleep(3)

# Sexto clique - arquivo01
text_box = driver.find_element(by=By.XPATH, value='//*[@id="j1_745_anchor"]')
text_box.click()
time.sleep(3)

# Sétimo clique - arquivo02
text_box = driver.find_element(by=By.XPATH, value='//*[@id="j1_746_anchor"]')
text_box.click()
time.sleep(3)

# Oitavo clique - arquivo03
text_box = driver.find_element(by=By.XPATH, value='//*[@id="j1_747_anchor"]')
text_box.click()
time.sleep(3)

driver.quit()