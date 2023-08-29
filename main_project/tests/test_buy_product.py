import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from main_project.pages.cart_page import Cart_page
from main_project.pages.client_information_page import Client_inforamtion_page
from main_project.pages.finish_page import Finish_page
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page
from main_project.pages.payment_page import Payment_page


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_inforamtion_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    time.sleep(1)
    driver.close()
