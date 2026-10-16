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

# pages/cart_page.py

from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    """Page Object for the SauceDemo Shopping Cart Page."""
    
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def verify_on_cart_page(self):
        """Verify that the user is on the cart page."""
        expect(self.title).to_have_text("Your Cart")

    def get_cart_count(self):
        """Return the count number displayed on the shopping cart badge."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def get_item_quantity(self, product_name):
        """Get the quantity of a specific item in the cart."""
        item_row = self.cart_items.filter(has_text=product_name)
        return int(item_row.locator(".cart_quantity").inner_text())

    def get_item_price(self, product_name):
        """Get the price of a specific item in the cart as a float."""
        item_row = self.cart_items.filter(has_text=product_name)
        price_text = item_row.locator(".inventory_item_price").inner_text()
        return float(price_text.replace("$", ""))

    def remove_item_from_cart(self, product_name):
        """Remove a specific item from the cart page."""
        item_row = self.cart_items.filter(has_text=product_name)
        item_row.get_by_role("button", name="Remove").click()

    def proceed_to_checkout(self):
        """Click the checkout button."""
        self.checkout_button.click()