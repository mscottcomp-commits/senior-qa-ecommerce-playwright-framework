from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD


def login(page, username=STANDARD_USERNAME, password=STANDARD_PASSWORD):
    # Go to the Sauce Demo login page
    page.goto(BASE_URL)

    # Enter username
    page.fill("#user-name", username)

    # Enter password
    page.fill("#password", password)

    # Click login
    page.click("#login-button")