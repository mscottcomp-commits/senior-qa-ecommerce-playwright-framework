from pages.login_page import LoginPage


def test_successful_login(page):
    # Create login page object
    login_page = LoginPage(page)

    # Log in with valid credentials
    login_page.login()

    # Verify the user lands on the Products page
    assert page.locator(".title").inner_text() == "Products"