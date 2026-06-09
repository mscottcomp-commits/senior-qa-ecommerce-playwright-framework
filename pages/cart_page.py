class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_link = ".shopping_cart_link"
        self.cart_item_name = ".inventory_item_name"
        self.checkout_button = "#checkout"

    def open_cart(self):
        # Open the shopping cart page
        self.page.click(self.cart_link)

    def get_cart_item_name(self):
        # Return the item name displayed in the cart
        return self.page.locator(self.cart_item_name).inner_text()

    def click_checkout(self):
        # Click the checkout button from the cart page
        self.page.click(self.checkout_button)