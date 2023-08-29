from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    select_product_1 = "#add-to-cart-sauce-labs-backpack"
    cart = "#shopping_cart_container"


    #Getters - возвращают значения

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart)))


    #Actions - наши действия

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Select Product 1")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    # Methods - наши методы (шаги)


    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
