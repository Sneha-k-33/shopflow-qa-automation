# tests/ui/test_complete_purchase.py

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.ui
@pytest.mark.smoke
def test_complete_checkout_flow(page: Page):
    """
    The ShopFlow Hero Test: Complete End-to-End E-Commerce Purchase Flow.
    Flow: Login -> Select Product -> Add to Cart -> Cart Validation -> 
          Checkout Information -> Order Summary -> Place Order -> Success Confirmation.
    """
    # Initialize Page Objects
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Login to SauceDemo
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    products_page.verify_on_products_page()

    # 2. Select product and add to cart
    product_name = "Sauce Labs Backpack"
    products_page.add_product_to_cart(product_name)
    
    # 3. Verify cart count badge updates and navigate to cart
    assert cart_page.get_cart_count() == 1
    products_page.go_to_cart()

    # 4. Verify cart items, quantities, and proceed to checkout
    cart_page.verify_on_cart_page()
    assert cart_page.get_item_quantity(product_name) == 1
    assert cart_page.get_item_price(product_name) == 29.99
    cart_page.proceed_to_checkout()

    # 5. Enter customer delivery details
    checkout_page.verify_on_checkout_page()
    checkout_page.fill_checkout_information("Sneha", "Vaghela", "300001")

    # 6. Verify order summary calculations (subtotal, tax, total)
    checkout_page.verify_checkout_summary()

    # 7. Place the order
    checkout_page.finish_checkout()

    # 8. Verify order confirmation success message
    checkout_page.verify_order_success()