from time import sleep
from pathlib import Path
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Definindo as Variaveis de ambiente
ROOT_FOLDER = Path(__file__).parent
ROOT_FILE = ROOT_FOLDER / 'chromedriver.exe'
ROOT_CHROME_DRIVER = str(ROOT_FILE)
URL_MAIN = str('https://www.worldometers.info/geography/flags-of-the-world/')
LISTA_DADOS = []
LISTA_NAMES = []

''' CONFIGURANDO AS DEFINIÇÕES DE ACESSOS HTTP'''

# Configurando as conexões de serviço
service = Service(executable_path=ROOT_CHROME_DRIVER)

# Configurando as options do webdriver
options = Options()
options.add_argument('window-size=1920,1080')

# Configurando o browser e URL de Acesso
browser = webdriver.Chrome(service=service, options=options)
browser.get(URL_MAIN)
sleep(1)


def return_flags(lista_dados):
    elemento = browser.find_elements(By.XPATH, '//div[@class="col-md-4"]')
    cont = 1
    for rows in elemento:
        find = rows.find_elements(By.TAG_NAME, 'a')
        for finds in find:
            result = finds.get_attribute('href')
            lista_dados.append(result)
            print(f'{result} - {cont}')
            cont += 1
    return lista_dados


def return_names(lista_names):
    name = browser.find_elements(By.XPATH, '//div[@style="font-weight:bold; padding-top:10px"]')
    cont = 1
    for names in name:
        result2 = names.text
        lista_names.append(result2)
        print(f'{result2} - {cont}')
        cont += 1

    return lista_names


def save_to_excel(lista_dados, lista_names):

    df = pd.DataFrame({'Country_Name': lista_names, 'Country_URL': lista_dados})
    caminho_excel = Path(__file__).parent/'countrys.xlsx'
    df.to_excel(caminho_excel, index=False)

    return None


return_flags(LISTA_DADOS)
return_names(LISTA_NAMES)
save_to_excel(LISTA_DADOS, LISTA_NAMES)
