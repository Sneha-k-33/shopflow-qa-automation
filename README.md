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