from .base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def get_product_count(self):
        return self.inventory_items.count()

    def add_product_to_cart(self, index):
        self.inventory_items.nth(index).locator("button").click()

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def go_to_cart(self):
        self.cart_link.click()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()