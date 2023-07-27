import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.maximize_window()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
time.sleep(3)
driver.close()



