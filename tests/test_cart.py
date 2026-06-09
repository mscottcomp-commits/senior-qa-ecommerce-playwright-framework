from helpers.auth_helpers import login
from helpers.cart_helpers import open_cart
from pages.products_page import ProductsPage


def test_user_can_add_product_to_cart(page):
    # Log in with valid credentials
    login(page)

    # Create products page object
    products_page = ProductsPage(page)

    # Add backpack to cart
    products_page.add_backpack_to_cart()

    # Verify the cart badge shows 1 item
    assert products_page.get_cart_badge_count() == "1"

    # Open the cart
    open_cart(page)

    # Verify the correct product is in the cart
    assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"