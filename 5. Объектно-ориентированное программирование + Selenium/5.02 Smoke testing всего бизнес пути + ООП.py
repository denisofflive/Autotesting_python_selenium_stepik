import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test1:
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("Start Test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        username = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name")))
        username.send_keys(login_standard_user)
        print("Input login")

        user_password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
        user_password.send_keys(password_all)
        print("Input password")

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
        button_login.click()
        print("Click login button")

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        select_product.click()
        print("Click")

        enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopping_cart_container")))
        enter_shopping_cart.click()
        print("Click Enter Shopping_cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".title")))
        value_success_test = success_test.text
        print(value_success_test)
        assert value_success_test == "Your Cart"
        print("Test Success!!!!")

        time.sleep(1)
        driver.close()


test = Test1()
test.test_select_product()
