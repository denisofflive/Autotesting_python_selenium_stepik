from .page import Page, chosen_product
from .locators import OverviewPageLocators
from .product_page import ProductPage, dict_values_product_page


class OverviewPage(Page):
    def compare_product_page_and_overview_page_products(self):
        if chosen_product == "1":
            overview_product_1 = self.browser.find_element(*OverviewPageLocators.overview_product_1)
            value_overview_product_1 = overview_product_1.text
            print('Final Name of Product 1: ' + str(value_overview_product_1))
            assert value_overview_product_1 == str(*dict_values_product_page.keys())
            print('OK, Final Name of Product 1 is correct')

            overview_price_product_1 = self.browser.find_element(*OverviewPageLocators.overview_price_product_1)
            value_overview_price_product_1 = overview_price_product_1.text
            print('Final Price of Product 1: ' + str(value_overview_price_product_1))
            assert value_overview_price_product_1 == str(*dict_values_product_page.values())
            print('OK, Final Price of Product 1 is correct')

        if chosen_product == "2":
            overview_product_2 = self.browser.find_element(*OverviewPageLocators.overview_product_2)
            value_overview_product_2 = overview_product_2.text
            print('Final Name of Product 2: ' + str(value_overview_product_2))
            assert value_overview_product_2 == str(*dict_values_product_page.keys())
            print('OK, Final Name of Product 2 is correct')

            overview_price_product_2 = self.browser.find_element(*OverviewPageLocators.overview_price_product_2)
            value_overview_price_product_2 = overview_price_product_2.text
            print('Final Price of Product 2: ' + str(value_overview_price_product_2))
            assert value_overview_price_product_2 == str(*dict_values_product_page.values())
            print('OK, Final Price of Product 2 is correct')

        if chosen_product == "3":
            overview_product_3 = self.browser.find_element(*OverviewPageLocators.overview_product_3)
            value_overview_product_3 = overview_product_3.text
            print('Final Name of Product 3: ' + str(value_overview_product_3))
            assert value_overview_product_3 == str(*dict_values_product_page.keys())
            print('OK, Final Name of Product 3 is correct')

            overview_price_product_3 = self.browser.find_element(*OverviewPageLocators.overview_price_product_3)
            value_overview_price_product_3 = overview_price_product_3.text
            print('Final Price of Product 3: ' + str(value_overview_price_product_3))
            assert value_overview_price_product_3 == str(*dict_values_product_page.values())
            print('OK, Final Price of Product 3 is correct')

        if chosen_product == "4":
            overview_product_4 = self.browser.find_element(*OverviewPageLocators.overview_product_4)
            value_overview_product_4 = overview_product_4.text
            print('Final Name of Product 4: ' + str(value_overview_product_4))
            assert value_overview_product_4 == str(*dict_values_product_page.keys())
            print('OK, Final Name of Product 4 is correct')

            overview_price_product_4 = self.browser.find_element(*OverviewPageLocators.overview_price_product_4)
            value_overview_price_product_4 = overview_price_product_4.text
            print('Final Price of Product 4: ' + str(value_overview_price_product_4))
            assert value_overview_price_product_4 == str(*dict_values_product_page.values())
            print('OK, Final Price of Product 4 is correct')

        if chosen_product == "5":
            overview_product_5 = self.browser.find_element(*OverviewPageLocators.overview_product_5)
            value_overview_product_5 = overview_product_5.text
            print('Final Name of Product 5: ' + str(value_overview_product_5))
            assert value_overview_product_5 == str(*dict_values_product_page.keys())
            print('OK, Final Name of Product 5 is correct')

            overview_price_product_5 = self.browser.find_element(*OverviewPageLocators.overview_price_product_5)
            value_overview_price_product_5 = overview_price_product_5.text
            print('Final Price of Product 5: ' + str(value_overview_price_product_5))
            assert value_overview_price_product_5 == str(*dict_values_product_page.values())
            print('OK, Final Price of Product 5 is correct')

        if chosen_product == "6":
            overview_product_6 = self.browser.find_element(*OverviewPageLocators.overview_product_6)
            value_overview_product_6 = overview_product_6.text
            print('Final Name of Product 6: ' + str(value_overview_product_6))
            assert value_overview_product_6 == str(*dict_values_product_page.keys())
            print('OK, Final Name of Product 6 is correct')

            overview_price_product_6 = self.browser.find_element(*OverviewPageLocators.overview_price_product_6)
            value_overview_price_product_6 = overview_price_product_6.text
            print('Final Price of Product 6: ' + str(value_overview_price_product_6))
            assert value_overview_price_product_6 == str(*dict_values_product_page.values())
            print('OK, Final Price of Product 6 is correct')
