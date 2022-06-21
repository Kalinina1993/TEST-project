from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationFormPage, LoginFormPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login url is not current"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password, password2):
        self.browser.find_element(*RegistrationFormPage.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*RegistrationFormPage.PSW_FIELD).send_keys(password)
        self.browser.find_element(*RegistrationFormPage.PSW_CONFIRM_FIELD).send_keys(password2)
        self.browser.find_element(*RegistrationFormPage.REGISTER_BUTTON).click()

    def login(self, email, password):
        self.browser.find_element(*LoginFormPage.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginFormPage.PSW_FIELD).send_keys(password)
        self.browser.find_element(*LoginFormPage.LOGIN_BUTTON).click()

