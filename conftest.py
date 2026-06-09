import os
import pytest


def pytest_configure(config):
    # Add custom metadata to the HTML report if pytest-html metadata is available
    metadata = getattr(config, "_metadata", None)

    if metadata is not None:
        metadata["Project"] = "Senior QA E-Commerce Automation Framework"
        metadata["Tester Role"] = "Senior QA Analyst expanding into Automation"
        metadata["Application Under Test"] = "Sauce Demo"
        metadata["Test Type"] = "Smoke / Regression"
        metadata["Browser"] = "Chromium"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook lets us inspect the test result after each test phase
    outcome = yield
    report = outcome.get_result()

    # Only take screenshots after the actual test call fails
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            print(f"Screenshot saved: {screenshot_path}")
BASE_URL = "https://www.saucedemo.com/"
STANDARD_USERNAME = "standard_user"
STANDARD_PASSWORD = "secret_sauce"