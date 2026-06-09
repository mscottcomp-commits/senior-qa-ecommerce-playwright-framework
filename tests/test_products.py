from helpers.auth_helpers import login
from pages.products_page import ProductsPage


def test_products_page_displays_inventory_items(page):
    # Log in with valid credentials
    login(page)

    # Create products page object
    products_page = ProductsPage(page)

    # Verify we are on the Products page
    assert products_page.get_page_title() == "Products"

    # Confirm at least one product appears
    assert products_page.get_inventory_count() > 0