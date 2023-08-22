import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Test1:
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        time.sleep(1)
        driver.close()


test = Test1()
test.test_select_product()
