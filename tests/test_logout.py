import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_logout(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    products_page.logout()
    assert logged_in_page.url == "https://www.saucedemo.com/"