# tests/ui/test_shopflow_ui.py

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_login_flow(page: Page):
    """Verify user can log in successfully using robust placeholder and role locators."""
    page.goto("https://www.saucedemo.com/")
    
    # Use placeholder-based locators instead of fragile IDs
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    
    # Use role-based locator for the button
    page.get_by_role("button", name="Login").click()
    
    # Verify inventory redirect
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


@pytest.mark.ui
def test_product_is_displayed(page: Page):
    """Verify specific products are visible on the inventory catalog."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Verify product text is visible using get_by_text
    backpack = page.get_by_text("Sauce Labs Backpack")
    expect(backpack).to_be_visible()
    
    bike_light = page.get_by_text("Sauce Labs Bike Light")
    expect(bike_light).to_be_visible()


@pytest.mark.ui
def test_product_details_navigation(page: Page):
    """Verify clicking a product navigates to its detail page and shows key info."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Click on the product title link/text
    page.get_by_text("Sauce Labs Backpack").click()
    
    # Verify we are on the item detail view
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    
    # Verify product title and description elements are present
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".inventory_details_desc")).to_be_visible()
    
    # Return back to products inventory using role locator
    page.get_by_role("button", name="Back to products").click()
    expect(page.locator(".title")).to_have_text("Products")