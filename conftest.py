import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(record_video_dir="test-results/videos")
    page = context.new_page()
    page.set_default_timeout(30000)
    yield page
    context.close()

@pytest.fixture
def logged_in_page(page):
    from pages.login_page import LoginPage
    page.goto("https://www.saucedemo.com/")
    page.wait_for_selector("#user-name")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    return page

@pytest.fixture
def home_page(page):
    page.goto("https://www.saucedemo.com/")
    page.wait_for_selector("#user-name")
    return page