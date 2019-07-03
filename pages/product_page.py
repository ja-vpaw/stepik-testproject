from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_check(self):
        basket_current = self.get_current_basket_value()
        product_price = self.get_product_price()
        self.add_to_basket_click()
        self.should_be_message_success_add_to_basket()
        self.should_be_product_price_add_to_basket_price(basket_current, product_price)

    def add_to_basket_click(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_message_success_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_add_to_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET).text
        print("product_name = {}\nmessage_add_to_basket = {}".format(product_name, message_add_to_basket))
        assert product_name == message_add_to_basket, "Current product not in message add to basket"

    def should_be_product_price_add_to_basket_price(self, basket_current=None, product_price=None):
        if basket_current is None:
            basket_current = self.get_current_basket_value()
            self.add_to_basket_click()
        if product_price is None:
            product_price = self.get_product_price()
        basket_message_price = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRICE_VALUE).text
        basket_message_price = float(basket_message_price[1:])
        print("basket_message_price = {}".format(basket_message_price))
        assert basket_message_price == basket_current + product_price, "Current product price add to basket not correct"

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price = float(product_price[1:])
        print("product_price = {}".format(product_price))
        return product_price

    def get_current_basket_value(self):
        basket_current = self.browser.find_element(*ProductPageLocators.BASKET_CURRENT_VALUE).text
        basket_current = float(basket_current.splitlines()[0].split(':')[1].strip()[1:])
        print("basket_current =".format(basket_current))
        return basket_current
