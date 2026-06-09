from helpers.auth_helpers import login
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from helpers.checkout_helpers import start_checkout


def test_user_can_start_checkout_from_cart(page):
    # Log in with valid credentials
    login(page)

    # Create page objects
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Add backpack to cart and open cart
    products_page.add_backpack_to_cart()
    cart_page.open_cart()

    # Start checkout
    start_checkout(page)

    # Verify checkout page loaded
    assert page.locator(".title").inner_text() == "Checkout: Your Information"

    # Verify checkout form fields are visible
    assert page.locator("#first-name").is_visible()
    assert page.locator("#last-name").is_visible()
    assert page.locator("#postal-code").is_visible()