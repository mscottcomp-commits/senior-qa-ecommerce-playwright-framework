![Playwright Python Tests](https://github.com/mscottcomp-commits/senior-qa-ecommerce-playwright-framework/actions/workflows/playwright-tests.yml/badge.svg)
\# Senior QA E-Commerce Automation Framework



This project is a Playwright, Python, and pytest automation framework for testing core e-commerce workflows on the Sauce Demo practice website.



It was built from the perspective of a Senior QA Analyst expanding into automation, with a focus on practical regression coverage, readable test structure, reusable helpers, HTML reporting, and screenshots on failure.



\## Application Under Test



Sauce Demo  

https://www.saucedemo.com/



\## Tools Used



\- Python

\- Playwright

\- pytest

\- pytest-html

\- GitHub-ready project structure



\## Current Test Coverage



The framework currently validates:



\- Successful login

\- Invalid login error message

\- Product inventory display

\- Add product to cart

\- Start checkout from cart

\- Checkout required field validation

\- Full checkout completion

\- Logout/session validation

\- Product name sorting

\- Product price sorting



\## Framework Features



\- Reusable login helper

\- Reusable cart helper

\- Reusable checkout helper

\- Centralized config file

\- HTML test report generation

\- Screenshot capture on test failure

\- Organized test folder structure



\## Project Structure



```text

senior-qa-ecommerce-playwright-framework

│

├── helpers

│   ├── auth\_helpers.py

│   ├── cart\_helpers.py

│   └── checkout\_helpers.py

│

├── reports

│   └── report.html

│

├── screenshots

│

├── tests

│   ├── test\_cart.py

│   ├── test\_checkout.py

│   ├── test\_checkout\_complete.py

│   ├── test\_checkout\_validation.py

│   ├── test\_invalid\_login.py

│   ├── test\_login.py

│   ├── test\_logout.py

│   ├── test\_price\_sorting.py

│   ├── test\_products.py

│   └── test\_sorting.py

│

├── config.py

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md
How to Run the Tests



Create and activate a virtual environment:
python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

Install dependencies:
python -m pip install -r requirements.txt

python -m playwright install

Run all tests:



python -m pytest



Run a single test file:



python -m pytest tests\\test\_login.py

HTML Report



After running the tests, open:



reports/report.html

Screenshot on Failure



If a test fails, the framework automatically saves a screenshot in:



screenshots

QA Value



This framework demonstrates practical automation coverage for common e-commerce risks such as login access, product visibility, cart behavior, checkout flow, required field validation, sorting logic, reporting, and failure evidence.



It is designed to show how senior manual QA experience can be translated into maintainable automation coverage.





Save and close.



\## Step 3: Run tests again



```powershell

python -m pytest



Expected:



10 passed





