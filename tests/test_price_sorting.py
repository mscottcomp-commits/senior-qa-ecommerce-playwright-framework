from helpers.auth_helpers import login


def test_user_can_sort_products_by_price_low_to_high(page):
    # Log in with valid credentials
    login(page)

    # Verify Products page loaded
    assert page.locator(".title").inner_text() == "Products"

    # Sort products by Price low to high
    page.select_option(".product_sort_container", "lohi")

    # Get all product prices from the page
    price_texts = page.locator(".inventory_item_price").all_inner_texts()

    # Convert prices from text like "$7.99" into numbers like 7.99
    prices = [float(price.replace("$", "")) for price in price_texts]

    # Verify prices are sorted from lowest to highest
    assert prices == sorted(prices)