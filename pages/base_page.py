# pages/base_page.py

class BasePage:
    """
    BasePage serves as the parent class for all Page Objects in ShopFlow.
    It encapsulates core browser actions and shared page behaviors.
    """
    
    def __init__(self, page):
        """
        Constructor method that initializes the page object with a Playwright page instance.
        """
        self.page = page

    def navigate_to(self, url):
        """
        Navigates the browser to a given URL.
        """
        self.page.goto(url)

    def get_current_title(self):
        """
        Returns the title of the current active browser page.
        """
        return self.page.title()