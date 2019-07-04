from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_has_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEM), "Basket hasn't any item element"


    def is_basket_has_not_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket has some item element"


    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket is empty text is not presented"


    def should_not_be_text_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket is empty text is presented"
