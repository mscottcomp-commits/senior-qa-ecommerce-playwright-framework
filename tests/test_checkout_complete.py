from helpers.auth_helpers import login
from helpers.cart_helpers import add_backpack_to_cart, open_cart
from helpers.checkout_helpers import start_checkout, fill_checkout_information, continue_checkout


def test_user_can_complete_checkout(page):
    # Log in with valid credentials
    login(page)

    # Add backpack to cart and open cart
    add_backpack_to_cart(page)
    open_cart(page)

    # Start checkout
    start_checkout(page)

    # Fill out checkout information
    fill_checkout_information(page)

    # Continue to checkout overview
    continue_checkout(page)

    # Verify checkout overview page loaded
    assert page.locator(".title").inner_text() == "Checkout: Overview"

    # Verify product is still listed before completing order
    assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"

    # Finish checkout
    page.click("#finish")

    # Verify order confirmation page loaded
    assert page.locator(".title").inner_text() == "Checkout: Complete!"

    # Verify confirmation message appears
    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"