import pytest
from pages.product_page import ProductPage

links = ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019']

links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019']


start_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def prepare_links_with_promo(start_link):
    links = []
    for i in range(10):
        promo_link = start_link + '?promo=offer' + str(i)
        links.append(promo_link)
    return links

#links = prepare_links_with_promo(start_link)

@pytest.mark.parametrize('link', links)
class TestProductPage():


    def test_guest_can_add_product_to_cart(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_check()


    def test_should_be_add_to_basket_button(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()


    def test_should_be_message_success_add_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.should_be_message_success_add_to_basket()


    def test_should_be_product_price_add_to_basket_price(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_price_add_to_basket_price()


    def test_get_product_price(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.get_product_price()


    def test_get_current_basket_value(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.get_current_basket_value()


    def test_should_not_be_product_price_add_to_basket_price(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_message_success_add_to_basket()

    @pytest.mark.skip(reason="Not realised yet")
    def test_should_disappear_message_success_add_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.should_disappear_message_success_add_to_basket()
