import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

URL_SITE = "https://class.devsamurai.com.br/"

logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Bot:
    def __init__(self):
        self._service = Service(ChromeDriverManager().install())
        logging.info(f"ChromeDriver obtido com sucesso.")

        self._options = ChromeOptions()
        self._options.add_experimental_option("detach", True)
        logging.info(f"Configurações realizadas com sucesso.")

        self._bot = webdriver.Chrome(service = self._service, options = self._options)
        logging.info(f"Instância do ChromeDriver criada com sucesso.")

        self._bot.get(URL_SITE)
        logging.info(f"Acessando o endereço: {URL_SITE}.")

        self.cursos = self._bot.find_elements('xpath', "//ul/li/a")
        logging.info(f"Lista de elementos obtida com sucesso.")


    def run(self):
        try:
            logging.info(f"Início do processamento.")
            for curso in self.cursos:
                nome_curso = curso.text
                curso.click()
                logging.info(f"Download do curso {nome_curso} iniciado com sucesso.")
                sleep(1)
            logging.info(f"Fim do processamento.")
        except Exception as e:
            logging.error(f"Erro ao executar o processo: {e}")


if __name__ == "__main__":
    Bot().run()
