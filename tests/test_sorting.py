from helpers.auth_helpers import login


def test_user_can_sort_products_by_name_z_to_a(page):
    # Log in with valid credentials
    login(page)

    # Verify Products page loaded
    assert page.locator(".title").inner_text() == "Products"

    # Sort products by Name Z to A
    page.select_option(".product_sort_container", "za")

    # Get the first product name after sorting
    first_product_name = page.locator(".inventory_item_name").first.inner_text()

    # Verify the first product is the expected item when sorted Z to A
    assert first_product_name == "Test.allTheThings() T-Shirt (Red)"