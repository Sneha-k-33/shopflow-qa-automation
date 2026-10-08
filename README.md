ShopFlow QA Automation is a Python-based end-to-end QA automation framework designed for an e-commerce application.

The framework automates UI workflows using Playwright and Pytest, validates REST APIs and database state, and covers payment success, failure, refund, and webhook scenarios. It also demonstrates Salesforce/SOQL integration testing and automated CI execution through GitHub Actions.

The project additionally includes experiments with AI-assisted test generation to explore how AI can improve test design and automation workflows.

## Day 2 - Python + Test Data

### What I learned
- Used Python dictionaries to store test data.
- Practiced if / elif / else conditional logic.
- Created a reusable validate_user() function.
- Learned how Pytest discovers and runs test functions.
- Used assert statements to validate expected results.
- Added valid, invalid, empty, and partial user test cases.

### What I built
- utils/test_data.py - reusable SauceDemo test data and validation logic.
- tests/test_data_validation.py - Pytest tests for the validation utility.
- Added __init__.py files to support clean package imports.

### Test Result
4 tests passed successfully.

### Git
Commit: 5dbe397 feat: add test data validation utility