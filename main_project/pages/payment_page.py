from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    finish_button = "#finish"


    #Getters - возвращают значения

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.finish_button)))


    #Actions - наши действия

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click Finish button")


    # Methods - наши методы (шаги)


    def payment(self):
        self.get_current_url()
        self.click_finish_button()

