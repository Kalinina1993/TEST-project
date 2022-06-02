from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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