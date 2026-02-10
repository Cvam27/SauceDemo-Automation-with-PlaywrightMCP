import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])
def test_valid_login(page, username, password):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login(username, password)
    assert "inventory" in page.url

def test_invalid_username(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("invalid_user", "secret_sauce")
    assert "Epic sadface" in login_page.get_error_message()

def test_invalid_password(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "wrong_password")
    assert "Epic sadface" in login_page.get_error_message()

def test_empty_username(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("", "secret_sauce")
    assert "Epic sadface" in login_page.get_error_message()

def test_empty_password(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "")
    assert "Epic sadface" in login_page.get_error_message()

def test_locked_out_user(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.get_error_message().lower()