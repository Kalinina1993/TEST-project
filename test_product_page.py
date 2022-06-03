from pages.product_page import ProductPage
from config import product_page_url, page_without_capcha_url, for_change_page_url
import pytest
import time


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_product_in_cart()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_in_cart()
    page.price_of_cart()


@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_cart()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_in_cart()
    page.price_of_cart()


@pytest.mark.xfail(reason="Hello, bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, page_without_capcha_url)
    page.open()
    page.add_product_in_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, page_without_capcha_url)
    page.open()
    page.success_message_should_disappear()


@pytest.mark.xfail(reason="Hello, bug 2")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, page_without_capcha_url)
    page.open()
    page.add_product_in_cart()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, for_change_page_url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.should_be_login_link()


