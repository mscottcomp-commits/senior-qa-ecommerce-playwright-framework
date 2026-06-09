class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = "#checkout"
        self.page_title = ".title"
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.error_message = "[data-test='error']"
        self.item_name = ".inventory_item_name"
        self.complete_header = ".complete-header"

    def start_checkout(self):
        # Click checkout from the cart page
        self.page.click(self.checkout_button)

    def get_page_title(self):
        # Return current checkout page title
        return self.page.locator(self.page_title).inner_text()

    def is_first_name_visible(self):
        return self.page.locator(self.first_name_input).is_visible()

    def is_last_name_visible(self):
        return self.page.locator(self.last_name_input).is_visible()

    def is_postal_code_visible(self):
        return self.page.locator(self.postal_code_input).is_visible()

    def fill_checkout_information(self, first_name="Michael", last_name="Scott", postal_code="12345"):
        # Fill out required checkout information
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)

    def fill_checkout_without_first_name(self, last_name="Scott", postal_code="12345"):
        # Fill checkout form while intentionally leaving first name blank
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)

    def continue_checkout(self):
        # Continue to checkout overview
        self.page.click(self.continue_button)

    def get_error_message(self):
        # Return checkout validation error text
        return self.page.locator(self.error_message).inner_text()

    def get_item_name(self):
        # Return item name shown during checkout
        return self.page.locator(self.item_name).inner_text()

    def finish_checkout(self):
        # Complete checkout
        self.page.click(self.finish_button)

    def get_complete_header(self):
        # Return checkout completion message
        return self.page.locator(self.complete_header).inner_text()