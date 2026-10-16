# tests/ui/test_cart.py

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.ui
@pytest.mark.smoke
def test_cart_item_addition_and_validation(page: Page):
    """Verify adding an item updates cart count, displays correct quantity, and price."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_name = "Sauce Labs Backpack"
    products_page.add_product_to_cart(product_name)
    
    # 1. Verify cart badge count is 1
    assert cart_page.get_cart_count() == 1

    # 2. Navigate to cart and verify details
    products_page.go_to_cart()
    cart_page.verify_on_cart_page()

    # 3. Verify quantity and price
    assert cart_page.get_item_quantity(product_name) == 1
    assert cart_page.get_item_price(product_name) == 29.99


@pytest.mark.ui
def test_remove_item_from_cart(page: Page):
    """Verify removing an item from the cart updates the cart count and clears the item."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    product_name = "Sauce Labs Bike Light"
    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart()

    cart_page.verify_on_cart_page()
    assert cart_page.get_cart_count() == 1

    # Remove the item
    cart_page.remove_item_from_cart(product_name)
    
    # Verify cart count drops to 0 and item row is gone
    assert cart_page.get_cart_count() == 0
    expect(page.locator(".cart_item")).not_to_be_visible()