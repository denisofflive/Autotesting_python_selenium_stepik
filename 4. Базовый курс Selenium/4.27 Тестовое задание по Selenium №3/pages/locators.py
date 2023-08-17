from selenium.webdriver.common.by import By


class LoginPageLocators():
    user_name = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")


class ProductPageLocators():
    product_1 = (By.CSS_SELECTOR, "#item_4_title_link")
    price_product_1 = (By.XPATH, "//div[text() = '29.99']")
    add_button_product_1 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")

    product_2 = (By.CSS_SELECTOR, "#item_0_title_link")
    price_product_2 = (By.XPATH, "//div[text() = '9.99']")
    add_button_product_2 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")

    product_3 = (By.CSS_SELECTOR, "#item_1_title_link")
    price_product_3 = (By.XPATH, "//div[text() = '15.99']")
    add_button_product_3 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")

    product_4 = (By.CSS_SELECTOR, "#item_5_title_link")
    price_product_4 = (By.XPATH, "//div[text() = '49.99']")
    add_button_product_4 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")

    product_5 = (By.CSS_SELECTOR, "#item_2_title_link")
    price_product_5 = (By.XPATH, "//div[text() = '7.99']")
    add_button_product_5 = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")

    product_6 = (By.CSS_SELECTOR, "#item_3_title_link")
    price_product_6 = (By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
    add_button_product_6 = (By.CSS_SELECTOR, "[id='add-to-cart-test.allthethings()-t-shirt-(red)']")

    cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")


class CartPageLocators():
    cart_product_1 = (By.CSS_SELECTOR, "#item_4_title_link")
    cart_price_product_1 = (By.XPATH, "//div[text() = '29.99']")

    cart_product_2 = (By.CSS_SELECTOR, "#item_0_title_link")
    cart_price_product_2 = (By.XPATH, "//div[text() = '9.99']")

    cart_product_3 = (By.CSS_SELECTOR, "#item_1_title_link")
    cart_price_product_3 = (By.XPATH, "//div[text() = '15.99']")

    cart_product_4 = (By.CSS_SELECTOR, "#item_5_title_link")
    cart_price_product_4 = (By.XPATH, "//div[text() = '49.99']")

    cart_product_5 = (By.CSS_SELECTOR, "#item_2_title_link")
    cart_price_product_5 = (By.XPATH, "//div[text() = '7.99']")

    cart_product_6 = (By.CSS_SELECTOR, "#item_3_title_link")
    cart_price_product_6 = (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    checkout = (By.CSS_SELECTOR, "#checkout")


class CheckoutPageLocators():
    first_name = (By.CSS_SELECTOR, "#first-name")
    last_name = (By.CSS_SELECTOR, "#last-name")
    postal_code = (By.CSS_SELECTOR, "#postal-code")

    continue_button = (By.CSS_SELECTOR, "#continue")


class OverviewPageLocators():
    overview_product_1 = (By.CSS_SELECTOR, "#item_4_title_link")
    overview_price_product_1 = (By.XPATH, "//div[text() = '29.99']")

    overview_product_2 = (By.CSS_SELECTOR, "#item_0_title_link")
    overview_price_product_2 = (By.XPATH, "//div[text() = '9.99']")

    overview_product_3 = (By.CSS_SELECTOR, "#item_1_title_link")
    overview_price_product_3 = (By.XPATH, "//div[text() = '15.99']")

    overview_product_4 = (By.CSS_SELECTOR, "#item_5_title_link")
    overview_price_product_4 = (By.XPATH, "//div[text() = '49.99']")

    overview_product_5 = (By.CSS_SELECTOR, "#item_2_title_link")
    overview_price_product_5 = (By.XPATH, "//div[text() = '7.99']")

    overview_product_6 = (By.CSS_SELECTOR, "#item_3_title_link")
    overview_price_product_6 = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")

    total_sum = (By.CSS_SELECTOR, ".summary_subtotal_label")
