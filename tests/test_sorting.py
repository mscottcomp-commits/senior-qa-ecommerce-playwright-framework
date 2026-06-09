from helpers.auth_helpers import login
from pages.products_page import ProductsPage


def test_user_can_sort_products_by_name_z_to_a(page):
    # Log in with valid credentials
    login(page)

    # Create products page object
    products_page = ProductsPage(page)

    # Verify Products page loaded
    assert products_page.get_page_title() == "Products"

    # Sort products by Name Z to A
    products_page.sort_by_name_z_to_a()

    # Verify the first product is the expected item when sorted Z to A
    assert products_page.get_first_product_name() == "Test.allTheThings() T-Shirt (Red)"