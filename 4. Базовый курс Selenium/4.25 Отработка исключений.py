import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

"""https://demoqa.com/dynamic-properties"""

"""работа с исключениями"""
# try:
#     visible_button = driver.find_element(By.CSS_SELECTOR, "#visibleAfter")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print('NoSuchElementException exception')
#     time.sleep(10)
#     driver.refresh()
#     visible_button = driver.find_element(By.XPATH, "#visibleAfter")
#     visible_button.click()
#     print('Click visible button')

"""https://demoqa.com/radio-button"""

yes_button = driver.find_element(By.CSS_SELECTOR, "[for='yesRadio']")
yes_button.click()
try:
    message = driver.find_element(By.CSS_SELECTOR, ".text-success")
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    driver.refresh()
    time.sleep(3)
    yes_button = driver.find_element(By.CSS_SELECTOR, "[for='yesRadio']")
    yes_button.click()
    message = driver.find_element(By.CSS_SELECTOR, ".text-success")
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print('Checkbox YES')
print('Test is over')

time.sleep(10)
driver.close()


