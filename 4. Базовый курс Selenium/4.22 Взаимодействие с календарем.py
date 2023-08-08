import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# new_date = driver.find_element(By.CSS_SELECTOR, "#datePickerMonthYearInput")
# new_date.send_keys(Keys.BACKSPACE*10)
# time.sleep(1)
# new_date.send_keys("08/08/2025")
# time.sleep(1)
# new_date.send_keys(Keys.RETURN)
# print("09/08/2025")

# """Второй вариант - обращаемся к дате"""
#
# new_date = driver.find_element(By.CSS_SELECTOR, "#datePickerMonthYearInput")
# new_date.click()
# date_08_09_23 = driver.find_element(By.CSS_SELECTOR, "[aria-label='Choose Wednesday, August 9th, 2023']")
# date_08_09_23.click()
# print("08/09/2023")
#
# time.sleep(1)
# driver.close()


"""Третий вариант - обращаемся к сегодняшней дате + 1 день"""

new_date = driver.find_element(By.CSS_SELECTOR, "#datePickerMonthYearInput")
new_date.click()
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) + 1
locator = "//div[@aria-label='Choose Tuesday, August " + str(date) + "th, 2023']"
print(locator)

# date_09 = driver.find_element(By.XPATH, locator)
# date_09.click()

time.sleep(1)
driver.close()
