import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.fixture
def cart_page(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(0)
    products_page.go_to_cart()
    return CartPage(page)

@pytest.fixture
def empty_cart_page(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    products_page.go_to_cart()
    return CartPage(page)

def test_cart_has_items(cart_page):
    assert cart_page.get_cart_item_count() > 0

def test_empty_cart(empty_cart_page):
    assert empty_cart_page.get_cart_item_count() == 0

def test_remove_item_from_cart(cart_page):
    initial_count = cart_page.get_cart_item_count()
    cart_page.remove_item(0)
    assert cart_page.get_cart_item_count() == initial_count - 1

def test_proceed_to_checkout(cart_page):
    cart_page.proceed_to_checkout()
    assert "checkout" in cart_page.page.url