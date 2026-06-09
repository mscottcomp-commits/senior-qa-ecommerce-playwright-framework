from helpers.auth_helpers import login
from helpers.cart_helpers import add_backpack_to_cart, open_cart
from helpers.checkout_helpers import start_checkout


def test_user_can_start_checkout_from_cart(page):
    # Log in with valid credentials
    login(page)

    # Add backpack to cart and open cart
    add_backpack_to_cart(page)
    open_cart(page)

    # Start checkout
    start_checkout(page)

    # Verify checkout page loaded
    assert page.locator(".title").inner_text() == "Checkout: Your Information"

    # Verify checkout form fields are visible
    assert page.locator("#first-name").is_visible()
    assert page.locator("#last-name").is_visible()
    assert page.locator("#postal-code").is_visible()