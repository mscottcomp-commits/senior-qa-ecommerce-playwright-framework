from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self):
        # Open the Sauce Demo login page
        self.page.goto(BASE_URL)

    def enter_username(self, username):
        # Enter username
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        # Enter password
        self.page.fill(self.password_input, password)

    def click_login(self):
        # Click login button
        self.page.click(self.login_button)

    def login(self, username=STANDARD_USERNAME, password=STANDARD_PASSWORD):
        # Complete the full login flow
        self.navigate()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()