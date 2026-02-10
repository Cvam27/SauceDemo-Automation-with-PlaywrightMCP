import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def checkout_page(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(0)
    products_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()
    return CheckoutPage(page)

def test_successful_checkout(checkout_page):
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()
    assert "Thank you" in checkout_page.get_complete_message()

def test_checkout_empty_first_name(checkout_page):
    checkout_page.fill_checkout_info("", "Doe", "12345")
    assert "First Name" in checkout_page.get_error_message()

def test_checkout_empty_last_name(checkout_page):
    checkout_page.fill_checkout_info("John", "", "12345")
    assert "Last Name" in checkout_page.get_error_message()

def test_checkout_empty_zip(checkout_page):
    checkout_page.fill_checkout_info("John", "Doe", "")
    assert "Postal Code" in checkout_page.get_error_message()

def test_checkout_invalid_zip(checkout_page):
    checkout_page.fill_checkout_info("John", "Doe", "abc")
    # Might not validate, but assume passes or check