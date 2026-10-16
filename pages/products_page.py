# pages/products_page.py

from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):
    """Page Object for the SauceDemo Products/Inventory Catalog Page."""
    
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_icon = page.locator(".shopping_cart_link")

    def verify_on_products_page(self):
        """Verify that the user successfully reached the products inventory catalog."""
        expect(self.title).to_have_text("Products")

    def select_product(self, product_name):
        """Click on a specific product by its visible text."""
        self.page.get_by_text(product_name).click()

    def add_product_to_cart(self, product_name):
        """Add a specific product to the cart from the catalog view."""
        # Finds the product card and clicks its corresponding 'Add to cart' button
        item_card = self.page.locator(".inventory_item", has_text=product_name)
        item_card.get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        """Navigate to the shopping cart page."""
        self.cart_icon.click()