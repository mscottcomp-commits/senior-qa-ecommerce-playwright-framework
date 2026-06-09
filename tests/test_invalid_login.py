def test_invalid_login_shows_error_message(page):
    # Go to the Sauce Demo login page
    page.goto("https://www.saucedemo.com/")

    # Enter invalid credentials
    page.fill("#user-name", "invalid_user")
    page.fill("#password", "wrong_password")

    # Click login
    page.click("#login-button")

    # Verify error message appears
    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert "Username and password do not match" in error_message.inner_text()