# Write a program that reads a word and print the first letter of the word and stars instead of the other words

word = input()
first_letter = word[0]
remanining_letters = len(word) - 1
star = "*" * remanining_letters
print(first_letter + star)