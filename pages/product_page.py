from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_in_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_IN_CART_BUTTON).click()

    def product_in_cart(self):
        text = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert text.text in self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE_CONFIRM).text, "The cart is " \
                                                                                                         "empty " \
                                                                                                         "or incorrect " \
                                                                                                         "name"
        print(text.text)

    def price_of_cart(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert text.text in self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).text, "Incorrect " \
                                                                                                        "price"
