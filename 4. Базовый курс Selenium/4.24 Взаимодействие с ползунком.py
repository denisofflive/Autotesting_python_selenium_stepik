import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

"""ActionChains помогает взаимодействовать с мышью"""
action = ActionChains(driver)

square = driver.find_element(By.CSS_SELECTOR, "#id2")
"""Вызываем бегунок и тянем его вправо на 300 по оси Х, потом отпускаем и сохраняем результат"""
action.click_and_hold(square).move_by_offset(300, 0).release().perform()
print('Square +')

time.sleep(3)
driver.close()
