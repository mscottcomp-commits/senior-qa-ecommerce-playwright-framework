class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.page_title = ".title"
        self.inventory_items = ".inventory_item"
        self.backpack_add_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"
        self.sort_dropdown = ".product_sort_container"
        self.product_names = ".inventory_item_name"
        self.product_prices = ".inventory_item_price"

    def get_page_title(self):
        # Return the Products page title text
        return self.page.locator(self.page_title).inner_text()

    def get_inventory_count(self):
        # Return the number of inventory items displayed
        return self.page.locator(self.inventory_items).count()

    def add_backpack_to_cart(self):
        # Add Sauce Labs Backpack to the cart
        self.page.click(self.backpack_add_button)

    def get_cart_badge_count(self):
        # Return the cart badge text
        return self.page.locator(self.cart_badge).inner_text()

    def sort_by_name_z_to_a(self):
        # Sort products by name from Z to A
        self.page.select_option(self.sort_dropdown, "za")

    def sort_by_price_low_to_high(self):
        # Sort products by price from low to high
        self.page.select_option(self.sort_dropdown, "lohi")

    def get_first_product_name(self):
        # Return the first product name displayed
        return self.page.locator(self.product_names).first.inner_text()

    def get_all_product_prices(self):
        # Return all product prices as text values
        return self.page.locator(self.product_prices).all_inner_texts()