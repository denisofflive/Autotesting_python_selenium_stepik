from .page import Page, chosen_product
from .locators import ProductPageLocators

dict_values_product_page = dict()


class ProductPage(Page):
    def get_info_product_page(self):
        if chosen_product == '1':
            product_1 = self.browser.find_element(*ProductPageLocators.product_1)
            value_product_1 = product_1.text
            print('Name of Product 1: ' + str(value_product_1))
            price_product_1 = self.browser.find_element(*ProductPageLocators.price_product_1)
            value_price_product_1 = price_product_1.text
            print('Price of Product 1: ' + str(value_price_product_1))
            dict_values_product_page[value_product_1] = value_price_product_1
        elif chosen_product == '2':
            product_2 = self.browser.find_element(*ProductPageLocators.product_2)
            value_product_2 = product_2.text
            print('Name of Product 2: ' + str(value_product_2))
            price_product_2 = self.browser.find_element(*ProductPageLocators.price_product_2)
            value_price_product_2 = price_product_2.text
            print('Price of Product 2: ' + str(value_price_product_2))
            dict_values_product_page[value_product_2] = value_price_product_2
        elif chosen_product == '3':
            product_3 = self.browser.find_element(*ProductPageLocators.product_3)
            value_product_3 = product_3.text
            print('Name of Product 3: ' + str(value_product_3))
            price_product_3 = self.browser.find_element(*ProductPageLocators.price_product_3)
            value_price_product_3 = price_product_3.text
            print('Price of Product 3: ' + str(value_price_product_3))
            dict_values_product_page[value_product_3] = value_price_product_3
        elif chosen_product == '4':
            product_4 = self.browser.find_element(*ProductPageLocators.product_4)
            value_product_4 = product_4.text
            print('Name of Product 4: ' + str(value_product_4))
            price_product_4 = self.browser.find_element(*ProductPageLocators.price_product_4)
            value_price_product_4 = price_product_4.text
            print('Price of Product 4: ' + str(value_price_product_4))
            dict_values_product_page[value_product_4] = value_price_product_4
        elif chosen_product == '5':
            product_5 = self.browser.find_element(*ProductPageLocators.product_5)
            value_product_5 = product_5.text
            print('Name of Product 5: ' + str(value_product_5))
            price_product_5 = self.browser.find_element(*ProductPageLocators.price_product_5)
            value_price_product_5 = price_product_5.text
            print('Price of Product 5: ' + str(value_price_product_5))
            dict_values_product_page[value_product_5] = value_price_product_5
        elif chosen_product == '6':
            product_6 = self.browser.find_element(*ProductPageLocators.product_6)
            value_product_6 = product_6.text
            print('Name of Product 6: ' + str(value_product_6))
            price_product_6 = self.browser.find_element(*ProductPageLocators.price_product_6)
            value_price_product_6 = price_product_6.text
            print('Price of Product 6: ' + str(value_price_product_6))
            dict_values_product_page[value_product_6] = value_price_product_6
        else:
            print("Error, this product doesn't exist!")

    def add_to_cart(self):
        if chosen_product == '1':
            add_button_product_1 = self.browser.find_element(*ProductPageLocators.add_button_product_1)
            add_button_product_1.click()
            print('Add Product 1 to cart')
        elif chosen_product == '2':
            add_button_product_2 = self.browser.find_element(*ProductPageLocators.add_button_product_2)
            add_button_product_2.click()
            print('Add Product 2 to cart')
        elif chosen_product == '3':
            add_button_product_3 = self.browser.find_element(*ProductPageLocators.add_button_product_3)
            add_button_product_3.click()
            print('Add Product 3 to cart')
        elif chosen_product == '4':
            add_button_product_4 = self.browser.find_element(*ProductPageLocators.add_button_product_4)
            add_button_product_4.click()
            print('Add Product 4 to cart')
        elif chosen_product == '5':
            add_button_product_5 = self.browser.find_element(*ProductPageLocators.add_button_product_5)
            add_button_product_5.click()
            print('Add Product 5 to cart')
        elif chosen_product == '6':
            add_button_product_6 = self.browser.find_element(*ProductPageLocators.add_button_product_6)
            add_button_product_6.click()
            print('Add Product 6 to cart')
        else:
            print("Error, this product doesn't exist!")

    def go_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.cart_link)
        cart_link.click()
        print('Go to cart')
