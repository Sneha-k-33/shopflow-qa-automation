# pages/login_page.py

from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Page."""
    
    def __init__(self, page):
        super().__init__(page)
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        """Navigate to the SauceDemo login URL."""
        self.navigate_to("https://www.saucedemo.com/")

    def login(self, username, password):
        """Perform login action with given credentials."""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()