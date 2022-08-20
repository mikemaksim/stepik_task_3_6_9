from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.get(link)
    browser.implicitly_wait(7)
    button = browser.find_elements( By.CSS_SELECTOR, 'button.btn-add-to-basket')
    
    assert button, "Error: 'Add to basket' button not found!"