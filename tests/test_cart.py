from helpers.auth_helpers import login
from helpers.cart_helpers import add_backpack_to_cart, open_cart


def test_user_can_add_product_to_cart(page):
    # Log in with valid credentials
    login(page)

    # Add backpack to cart
    add_backpack_to_cart(page)

    # Verify the cart badge shows 1 item
    assert page.locator(".shopping_cart_badge").inner_text() == "1"

    # Open the cart
    open_cart(page)

    # Verify the correct product is in the cart
    assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"