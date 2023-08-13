import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from bs4 import BeautifulSoup
from typing import List
from pandas import DataFrame, read_html

# Opciones
firefox_options = FireFoxOptions()
firefox_options.headless = True

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')

# Constantes
DRIVERS = {
    'firefox': webdriver.Firefox,
    'chrome': webdriver.Chrome,
}

HEADLESS = {
    'firefox': firefox_options,
    'chrome': chrome_options,
}

class TableExtractor:

    def __init__(self):
        self.browser = self.check_browsers()
        self.driver = DRIVERS[self.browser]

    def check_browsers(self) -> List[str]:
        """
        Verifica los navegadores diponibles y el primer driver disponible.
        """
        
        # Seleccion del navegador
        selected_browser = None
        for browser in DRIVERS.keys():
            # Si el driver abre el navegador se selecciona
            try:
                driver = DRIVERS[browser](options=HEADLESS[browser])
                selected_browser = browser
                break
            except Exception as e:
                print('error: ', e)
            finally:
                driver.quit()
        
        # Si no encuentra ningun driver especificado se termina el proceso
        if driver == None:
            sys.exit('No se encuentra ningun navegador compatible')

        return selected_browser
        

    def extract_html(self, url: str) -> BeautifulSoup:
        """
        Extrae el contenido html de la url procesado con BeautifulSoup.

        Argumentos:
        url -> URL de la pagina web.
        """
        driver = self.driver
        content = ''
        try:
            browser = driver(options=HEADLESS[self.browser])
            browser.get(url)
            content_raw = browser.page_source
            content = BeautifulSoup(content_raw, 'html.parser')
        except Exception as e:
            print('error: ', e)
        finally:
            browser.quit()

        return content
    

    def extract_tables(self, url: str) -> List[DataFrame]:
        """
        Retorna una lista de dataframes extraidos a partir de elementos table en la pagina web.

        Argumentos:
        url -> URL de la pagina web
        """
        content = self.extract_html(url)
        tables = content.find_all('table')
        dataframes = read_html(str(tables))

        return dataframes
        