from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text == "Your basket is empty. " \
                                                                                        "Continue " \
                                                                                        "shopping", "Your basket is " \
                                                                                                    "not " \
                                                                                                    "empty"
