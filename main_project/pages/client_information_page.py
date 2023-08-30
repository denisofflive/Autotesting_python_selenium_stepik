from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from main_project.base.base_class import Base
from main_project.utils.logger import Logger


class Client_inforamtion_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    first_name = "#first-name"
    last_name = "#last-name"
    postal_code = "#postal-code"
    continue_button = "#continue"



    #Getters - возвращают значения

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.continue_button)))


    #Actions - наши действия

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input First Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input Postal Code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue Button")

    # Methods - наши методы (шаги)


    def input_information(self):
        with allure.step("Input Information"):
            Logger.add_start_step(method="input_information")
            self.get_current_url()
            self.input_first_name("Denis")
            self.input_last_name("Denisov")
            self.input_postal_code("1234")
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_information")






