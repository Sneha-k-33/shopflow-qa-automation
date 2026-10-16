# pages/checkout_page.py

from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckoutPage(BasePage):
    """Page Object for the SauceDemo Checkout Pages (Information, Overview, Complete)."""
    
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.error_container = page.locator(".error-message-container")
        self.subtotal_label = page.locator(".summary_subtotal_label")
        self.tax_label = page.locator(".summary_tax_label")
        self.total_label = page.locator(".summary_total_label")
        self.complete_header = page.locator(".complete-header")

    def verify_on_checkout_page(self):
        """Verify that the user is on the checkout information page."""
        expect(self.title).to_have_text("Checkout: Your Information")

    def fill_checkout_information(self, first_name, last_name, postal_code):
        """Fill out the customer checkout information form and continue."""
        if first_name:
            self.first_name.fill(first_name)
        if last_name:
            self.last_name.fill(last_name)
        if postal_code:
            self.postal_code.fill(postal_code)
        self.continue_button.click()

    def get_error_message(self):
        """Return the validation error message text."""
        return self.error_container.inner_text()

    def verify_checkout_summary(self):
        """Verify that subtotal, tax, and total summary labels are visible."""
        expect(self.subtotal_label).to_be_visible()
        expect(self.tax_label).to_be_visible()
        expect(self.total_label).to_be_visible()

    def finish_checkout(self):
        """Click the finish button on the checkout overview page."""
        self.finish_button.click()

    def verify_order_success(self):
        """Verify the order completion success header."""
        expect(self.complete_header).to_have_text("Thank you for your order!")