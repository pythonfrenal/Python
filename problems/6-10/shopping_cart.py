class ShoppingCart:

    def __init__(self):
        self.cart = {
            "Laptop": 50000,
            "Mouse": 1000,
            "Keyboard": 2000
        }

    # Display all products
    def display_products(self):
        print("Products in Cart:")
        for product, price in self.cart.items():
            print(product, ":", price)

    # Calculate total price
    def total_price(self):
        return sum(self.cart.values())

    # Add a new product
    def add_product(self, product, price):
        self.cart[product] = price
        print(product, "added successfully.")

    # Remove a product
    def remove_product(self, product):
        try:
            del self.cart[product]
            print(product, "removed successfully.")
        except KeyError:
            print("Error: Product does not exist.")

    # Access a product
    def get_product(self, product):
        try:
            print(product, "price:", self.cart[product])
        except KeyError:
            print("Error: Product does not exist.")

    # Apply discount
    def apply_discount(self):
        total = self.total_price()

        if total > 50000:
            discount = lambda price: price * 0.90
            discounted_price = discount(total)

            print("Original Total:", total)
            print("10% Discount Applied")
            print("Final Price:", discounted_price)
        else:
            print("No discount applied.")
            print("Total Price:", total)


# Create object
cart = ShoppingCart()

# Display products
cart.display_products()

# Calculate total
print("\nTotal Price:", cart.total_price())

# Add new product
print()
cart.add_product("Headphones", 3000)

# Remove product
cart.remove_product("Mouse")

# Try to remove a product that does not exist
cart.remove_product("Mobile")

# Access an existing product
print()
cart.get_product("Laptop")

# Try to access a product that does not exist
cart.get_product("Tablet")

# Apply discount
print()
cart.apply_discount()