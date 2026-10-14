# Print numbers divisible by 3 and 5 between 1-100.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number)
        