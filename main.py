from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Bot:
    def __init__(self):
        # Configurações do webdriver
        self._service = Service(ChromeDriverManager().install())
        self._options = ChromeOptions()
        self._options.add_experimental_option("detach", True)
        self._bot = webdriver.Chrome(service = self._service, options = self._options)
        
        # Obtém os elementos 
        self._bot.get('https://class.devsamurai.com.br/')
        self.cursos = self._bot.find_elements('xpath', "//ul/li/a")


    def run(self):
        try:
            for curso in self.cursos:
                nome_curso = curso.text
                curso.click()
                
                print(f'Download do curso {nome_curso} iniciado com sucesso.')
                sleep(1)
            
            print(f'Fim do processamento.')
        except Exception as e:
            print(e)


Bot().run()
