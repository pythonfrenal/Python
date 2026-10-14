# Create a class NumberAnalyzer with:
# python
# numbers = [10, 15, 22, 30, 41, 50]
# Create methods to:
# - Print all numbers using a for loop.
# - Print even numbers.
# - Print odd numbers.
# - Calculate the total.
# - Calculate the average.
# - Use a condition to print "High" if the average is above 25, 
# otherwise "Low".

class NumberAnalyzer:

    numbers = [10, 15, 22, 30, 41, 50]

    # Print all numbers
    def display_numbers(self):
        print("All Numbers:")
        for number in self.numbers:
            print(number)

    # Print even numbers
    def display_even(self):
        print("\nEven Numbers:")
        for number in self.numbers:
            if number % 2 == 0:
                print(number)

    # Print odd numbers
    def display_odd(self):
        print("\nOdd Numbers:")
        for number in self.numbers:
            if number % 2 != 0:
                print(number)

    # Calculate total
    def calculate_total(self):
        total = 0
        for number in self.numbers:
            total += number
        print("\nTotal:", total)
        return total

    # Calculate average
    def calculate_average(self):
        total = self.calculate_total()
        average = total / len(self.numbers)
        print("Average:", average)
        return average

    # Check average
    def check_average(self):
        average = self.calculate_average()

        if average > 25:
            print("High")
        else:
            print("Low")


# Create object
analyzer = NumberAnalyzer()

analyzer.display_numbers()
analyzer.display_even()
analyzer.display_odd()
analyzer.check_average()
