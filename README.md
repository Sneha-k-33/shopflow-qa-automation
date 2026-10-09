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