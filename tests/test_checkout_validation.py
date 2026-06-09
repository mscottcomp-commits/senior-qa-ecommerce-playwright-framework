from helpers.auth_helpers import login
from helpers.cart_helpers import add_backpack_to_cart, open_cart
from helpers.checkout_helpers import start_checkout, continue_checkout


def test_checkout_requires_first_name(page):
    # Log in with valid credentials
    login(page)

    # Add backpack to cart and open cart
    add_backpack_to_cart(page)
    open_cart(page)

    # Start checkout
    start_checkout(page)

    # Leave first name blank
    page.fill("#last-name", "Scott")
    page.fill("#postal-code", "12345")

    # Click continue
    continue_checkout(page)

    # Verify the correct error message appears
    assert page.locator("[data-test='error']").inner_text() == "Error: First Name is required"