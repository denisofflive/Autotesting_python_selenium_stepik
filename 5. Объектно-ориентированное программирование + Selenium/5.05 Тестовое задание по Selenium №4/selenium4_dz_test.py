import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from product_page import ProductPage


class Test_4_Users_Auth:

    def login_logout(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print('Start Test')

        list_login_user = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        password_all = 'secret_sauce'

        login = LoginPage(driver)
        for i in list_login_user:
            login.authorization(i, password_all)
            time.sleep(5)
            if i == 'locked_out_user':
                user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name")))
                user_name.send_keys(Keys.BACKSPACE * 15)
                print("Clear login")

                password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
                password.send_keys(Keys.BACKSPACE * 12)
                print("Clear password")
                continue

            check = ProductPage(driver)
            check.check_product_page()

            logout = ProductPage(driver)
            logout.log_out()
            print('Test is Over!')


test = Test_4_Users_Auth()
test.login_logout()
