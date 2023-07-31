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

login_standard_user = "standard_user"
password_all = "secret_sauce"

username = driver.find_element(By.CSS_SELECTOR, "#user-name")
username.send_keys(login_standard_user)
print("Input Login")
user_password = driver.find_element(By.CSS_SELECTOR, "#password")
user_password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
button_login.click()
print("Click Login Button")

"""INFO Product #1"""
product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price") #XPATH //div[text() = '29.99'] .inventory_item_price
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
select_product_1.click()
print("Select Product_1")

cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
cart.click()
print("Enter Cart")

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product 1 GOOD")

price_cart_product_1 = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price") #XPATH //div[text() = '29.99'] .inventory_item_price
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO Cart Price Product 1 GOOD")

checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout.click()
print("Click Checkout")

"""Select User INFO"""

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Denis")
print("Input First Name")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Denisov")
print("Input Last Name")

zip = driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip.send_keys("10880")
print("Input Zip/Postalcode")

button_continue = driver.find_element(By.CSS_SELECTOR, "#continue")
button_continue.click()
print("Click Continue Button")

"""INFO Finish Product 1"""
finish_product_1 = driver.find_element(By.CSS_SELECTOR, "#item_4_title_link")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Finish Product 1 GOOD")

price_finish_product_1 = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price") #XPATH //div[text() = '29.99'] .inventory_item_price
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Finish Price Product 1 GOOD")

summury_price = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
value_summury_price = summury_price.text
print(value_summury_price)
item_total = "Item total: " + value_finish_price_product_1
print(item_total)
assert value_summury_price == item_total
print("Total summary price Good")

time.sleep(1)
driver.close()

