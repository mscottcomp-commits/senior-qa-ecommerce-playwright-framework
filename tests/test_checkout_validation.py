from helpers.auth_helpers import login
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from helpers.checkout_helpers import start_checkout, continue_checkout


def test_checkout_requires_first_name(page):
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

    # Leave first name blank
    page.fill("#last-name", "Scott")
    page.fill("#postal-code", "12345")

    # Click continue
    continue_checkout(page)

    # Verify the correct error message appears
    assert page.locator("[data-test='error']").inner_text() == "Error: First Name is required"