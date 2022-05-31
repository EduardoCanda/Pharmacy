from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SHOPPING_GOOGLE_URL = f'https://shopping.google.com.br/search?q='


def execute():
    with open(file='file.txt', mode='r', encoding='utf-8') as file:
        content = file.read()
        lines = content.split('\n')
        address = lines[0].replace('Address:', '').strip()
        medicament = lines[1].replace('Medicament:', '').strip()
        print(address, medicament)

    service = Service(ChromeDriverManager(path=r'./chromedriver').install())
    driver = webdriver.Chrome(executable_path=service.path)

    driver.get(SHOPPING_GOOGLE_URL+medicament)


if __name__ == '__main__':
    execute()
