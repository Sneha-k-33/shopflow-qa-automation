# tests/ui/test_products.py

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.ui
@pytest.mark.smoke
def test_product_catalog_display_and_details(page: Page):
    """Verify product list, names, prices, and product details page navigation."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    products_page.verify_on_products_page()

    # 1. Verify product list contains expected items and prices
    names = products_page.get_product_names()
    prices = products_page.get_product_prices()
    
    assert len(names) > 0, "Product list is empty!"
    assert "Sauce Labs Backpack" in names
    assert 29.99 in prices

    # 2. Click product and verify details view
    products_page.click_product_name("Sauce Labs Backpack")
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".inventory_details_price")).to_have_text("$29.99")


@pytest.mark.ui
def test_product_sorting(page: Page):
    """Verify product sorting functionality (Price Low-to-High and Name Z-to-A)."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    products_page.verify_on_products_page()

    # 1. Sort by Price: Low to High ("lohi")
    products_page.sort_products("lohi")
    prices = products_page.get_product_prices()
    assert prices == sorted(prices), "Prices are not sorted correctly (Low to High)!"

    # 2. Sort by Name: Z to A ("za")
    products_page.sort_products("za")
    names = products_page.get_product_names()
    assert names == sorted(names, reverse=True), "Product names are not sorted correctly (Z to A)!"


@pytest.mark.ui
def test_add_product_from_catalog(page: Page):
    """Verify adding a product to the cart directly from the product list."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    product_name = "Sauce Labs Bike Light"
    products_page.add_product_to_cart(product_name)
    
    # Verify the button changes to 'Remove' upon adding
    item_card = page.locator(".inventory_item", has_text=product_name)
    expect(item_card.get_by_role("button", name="Remove")).to_be_visible()