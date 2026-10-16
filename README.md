# ShopFlow QA Automation Framework

ShopFlow QA Automation is a Python-based end-to-end QA automation framework designed for an e-commerce application.

The framework automates UI workflows using Playwright and Pytest, validates REST APIs and database state, and covers payment success, failure, refund, and webhook scenarios. It also demonstrates Salesforce/SOQL integration testing and automated CI execution through GitHub Actions.

The project additionally includes experiments with AI-assisted test generation to explore how AI can improve test design and automation workflows.

---

## 📅 Daily Progress Log

### Day 1 — Framework Setup
- Initialized repository structure (`api/`, `pages/`, `tests/`, `utils/`, `test_data/`, `docs/`).
- Configured Python virtual environment and `requirements.txt`.
- Pushed initial project layout to GitHub.

---

### Day 2 — Python + Test Data

#### What I Learned
- Stored structured test data using Python dictionaries.
- Implemented conditional control flow using `if`, `elif`, `else`, and `and` logical operators.
- Created reusable data processing and validation functions.
- Applied Pytest test discovery rules, assertions, dynamic `for` loop iterations, and `while` loop retry logic.
- Managed edge cases including valid, invalid, empty, and partial user credentials.

#### What I Built
- `utils/test_data.py` — Reusable SauceDemo user test data and `validate_user()` function.
- `tests/test_data_validation.py` — Pytest test suite validating user credentials and loop behaviors.
- Package initializers (`__init__.py`) to support clean modular imports across the project.

#### Test Results
```text
tests/test_data_validation.py PASSED [100%]
============================== 6 passed in 0.29s ==============================

### Day 3 — Python Functions & Order Lifecycle Model

**What I Learned**
* Implemented reusable Python functions with parameters and return values.
* Manipulated complex nested dictionaries and lists representing e-commerce order models.
* Performed list iteration and math aggregations using generator expressions (`sum(...) for item in items`).
* Managed order state transitions with business rule dictionaries.
* Applied Pytest fixtures (`@pytest.fixture`) to supply clean test data across multiple test functions.

**What I Built**
* `utils/order_model.py` — Core order logic including `calculate_order_total()` (handling 8% tax and optional discounts), `validate_order()`, and `update_order_status()`.
* `tests/test_order_model.py` — Comprehensive unit test suite using fixtures to validate calculation accuracy, field validation rules, and status transitions.

**Test Results**
```text
collected 12 items
============================== 12 passed in 0.04s ==============================

### Day 4 — Exceptions, JSON & File I/O

**What I Learned**
* Externalized test data from Python code into modular JSON configuration files (`users.json`, `products.json`, `payments.json`).
* Implemented defensive programming using `try`, `except`, and `finally` exception handling blocks.
* Handled specific runtime errors such as `FileNotFoundError` and `json.JSONDecodeError`.
* Validated exception-throwing test cases using Pytest's `pytest.raises()`.

**What I Built**
* `utils/file_reader.py` — Reusable utility function `load_json_data()` providing safe file reading and resource cleanup.
* `tests/test_file_reader.py` — Unit test suite validating successful JSON parsing across multiple domains and ensuring proper exception raising for missing files.

**Test Results**
```text
collected 16 items
============================== 16 passed in 0.04s ==============================

Here is the README update snippet for **Day 5**, formatted to match your structure:

---

### Day 5 — Python OOP & Page Object Model Foundation

**What I Learned**

* Mastered Object-Oriented Programming (OOP) fundamentals in Python (`class`, `object`).
* Implemented initializer constructors (`__init__`) to automatically assign instance variables (such as `self.page`).
* Encapsulated reusable browser actions and page behaviors into class methods.
* Explored basic class inheritance (`super().__init__`) to structure parent and child page objects for the Page Object Model (POM) architecture.

**What I Built**

* `pages/base_page.py` — Foundational parent class (`BasePage`) designed to encapsulate core browser interactions and shared navigation methods for all future page objects.
* `tests/test_base_page.py` — Unit test suite verifying class initialization, attribute assignment, and basic method inheritance.

**Test Results**

```text
tests/test_base_page.py::test_base_page_initialization PASSED
tests/test_base_page.py::test_inheritance_and_methods PASSED

