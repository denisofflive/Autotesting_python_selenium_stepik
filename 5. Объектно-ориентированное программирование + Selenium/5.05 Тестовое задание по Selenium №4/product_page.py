from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage

class ProductPage(LoginPage):

    def check_product_page(self):
        products_word = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".title")))
        value_products_word = products_word.text
        assert value_products_word == 'Products'
        print('We are on the Products Page')

    def log_out(self):
        menu_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#react-burger-menu-btn")))
        menu_button.click()
        log_out_link = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#logout_sidebar_link")))
        log_out_link.click()