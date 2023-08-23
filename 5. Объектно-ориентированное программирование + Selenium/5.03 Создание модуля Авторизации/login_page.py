from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        username = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name")))
        username.send_keys(login_name)
        print("Input login")

        user_password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
        user_password.send_keys(login_password)
        print("Input password")

        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
        button_login.click()
        print("Click login button")
