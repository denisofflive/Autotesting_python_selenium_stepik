import time

"""Talking to client"""
print('Приветствую тебя в нашем интернет-магазине! :)')
print('Выбери один из следующих товаров и укажи его номер: '
      '1 - Sauce Labs Backpack,'
      '2 - Sauce Labs Bike Light, '
      '3 - Sauce Labs Bolt T-Shirt,'
      '4 - Sauce Labs Fleece Jacket,'
      '5 - Sauce Labs Onesie,'
      '6 - Test.allTheThings() T-Shirt (Red)')
chosen_product = input()
print(chosen_product)


class Page():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        time.sleep(5)
        self.browser.close()
