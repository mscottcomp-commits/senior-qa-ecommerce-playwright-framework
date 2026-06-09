from helpers.auth_helpers import login
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_user_can_complete_checkout(page):
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

    # Fill out checkout information
    checkout_page.fill_checkout_information()

    # Continue to checkout overview
    checkout_page.continue_checkout()

    # Verify checkout overview page loaded
    assert checkout_page.get_page_title() == "Checkout: Overview"

    # Verify product is still listed before completing order
    assert checkout_page.get_item_name() == "Sauce Labs Backpack"

    # Finish checkout
    checkout_page.finish_checkout()

    # Verify order confirmation page loaded
    assert checkout_page.get_page_title() == "Checkout: Complete!"

    # Verify confirmation message appears
    assert checkout_page.get_complete_header() == "Thank you for your order!"