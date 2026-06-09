def start_checkout(page):
    # Click the checkout button from the cart page
    page.click("#checkout")


def fill_checkout_information(page, first_name="Michael", last_name="Scott", postal_code="12345"):
    # Fill out required checkout customer information
    page.fill("#first-name", first_name)
    page.fill("#last-name", last_name)
    page.fill("#postal-code", postal_code)


def continue_checkout(page):
    # Continue to checkout overview
    page.click("#continue")