```

Here is the README update snippet for **Day 6**, formatted to match your structure:

---

### Day 6 — Advanced Pytest, Unit Testing, Parametrization & Markers

**What I Learned**

* Discovered core Pytest orchestration concepts including automated test discovery and test execution output (`pytest -v`).
* Mastered assertions (`assert`) for verifying equality, data types, strings, lists, and dictionary structures.
* Implemented fixtures (`@pytest.fixture`) and shared them globally across test suites using `conftest.py`.
* Automated data-driven test execution using `@pytest.mark.parametrize` to run a single test function across multiple datasets and boundary conditions.
* Categorized and filtered test execution using custom markers (`@pytest.mark.smoke`, `@pytest.mark.payment`) configured via `pytest.ini`.

**What I Built**

* `pytest.ini` — Global configuration file defining test search paths, minimum versions, and custom test markers.
* `tests/unit/` — Dedicated directory for isolating granular unit-level test suites.
* `tests/unit/test_payment_unit.py` — Comprehensive unit test suite featuring standard assertions, curriculum-aligned exercises, and advanced parametrized boundary checks.

**Test Results**

```text
collected 28 items
============================== 28 passed in 0.05s ==============================

```

## 🚀 Day 7 — First Real Browser Automation with Playwright

### Overview
Day 7 marks the exciting transition from testing pure Python logic and unit data to executing **real-world UI browser automation**. We integrated Microsoft Playwright with Pytest to automate an end-to-end user login workflow on the SauceDemo practice e-commerce application.

### 🛠️ What We Built
* **`tests/ui/`** — A dedicated directory structure to house all browser-based UI automation test suites.
* **`tests/ui/test_login.py`** — An end-to-end UI automation test validating the SauceDemo login and inventory navigation flow.

### 💻 Key Code Implementation (`tests/ui/test_login.py`)
```python
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
    page.goto("[https://www.saucedemo.com/](https://www.saucedemo.com/)")
    
    # 2. Login (Enter username, password, and click login)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # 3. Verify Products page (Check URL and page header title)
    expect(page).to_have_url("[https://www.saucedemo.com/inventory.html](https://www.saucedemo.com/inventory.html)")
    expect(page.locator(".title")).to_have_text("Products")

    Here is the README content for Day 7 and Day 8 formatted precisely as requested:

---

### Day 7 — First Real Browser Automation with Playwright

**What I Learned**

* Core browser automation fundamentals using Microsoft Playwright.
* Integrating Pytest with the `pytest-playwright` plugin for automatic browser fixture management.
* Executing tests in headless mode (default) vs. headed mode (`--headed`) for visual debugging.
* Automating real-world user workflows on the SauceDemo e-commerce application.

**What I Built**

* `tests/ui/` — Dedicated directory for browser-based UI automation tests.
* `tests/ui/test_login.py` — End-to-end UI automation test covering website navigation, standard credential authentication, and inventory page validation.

**Test Results**

```text
tests\ui\test_login.py .                                                     [100%]
======================================== 1 passed in 6.28s =========================================

```

---

### Day 8 — Playwright Robust Locators & UI Test Suite

**What I Learned**

* Playwright's robust, user-facing locator strategies and their priority order (`get_by_role`, `get_by_label`, `get_by_text`, `get_by_test_id`, and generic `locator`).
* How to avoid fragile, tightly-coupled XPath or CSS selectors that break during front-end refactoring.
* Leveraging semantic locators to match how real users and screen readers interact with web elements.

**What I Built**

* Expanded UI test suite (`tests/ui/test_shopflow_ui.py` / `test_login.py`) incorporating robust locator patterns.
* `test_valid_login` — Robust login flow utilizing placeholder and role locators.
* `test_product_displayed` — Catalog verification ensuring products appear on screen using visible text locators.
* `test_product_details` — Item detail navigation and price/description validation test.

**Test Results**

```text
tests\ui\test_shopflow_ui.py ...                                              [100%]
======================================== 3 passed in 35.55s ========================================

```

Day 9 — Page Object Model (POM) Refactoring
What I Learned

The Page Object Model (POM) architectural design pattern used by enterprise QA automation engineers.

How to decouple test logic from UI element selectors and action code to maximize maintainability.

Utilizing Python class inheritance (BasePage) to share core browser capabilities across multiple page classes.

Encapsulating page-specific elements in constructors (__init__) and organizing actions into domain-specific methods (e.g., login(), add_product_to_cart()).

What I Built

pages/login_page.py — Page object handling SauceDemo authentication elements and actions.

pages/products_page.py — Page object managing the inventory catalog, product selection, and cart navigation.

pages/cart_page.py — Page object validating shopping cart items and checkout transitions.

tests/ui/test_shopflow_pom.py — Clean, readable E-commerce UI test suite utilizing the new page objects.

Test Results

Plaintext
tests\ui\test_shopflow_pom.py ..                                              [100%]
======================================== 2 passed in 12.07s ========================================

