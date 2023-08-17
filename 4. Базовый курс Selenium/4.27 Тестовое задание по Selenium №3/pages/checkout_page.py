import datetime
from .page import Page
from .locators import CheckoutPageLocators

FIRSTNAME = 'Denis'
LASTNAME = 'Denisov'
POSTCODE = '108880'


class CheckoutPage(Page):
    def do_checkout(self):
        first_name = self.browser.find_element(*CheckoutPageLocators.first_name)
        first_name.send_keys(FIRSTNAME)
        print('First name')
        last_name = self.browser.find_element(*CheckoutPageLocators.last_name)
        last_name.send_keys(LASTNAME)
        print('Last name')
        postal_code = self.browser.find_element(*CheckoutPageLocators.postal_code)
        postal_code.send_keys(POSTCODE)
        print('Zip')

    def go_to_overview_page(self):
        continue_button = self.browser.find_element(*CheckoutPageLocators.continue_button)
        continue_button.click()
        print('Go to Overview page')

    def make_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot-' + now_date + '.png'
        self.browser.save_screenshot('F:\\Autotesting_python_selenium_stepik\\4. Базовый курс Selenium\\4.27 Тестовое задание по Selenium №3\\screenshots\\' + name_screenshot)
        print('Screen is made successfully')
