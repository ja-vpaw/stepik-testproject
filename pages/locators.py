from selenium.webdriver.common.by import By


class BasePageLocators(object):

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")

    BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-default[href]")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators(object):

    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators(object):

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class MainPageLocators(object):

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(object):

    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    MESSAGE_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_MESSAGE_PRICE_VALUE = (By.CSS_SELECTOR, "#messages div.alertinner>p:nth-child(1)>strong")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")

    BASKET_CURRENT_VALUE = (By.CSS_SELECTOR, ".basket-mini")
