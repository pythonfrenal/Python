# Write a function reverse_string(text) that returns the reversed version of the string.

def reverse_string(text):
    return text[::-1]


word = input("Enter a string: ")

result = reverse_string(word)

print("Reversed string:", result)
