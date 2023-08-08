import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
double = driver.find_element(By.CSS_SELECTOR, "#doubleClickBtn")
action.double_click(double).perform() # метод perform сохраняет результат
print("Click DoubleClick Button")

right_click = driver.find_element(By.CSS_SELECTOR, "#rightClickBtn")
action.context_click(right_click).perform()
print("Click RightClick Button")


time.sleep(1)
driver.close()
