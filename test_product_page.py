from pages.product_page import ProductPage
from config import product_page_url
import time


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_product_in_cart()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_in_cart()
    page.price_of_cart()
