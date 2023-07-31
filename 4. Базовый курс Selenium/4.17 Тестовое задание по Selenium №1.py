"""
1.Авторизоваться на сайте

2.Выбрать 2 товара

3.Сохранить в переменные названия и цены товаров

4.Пройти весь БП, на моменте оплаты товара сверить сохраненные значения,
а так же что система правильно посчитала сумму товаров
(отдельно считаем сумм товаров и проверяем с тем что говорит нам система)

5.Не забывайте добавлять PRINT и КОММЕНТАРИИ для лучшей читаемости кода

"""
import datetime
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

"""Авторизация"""
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

username = driver.find_element(By.CSS_SELECTOR, "#user-name")
username.send_keys(login_standard_user)
print("Ввести логин")

user_password = driver.find_element(By.CSS_SELECTOR, "#password")
user_password.send_keys(password_all)
print("Ввести пароль")

button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
button_login.click()
print("Нажать на кнопку логина")

"""Инфо от товаре 1"""
product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link")
value_product_1 = product_1.text
print('Имя товара 1: ' + str(value_product_1))

price_product_1 = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
value_price_product_1 = price_product_1.text
print('Цена товара 1: ' + str(value_price_product_1))

"""Добавить товар 1 в корзину"""
add_button_product_1 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
add_button_product_1.click()
print('Добавить товар 1 в корзину')

"""Инфо от товаре 2"""
product_2 = driver.find_element(By.CSS_SELECTOR, "#item_5_title_link")
value_product_2 = product_2.text
print('Имя товара 2: ' + str(value_product_2))

price_product_2 = driver.find_element(By.XPATH, "//div[text() = '49.99']")
value_price_product_2 = price_product_2.text
print('Цена товара 2: ' + str(value_price_product_2))

"""Добавить товар 2 в корзину"""
add_button_product_2 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
add_button_product_2.click()
print('Добавить товар 2 в корзину')

"""Нажать на кнопку Shopping Cart"""
cart = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
cart.click()
print('Нажать на кнопку Shopping Cart')

"""Инфо о товаре 1 в корзине"""
cart_product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("OK,инфо о товаре 1 подтверждена")

price_cart_product_1 = driver.find_element(By.XPATH, "//div[text() = '29.99']")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("OK, цена о товаре 1 подтверждена")

"""Инфо о товаре 2 в корзине"""
cart_product_2 = driver.find_element(By.CSS_SELECTOR, "#item_5_title_link")
value_cart_product_2 = cart_product_2.text
print('Имя товара 2 в корзине: ' + str(value_cart_product_2))
assert value_cart_product_2 == value_product_2
print('OK, инфо товара 2 подтвержена')

cart_price_product_2 = driver.find_element(By.XPATH, "//div[text() = '49.99']")
value_cart_price_product_2 = cart_price_product_2.text
print('Цена товара 2 в корзине: ' + str(value_cart_price_product_2))
assert value_cart_price_product_2 == value_price_product_2
print('OK, цена товара 2 подтвержена')

"""Нажать на кнопку Checkout"""
checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout.click()
print("Нажать на кнопку Checkout")

"""Заполнить поля (Вашу информацию)"""
first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Denis")
print("Ввести имя")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Denisov")
print("Ввести фамилию")

zip = driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip.send_keys("10880")
print("Ввести индекс")

"""Нажать на кнопку Continue"""
button_continue = driver.find_element(By.CSS_SELECTOR, "#continue")
button_continue.click()
print("Нажать на кнопку Continue")

time.sleep(3)

"""Создание скриншота"""
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = "screenshot" + now_date + '.png'
driver.save_screenshot(
    'F:\\Autotesting_python_selenium_stepik\\4. Базовый курс Selenium\\screenshots\\' + name_screenshot)

"""Обзор информации о товаре 1"""
overview_product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link")
value_overview_product_1 = overview_product_1.text
print('Финальное имя продукта 1: ' + str(value_overview_product_1))
assert value_product_1 == value_overview_product_1
print('OK, финальное имя продукта корректно')

overview_price_product_1 = driver.find_element(By.XPATH, "//div[text() = '29.99']")
value_overview_price_product_1 = overview_price_product_1.text
print('Финальная цена продукта 1: ' + str(value_overview_price_product_1))
assert value_price_product_1 == value_overview_price_product_1
print('OK, финальная цена продукта корректна')

"""Обзор информации о товаре 2"""
overview_product_2 = driver.find_element(By.CSS_SELECTOR, "#item_5_title_link")
value_overview_product_2 = overview_product_2.text
print('Финальное имя продукта 2: ' + str(value_overview_product_2))
assert value_product_2 == value_overview_product_2
print('OK, финальное имя продукта корректно')

overview_price_product_2 = driver.find_element(By.XPATH, "//div[text() = '49.99']")
value_overview_price_product_2 = overview_price_product_2.text
print('Финальная цена продукта 2: ' + str(value_overview_price_product_2))
assert value_price_product_2 == value_overview_price_product_2
print('OK, финальная цена продукта корректна')

"""Отделить $ от итоговой сумму"""
total_sum = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
value_total_sum = str(total_sum.text).replace('Item total: $', '')
print('Общая сумма равна:  ' + value_total_sum)

"""Подсчет сумм двух товаров"""
sum_product_1 = driver.find_element(By.XPATH, "//div[text() = '29.99']")
value_sum_product_1 = str(sum_product_1.text).replace('$', '')
print("Цена товара 1: " + value_sum_product_1)
sum_product_2 = driver.find_element(By.XPATH, "//div[text() = '49.99']")
value_sum_product_2 = str(sum_product_2.text).replace('$', '')
print("Цена товара 2: " + value_sum_product_2)

count_sum = float(value_sum_product_1) + float(value_sum_product_2)
print('Итоговая сумма двух товаров: ' + str(count_sum))

assert float(count_sum) == float(value_total_sum)
print('Система правильно посчитала общую сумму')

"""Нажать на кнопку Finish"""
finish_button = driver.find_element(By.CSS_SELECTOR, "#finish")
finish_button.click()
print("Нажать на кнопку Finish")


"""Спасибо за ваш заказ"""

complete_header = driver.find_element(By.CSS_SELECTOR, ".complete-header")
value_complete_header = complete_header.text
# print(value_complete_header)
assert value_complete_header == "Thank you for your order!"
print("Спасибо за ваш заказ!")


time.sleep(3)
driver.close()
