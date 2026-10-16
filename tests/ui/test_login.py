# tests/ui/test_login.py

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_login_success(page: Page):
    """
    Verify successful login to SauceDemo and transition to the Products inventory page.
    Flow: Open website -> Login with standard credentials -> Verify Products page
    """
    # 1. Open website
    page.goto("https://www.saucedemo.com/")
    
    # 2. Login (Enter username, password, and click login)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # 3. Verify Products page (Check URL and page header title)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")