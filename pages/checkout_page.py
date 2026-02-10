from .base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.zip_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.error_message = page.locator(".error-message-container")
        self.complete_message = page.locator(".complete-header")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_input.fill(zip_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_error_message(self):
        return self.error_message.text_content()

    def get_complete_message(self):
        return self.complete_message.text_content()