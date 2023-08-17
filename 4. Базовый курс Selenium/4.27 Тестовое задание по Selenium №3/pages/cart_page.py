from .page import Page, chosen_product
from .locators import CartPageLocators
from .product_page import ProductPage, dict_values_product_page


class CartPage(Page):
    def compare_product_page_and_cart_page_products(self):
        if chosen_product == '1':
            cart_product_1 = self.browser.find_element(*CartPageLocators.cart_product_1)
            value_cart_product_1 = cart_product_1.text
            print('Name of Product 1 in Cart: ' + str(value_cart_product_1))
            assert value_cart_product_1 == str(*dict_values_product_page.keys())
            print('OK, Product 1 is the same!')

            cart_price_product_1 = self.browser.find_element(*CartPageLocators.cart_price_product_1)
            value_cart_price_product_1 = cart_price_product_1.text
            print('Price of Product 1 in Cart: ' + str(value_cart_price_product_1))
            assert value_cart_price_product_1 == str(*dict_values_product_page.values())
            print('OK, Product 1 price is the same!')
        if chosen_product == '2':
            cart_product_2 = self.browser.find_element(*CartPageLocators.cart_product_2)
            value_cart_product_2 = cart_product_2.text
            print('Name of Product 2 in Cart: ' + str(value_cart_product_2))
            assert value_cart_product_2 == str(*dict_values_product_page.keys())
            print('OK, Product 2 is the same!')

            cart_price_product_2 = self.browser.find_element(*CartPageLocators.cart_price_product_2)
            value_cart_price_product_2 = cart_price_product_2.text
            print('Price of Product 2 in Cart: ' + str(value_cart_price_product_2))
            assert value_cart_price_product_2 == str(*dict_values_product_page.values())
            print('OK, Product 2 price is the same!')
        if chosen_product == '3':
            cart_product_3 = self.browser.find_element(*CartPageLocators.cart_product_3)
            value_cart_product_3 = cart_product_3.text
            print('Name of Product 3 in Cart: ' + str(value_cart_product_3))
            assert value_cart_product_3 == str(*dict_values_product_page.keys())
            print('OK, Product 3 is the same!')

            cart_price_product_3 = self.browser.find_element(*CartPageLocators.cart_price_product_3)
            value_cart_price_product_3 = cart_price_product_3.text
            print('Price of Product 3 in Cart: ' + str(value_cart_price_product_3))
            assert value_cart_price_product_3 == str(*dict_values_product_page.values())
            print('OK, Product 3 price is the same!')
        if chosen_product == '4':
            cart_product_4 = self.browser.find_element(*CartPageLocators.cart_product_4)
            value_cart_product_4 = cart_product_4.text
            print('Name of Product 4 in Cart: ' + str(value_cart_product_4))
            assert value_cart_product_4 == str(*dict_values_product_page.keys())
            print('OK, Product 4 is the same!')

            cart_price_product_4 = self.browser.find_element(*CartPageLocators.cart_price_product_4)
            value_cart_price_product_4 = cart_price_product_4.text
            print('Price of Product 4 in Cart: ' + str(value_cart_price_product_4))
            assert value_cart_price_product_4 == str(*dict_values_product_page.values())
            print('OK, Product 4 price is the same!')
        if chosen_product == '5':
            cart_product_5 = self.browser.find_element(*CartPageLocators.cart_product_5)
            value_cart_product_5 = cart_product_5.text
            print('Name of Product 5 in Cart: ' + str(value_cart_product_5))
            assert value_cart_product_5 == str(*dict_values_product_page.keys())
            print('OK, Product 5 is the same!')

            cart_price_product_5 = self.browser.find_element(*CartPageLocators.cart_price_product_5)
            value_cart_price_product_5 = cart_price_product_5.text
            print('Price of Product 5 in Cart: ' + str(value_cart_price_product_5))
            assert value_cart_price_product_5 == str(*dict_values_product_page.values())
            print('OK, Product 5 price is the same!')
        if chosen_product == '6':
            cart_product_6 = self.browser.find_element(*CartPageLocators.cart_product_6)
            value_cart_product_6 = cart_product_6.text
            print('Name of Product 6 in Cart: ' + str(value_cart_product_6))
            assert value_cart_product_6 == str(*dict_values_product_page.keys())
            print('OK, Product 6 is the same!')

            cart_price_product_6 = self.browser.find_element(*CartPageLocators.cart_price_product_6)
            value_cart_price_product_6 = cart_price_product_6.text
            print('Price of Product 6 in Cart: ' + str(value_cart_price_product_6))
            assert value_cart_price_product_6 == str(*dict_values_product_page.values())
            print('OK, Product 6 price is the same!')

    def go_to_checkout(self):
        checkout = self.browser.find_element(*CartPageLocators.checkout)
        checkout.click()
        print('Go to Checkout')
