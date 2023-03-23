letter = input("Enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
# if letter in "aeiouAEIOU"
# if letter.lower() in "aeiou"
    print("It's a vowel.")

elif letter == "y":
    print("Sometimes it's a vowel ... Sometimes it's a consonant.")
    
else:
    print("It's a consonant")