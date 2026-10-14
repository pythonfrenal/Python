# Write a function count_vowels (word) that counts and returns 
# how many vowels are in the given word.


def count_vowels(word):
    count = 0

    for letter in word:
        if letter.lower() in "aeiou":
            count += 1

    return count


word = input("Enter a word: ")

print("Number of vowels:", count_vowels(word))


