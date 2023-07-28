import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use"
password_all = "secret_sauce"

username = driver.find_element(By.CSS_SELECTOR, "#user-name")
username.send_keys(login_standard_user)
print("Input login")
user_password = driver.find_element(By.CSS_SELECTOR, "#password")
user_password.send_keys(password_all)
print("Input password")
button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
button_login.click()
print("Click login button")

"""Создаём переменную с найденным элементом"""
warring_text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
"""Создаём новую переменную value_warring_text, которой присваеим переменную warring_text
с функцией text"""
value_warring_text = warring_text.text
"""сравниваем переменную value_warring_text с отображаемой ошибкой"""
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
"""выводим на экран Good Test, если всё прошло успешно"""
print("Good Test")


time.sleep(1)
driver.close()
