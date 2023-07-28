import time
from selenium import webdriver
"""Keys - работа с клавишами на клавиатуре"""
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

username = driver.find_element(By.CSS_SELECTOR, "#user-name")
username.send_keys(login_standard_user)
print("Input login")
"""Удаляет один символ с конца т.е. получится standard_use, 
а для того, чтобы удалить несколько символов, можно написать
username.send_keys(Keys.BACKSPACE * 10)"""
username.send_keys(Keys.BACKSPACE)
"""Вставим стёртый символ r"""
username.send_keys("r")

user_password = driver.find_element(By.CSS_SELECTOR, "#password")
user_password.send_keys(password_all)
print("Input password")
"""RETURN(ENTER) - кнопка ввода"""
user_password.send_keys(Keys.RETURN)

filter = driver.find_element(By.CSS_SELECTOR, "[data-test='product_sort_container']")
filter.click()
print("Click Filter")
time.sleep(3)
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)
time.sleep(3)
driver.close()
