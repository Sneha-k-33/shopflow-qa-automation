# tests/ui/test_checkout.py

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.ui
@pytest.mark.smoke
def test_successful_checkout_flow(page: Page):
    """Verify complete E2E flow: Login -> Products -> Cart -> Checkout -> Success."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Login and add product to cart
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    product_name = "Sauce Labs Backpack"
    products_page.add_product_to_cart(product_name)
    products_page.go_to_cart()

    # 2. Proceed from cart to checkout
    cart_page.verify_on_cart_page()
    cart_page.proceed_to_checkout()

    # 3. Fill valid customer details and verify summary
    checkout_page.verify_on_checkout_page()
    checkout_page.fill_checkout_information("Sneha", "Vaghela", "300001")
    checkout_page.verify_checkout_summary()

    # 4. Finish order and verify success screen
    checkout_page.finish_checkout()
    checkout_page.verify_order_success()


@pytest.mark.ui
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Vaghela", "300001", "Error: First Name is required"),
        ("Sneha", "", "300001", "Error: Last Name is required"),
        ("Sneha", "Vaghela", "", "Error: Postal Code is required"),
    ],
)
def test_checkout_form_missing_fields(page: Page, first_name, last_name, postal_code, expected_error):
    """Verify form validation error messages when required checkout fields are missing."""
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Navigate to checkout info form
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.go_to_cart()
    cart_page.proceed_to_checkout()

    # 2. Submit form with missing data
    checkout_page.verify_on_checkout_page()
    checkout_page.fill_checkout_information(first_name, last_name, postal_code)

    # 3. Validate correct error message is displayed
    error_text = checkout_page.get_error_message()
# 3. Validate correct error message is displayed
    error_text = checkout_page.get_error_message()
    assert expected_error in error_text, f"Expected error '{expected_error}' not found in '{error_text}'"