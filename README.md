![Playwright Python Tests](https://github.com/mscottcomp-commits/senior-qa-ecommerce-playwright-framework/actions/workflows/playwright-tests.yml/badge.svg)


# Senior QA E-Commerce Automation Framework

This project is a Playwright, Python, and pytest automation framework for testing core e-commerce workflows on the Sauce Demo practice website.

It was built from the perspective of a Senior QA Analyst expanding into automation, with a focus on practical regression coverage, readable test structure, Page Object Model design, HTML reporting, screenshots on failure, and CI execution through GitHub Actions.

## Application Under Test

Sauce Demo  
https://www.saucedemo.com/

## Tools Used

- Python
- Playwright
- pytest
- pytest-html
- Git
- GitHub
- GitHub Actions

## Current Test Coverage

The framework currently validates:

- Successful login
- Invalid login error message
- Product inventory display
- Add product to cart
- Start checkout from cart
- Checkout required field validation
- Full checkout completion
- Logout/session validation
- Product name sorting
- Product price sorting

## Framework Features

- Page Object Model structure
- Reusable LoginPage object
- Reusable ProductsPage object
- Reusable CartPage object
- Reusable CheckoutPage object
- Centralized config file
- HTML test report generation
- Screenshot capture on test failure
- GitHub Actions CI/CD workflow
- GitHub Actions status badge
- Organized test folder structure

## Project Structure

```text
senior-qa-ecommerce-playwright-framework
│
├── .github
│   └── workflows
│       └── playwright-tests.yml
│
├── pages
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── helpers
│   ├── auth_helpers.py
│   ├── cart_helpers.py
│   └── checkout_helpers.py
│
├── reports
│   └── report.html
│
├── screenshots
│
├── tests
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_checkout_complete.py
│   ├── test_checkout_validation.py
│   ├── test_invalid_login.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_price_sorting.py
│   ├── test_products.py
│   └── test_sorting.py
│
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
How to Run the Tests

Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt
python -m playwright install

Run all tests:

python -m pytest

Run a single test file:

python -m pytest tests\test_login.py
HTML Report

After running the tests, open:

reports/report.html
Screenshot on Failure

If a test fails, the framework automatically saves a screenshot in:

screenshots
GitHub Actions CI/CD

This project includes a GitHub Actions workflow that automatically runs the Playwright test suite on push and pull request events.

Workflow file:

.github/workflows/playwright-tests.yml

The workflow installs Python dependencies, installs Playwright browsers, runs the pytest suite, and uploads the HTML report and screenshots as artifacts.

QA Value

This framework demonstrates practical automation coverage for common e-commerce risks such as login access, product visibility, cart behavior, checkout flow, required field validation, sorting logic, reporting, and failure evidence.

It shows how senior manual QA experience can be translated into maintainable automation coverage using Playwright, Python, pytest, Page Object Model, and CI/CD.


Save and close.

# Step 3: Run tests one last time

```powershell
python -m pytest

Expected:

10 passed