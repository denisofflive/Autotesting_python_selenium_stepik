import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from main_project.pages.cart_page import Cart_page
from main_project.pages.client_information_page import Client_inforamtion_page
from main_project.pages.finish_page import Finish_page
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page
from main_project.pages.payment_page import Payment_page

# @pytest.mark.run(order=2)
def test_buy_product_1(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_inforamtion_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    print('Finish Test 1')
    time.sleep(1)
    driver.close()
# @pytest.mark.run(order=3)
def test_buy_product_2(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print('Finish Test 2')
    time.sleep(1)
    driver.close()
# @pytest.mark.run(order=1)
def test_buy_product_3(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print('Finish Test 3')
    time.sleep(1)
    driver.close()
