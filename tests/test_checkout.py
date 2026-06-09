from helpers.auth_helpers import login
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_user_can_start_checkout_from_cart(page):
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

    # Verify checkout page loaded
    assert checkout_page.get_page_title() == "Checkout: Your Information"

    # Verify checkout form fields are visible
    assert checkout_page.is_first_name_visible()
    assert checkout_page.is_last_name_visible()
    assert checkout_page.is_postal_code_visible()