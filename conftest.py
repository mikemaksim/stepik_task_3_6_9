import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Further development
"""
button_values = {'ar': 'أضف الى سلة التسوق', 'ca': 'Afegeix a la cistella',
'cs': 'Vložit do košíku', 'da': 'Læg i kurv',
'de': 'In Warenkorb legen', 'en-gb': 'Add to basket',
'el': 'Προσθήκη στο καλάθι', 'es': 'Añadir al carrito',
'fi': 'Lisää koriin', 'fr': 'Ajouter au panier',
'it': 'Aggiungi al carrello', 'ko': '장바구니 담기',
'nl': 'Voeg aan winkelmand toe', 'pl': 'Dodaj do koszyka',
'pt': 'Adicionar ao carrinho', 'pt-br': 'Adicionar à cesta',
'ro': 'Adauga in cos', 'ru': 'Добавить в корзину',
'sk': 'Pridať do košíka', 'uk': 'Додати в кошик'}
"""

# languages = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']


def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store', default = "chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default = "en-gb",
                     help = "Choose your language")


@pytest.fixture(scope="function")
def browser(request):
    
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options = options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options = options)
        
    yield browser
    
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()
