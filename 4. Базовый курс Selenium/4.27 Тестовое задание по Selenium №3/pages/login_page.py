from .page import Page
from .locators import LoginPageLocators

login_standard_user = 'standard_user'
password_all = 'secret_sauce'


class LoginPage(Page):

    def auth(self):
        user_name = self.browser.find_element(*LoginPageLocators.user_name)
        user_name.send_keys(login_standard_user)
        print('Input login')
        password = self.browser.find_element(*LoginPageLocators.password)
        password.send_keys(password_all)
        print('Input password')
        login_button = self.browser.find_element(*LoginPageLocators.login_button)
        login_button.click()
        print('Click login button')
        print('Go to Product Page')
