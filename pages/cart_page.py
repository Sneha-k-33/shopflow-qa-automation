# pages/cart_page.py

from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    """Page Object for the SauceDemo Shopping Cart Page."""
    
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def verify_on_cart_page(self):
        """Verify that the user is on the cart page."""
        expect(self.title).to_have_text("Your Cart")

    def verify_item_in_cart(self, product_name):
        """Verify a specific product appears in the cart list."""
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def proceed_to_checkout(self):
        """Click the checkout button."""
        self.checkout_button.click()