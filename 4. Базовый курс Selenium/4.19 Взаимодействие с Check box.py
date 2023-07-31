import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

check_box = driver.find_element(By.CSS_SELECTOR, ".rct-checkbox")
check_box.click()
print("Click Checkbox")

toggle_button = driver.find_element(By.CSS_SELECTOR, "[title='Toggle']")
toggle_button.click()
print("Click Toggle Button")

time.sleep(1)
driver.close()
