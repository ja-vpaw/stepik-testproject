import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL_FIELD)
        input.send_keys(email)
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_FIELD)
        input.send_keys(password)
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_CONFIRM_PASSWORD_FIELD)
        input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_REGISTER_SUBMIT_BUTTON)
        button.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert "/login" in self.browser.current_url, "Current url not contain '/login'"


    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
