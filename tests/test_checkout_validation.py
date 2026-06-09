from helpers.auth_helpers import login
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_requires_first_name(page):
    # Log in with valid credentials
    login(page)

    # Create page objects
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Add backpack to cart and open cart
    products_page.add_backpack_to_cart()
    cart_page.open_cart()

    # Start checkout
    checkout_page.start_checkout()

    # Leave first name blank
    checkout_page.fill_checkout_without_first_name()

    # Click continue
    checkout_page.continue_checkout()

    # Verify the correct error message appears
    assert checkout_page.get_error_message() == "Error: First Name is required"