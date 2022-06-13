from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL_FIELD = (By.NAME, "login-username")
    LOGIN_PSW_FIELD = (By.NAME, "login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTER_PSW_FIELD = (By.NAME, "registration-password1")
    REGISTER_PSW_CONFIRM_FIELD = (By.NAME, "registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_IN_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_PRICE_IN_CART = (
    By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                     "p:nth-child(1) > strong")
    ADDING_MESSAGE_CONFIRM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")


class BasketPageLocators:
    BASKET_PAGE_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right."
                                           "hidden-xs > span > a")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")

