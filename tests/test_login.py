from helpers.auth_helpers import login


def test_successful_login(page):
    # Log in with valid credentials
    login(page)

    # Verify the user lands on the Products page
    assert page.locator(".title").inner_text() == "Products"