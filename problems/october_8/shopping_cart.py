
# Decorator function
def cart_decorator(func):
    def wrapper(*args, **kwargs):
        print("Cart calculation started")
        result = func(*args, **kwargs)
        print("Cart calculation completed")
        return result
    return wrapper


class ShoppingCart:
    def __init__(self):
        self.cart = {
            "Laptop": 50000,
            "Mouse": 1000,
            "Keyboard": 2000
        }

    # Add a product
    def add_product(self, name, price):
        self.cart[name] = price
        print(name, "added successfully!")

    # Remove a product
    def remove_product(self, name):
        try:
            del self.cart[name]
            print(name, "removed successfully!")
        except KeyError:
            print("Error: Product does not exist!")

    # Display all products
    def display_products(self):
        print("Shopping Cart Products:")
        for name, price in self.cart.items():
            print(name, ":", price)

    # Calculate total price using decorator
    @cart_decorator
    def calculate_total(self):
        total = sum(self.cart.values())
        print("Total Price:", total)
        return total


# Create an object
cart = ShoppingCart()

# Display products
cart.display_products()

# Calculate total
total = cart.calculate_total()

# Calculate 10% discount using lambda
discount = lambda price: price * 0.10
discount_amount = discount(total)

print("Discount (10%):", discount_amount)
print("Final Price:", total - discount_amount)

# Add a product
cart.add_product("Monitor", 10000)

# Remove a product
cart.remove_product("Mouse")

# Try removing a product that does not exist
cart.remove_product("Mobile")
