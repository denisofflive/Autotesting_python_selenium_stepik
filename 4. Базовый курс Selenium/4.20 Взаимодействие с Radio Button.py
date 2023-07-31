import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

radio_button = driver.find_element(By.CSS_SELECTOR, "[for='yesRadio']")
radio_button.click()
print("Click Radio Button")


time.sleep(1)
driver.close()
