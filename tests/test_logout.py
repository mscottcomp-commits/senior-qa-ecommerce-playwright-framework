from helpers.auth_helpers import login


def test_user_can_logout(page):
    # Log in with valid credentials
    login(page)

    # Verify Products page loaded
    assert page.locator(".title").inner_text() == "Products"

    # Open the side menu
    page.click("#react-burger-menu-btn")

    # Click logout
    page.click("#logout_sidebar_link")

    # Verify user is returned to the login page
    assert page.locator("#login-button").is_visible()