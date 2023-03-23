"""
a. Only the uppercase letters in the string. 
b. Every second letter of the string. 
c. The string, with all vowels replaced by an underscore. 
d. The number of digits in the string. 
e. The number of vowels in the string. 
"""


user_string = input("This program wil check what a string contains: ")


def upperCase(string):
    for char in string:
        upper_chars = ""
        if char.isupper():
            upper_chars += char
            print(upper_chars, end="")


"""
def everySecondLetter(string):
    second_letters = ""
    i = 1
    for i in string:
        second_letters += string[i]
        i = i + 2
    print(second_letters)
"""


def everySecondLetter(string):
    second_letters = ""
    index = 1
    for letter in string:
        if index % 2 == 0:
            second_letters += letter
        index += 1
    print(second_letters)


def checkVowels(string):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        string = string.replace(vowel, "_")
    print(string)


def checkNums(string):
    amount_of_digits = 0
    for char in string:
        if char.isdigit():
            amount_of_digits += 1
    print(amount_of_digits)


def checkVowels(string):
    amount_of_vowels = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            amount_of_vowels += 1
    print(amount_of_vowels)

# checkNums(user_string)
# checkVowels(user_string)
# everySecondLetter(user_string)
# upperCase(user_string)
