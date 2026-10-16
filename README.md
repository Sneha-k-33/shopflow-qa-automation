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