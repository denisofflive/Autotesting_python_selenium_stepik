from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from main_project.base.base_class import Base
from main_project.utils.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    select_product_1 = "#add-to-cart-sauce-labs-backpack"
    select_product_2 = "#add-to-cart-sauce-labs-bolt-t-shirt"
    select_product_3 = "#add-to-cart-sauce-labs-fleece-jacket"
    cart = "#shopping_cart_container"
    menu = "#react-burger-menu-btn"
    link_about = '#about_sidebar_link'


    #Getters - возвращают значения

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.link_about)))

    #Actions - наши действия

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Select Product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click Select Product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click Select Product 3")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click Menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click Link About")

    # Methods - наши методы (шаги)


    def select_products_1(self):
        with allure.step("Select Products 1"):
            Logger.add_start_step(method="select_products_1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        with allure.step("Select Menu About"):
            self.get_current_url()
            self.click_menu()
            self.click_link_about()
            self.assert_url('https://saucelabs.com/')
