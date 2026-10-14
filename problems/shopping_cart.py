# Create a class ShoppingCart with a dictionary:
# python
# products = {
#     "Laptop": 50000,
#     "Mouse": 1000,
#     "Keyboard": 2000
# }
# Create methods to:

# - Display all products using a for loop.
# - Calculate the total price.
# - Apply a 10% discount if the total is greater than 50000.
# - Display the final price.


class ShoppingCart:

    products = {
        "Laptop": 50000,
        "Mouse": 1000,
        "Keyboard": 2000
    }

    # Display all products
    def display_products(self):
        print("Available Products:")
        for product, price in self.products.items():
            print(product, ":", price)

    # Calculate total price
    def calculate_total(self):
        total = 0
        for price in self.products.values():
            total += price
        return total

    # Calculate discount and final price
    def display_final_price(self):
        total = self.calculate_total()

        print("\nTotal Price:", total)

        if total > 50000:
            discount = total * 10 / 100
            final_price = total - discount
            print("Discount (10%):", discount)
        else:
            final_price = total
            print("No discount applied.")

        print("Final Price:", final_price)


# Create object
cart = ShoppingCart()

cart.display_products()
cart.display_final_price()