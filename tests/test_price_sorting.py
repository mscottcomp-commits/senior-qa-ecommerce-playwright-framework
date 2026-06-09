from helpers.auth_helpers import login
from pages.products_page import ProductsPage


def test_user_can_sort_products_by_price_low_to_high(page):
    # Log in with valid credentials
    login(page)

    # Create products page object
    products_page = ProductsPage(page)

    # Verify Products page loaded
    assert products_page.get_page_title() == "Products"

    # Sort products by Price low to high
    products_page.sort_by_price_low_to_high()

    # Get all product prices from the page
    price_texts = products_page.get_all_product_prices()

    # Convert prices from text like "$7.99" into numbers like 7.99
    prices = [float(price.replace("$", "")) for price in price_texts]

    # Verify prices are sorted from lowest to highest
    assert prices == sorted(prices)