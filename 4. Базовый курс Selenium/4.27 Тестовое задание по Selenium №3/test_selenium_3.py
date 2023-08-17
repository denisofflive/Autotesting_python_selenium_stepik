from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.page import Page
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
browser = webdriver.Chrome(options=options, service=g)
url = 'https://www.saucedemo.com/'

page = Page(browser, url)
page.open()

login_page = LoginPage(browser, url)
login_page.auth()

product_page = ProductPage(browser, url)
product_page.get_info_product_page()
product_page.add_to_cart()
product_page.go_to_cart()

cart_page = CartPage(browser, url)
cart_page.compare_product_page_and_cart_page_products()
cart_page.go_to_checkout()

checkout_page = CheckoutPage(browser, url)
checkout_page.do_checkout()
checkout_page.go_to_overview_page()
checkout_page.make_screenshot()

overview_page = OverviewPage(browser, url)
overview_page.compare_product_page_and_overview_page_products()

print('Test is Over!')

page.close()
