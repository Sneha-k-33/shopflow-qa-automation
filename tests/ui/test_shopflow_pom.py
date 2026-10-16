# tests/ui/test_shopflow_pom.py

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login_pom(page: Page):
    """Verify login flow using the Page Object Model architecture."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    products_page.verify_on_products_page()


@pytest.mark.ui
def test_add_product_to_cart_pom(page: Page):
    """Verify adding a product to the cart using page objects."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Add Backpack to Cart and navigate to cart
    product_name = "Sauce Labs Backpack"
    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart()

    # 3. Verify Cart
    cart_page.verify_on_cart_page()
    cart_page.verify_item_in_cart(product_name)