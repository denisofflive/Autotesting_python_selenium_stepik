import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from main_project.pages.login_page import Login_page
from main_project.pages.main_page import Main_page


def test_link_about():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")

    time.sleep(1)
    driver.close()
