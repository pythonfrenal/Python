# Find the maximum number from a list without using max().

numbers = [10, 25, 7, 45, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Maximum number:", largest)
