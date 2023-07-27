import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.maximize_window()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

time.sleep(3)
driver.close()

