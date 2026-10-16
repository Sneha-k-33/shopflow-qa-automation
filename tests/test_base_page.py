# tests/test_base_page.py

import pytest
from pages.base_page import BasePage

# Optional: Creating a dummy child class to demonstrate basic inheritance
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # Calls the parent constructor

    def get_login_header(self):
        return "Please Login"


def test_base_page_initialization():
    # Mocking a page object or passing None for logic testing
    base_page = BasePage(page="mock_page_instance")
    assert base_page.page == "mock_page_instance"


def test_inheritance_and_methods():
    # Verify that child class inherits from BasePage and retains constructor properties
    login_page = LoginPage(page="mock_browser_page")
    assert login_page.page == "mock_browser_page"
    assert login_page.get_login_header() == "Please Login"