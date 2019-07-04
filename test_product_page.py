import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

# links = ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
#          'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019']

links = ['http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/']


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


    def test_guest_can_see_add_to_basket_button(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()


    def test_guest_can_see_message_success_add_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.should_be_message_success_add_to_basket()


    def test_should_be_product_price_add_to_basket_price(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_price_add_to_basket_price()


    def test_guest_can_see_product_price(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.get_product_price()


    def test_guest_can_see_current_basket_value(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.get_current_basket_value()


    def test_guest_cant_see_message_success_add_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_message_success_add_to_basket()


    @pytest.mark.skip(reason="Not realised yet")
    def test_should_disappear_message_success_add_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_click()
        page.should_disappear_message_success_add_to_basket()


    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page (self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_product_page (self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_has_not_items()
        basket_page.should_be_text_basket_is_empty()
