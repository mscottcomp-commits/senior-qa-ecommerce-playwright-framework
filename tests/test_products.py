from helpers.auth_helpers import login


def test_products_page_displays_inventory_items(page):
    # Log in with valid credentials
    login(page)

    # Verify we are on the Products page
    assert page.locator(".title").inner_text() == "Products"

    # Verify product items are displayed
    inventory_items = page.locator(".inventory_item")

    # Confirm at least one product appears
    assert inventory_items.count() > 0