from helpers.auth_helpers import login
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_user_can_add_product_to_cart(page):
    # Log in with valid credentials
    login(page)

    # Create page objects
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # Add backpack to cart
    products_page.add_backpack_to_cart()

    # Verify the cart badge shows 1 item
    assert products_page.get_cart_badge_count() == "1"

    # Open the cart
    cart_page.open_cart()

    # Verify the correct product is in the cart
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"