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


        # pages/products_page.py

from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):
    """Page Object for the SauceDemo Products/Inventory Catalog Page."""
    
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.inventory_items = page.locator(".inventory_item")

    def verify_on_products_page(self):
        """Verify that the user successfully reached the products inventory catalog."""
        expect(self.title).to_have_text("Products")

    def get_product_names(self):
        """Retrieve a list of all product names visible on the catalog."""
        return self.inventory_items.locator(".inventory_item_name").all_inner_texts()

    def get_product_prices(self):
        """Retrieve a list of all product prices as floats for validation."""
        prices_text = self.inventory_items.locator(".inventory_item_price").all_inner_texts()
        return [float(p.replace("$", "")) for p in prices_text]

    def sort_products(self, option_value):
        """
        Sort products using the dropdown container.
        Options: 'az' (Name A-Z), 'za' (Name Z-A), 'lohi' (Price low-high), 'hilo' (Price high-low)
        """
        self.sort_dropdown.select_option(value=option_value)

    def click_product_name(self, product_name):
        """Click on a specific product name to view its details page."""
        self.page.get_by_text(product_name).click()

    def add_product_to_cart(self, product_name):
        """Add a specific product to the cart from the catalog view."""
        item_card = self.page.locator(".inventory_item", has_text=product_name)
        item_card.get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        """Navigate to the shopping cart page."""
        self.cart_icon.click()