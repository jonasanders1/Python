"""
Write programs that read a line of input as a string and print
a. Only the uppercase letters in the string.
b. Every second letter of the string.
c. The string, with all vowels replaced by an underscore.
d. The number of digits in the string.
e. The positions of all vowels in the string.
"""


def checkForUpper(string):
    upper_chars = ""
    # for hver bokstav i setningen
    for char in string:
        # sjekk om bokstanven er stor
        if char.isupper():
            # hvis bokstaven er stor putt den store bokstaven inn i en variabel
            upper_chars += char
    print("Uppercase letters in the string:", upper_chars)


def everySecondLetter(string):
    second_letters = ""
    i = 1
    while i < len(string):
        second_letters += string[i]
        i = i + 2
    print("Every second letter of the string:", second_letters)


def checkForVowels(string):
    vowels = "AEIOUaeiou"
    i = 0
    for i in vowels:
        string = string.replace(i, "_")
    print("The string, with all vowels replaced by an underscore: ", string)


def checkForDigits(string):
    digits = 0
    # for hver bokstav i setningen
    for digit in string:
        # sjekk om bokstanven er stor
        if digit.isdigit():
            # hvis bokstaven er stor putt den store bokstaven inn i en variabel
            digits += 1
    print("The number of digits in the string: ", digits)


def checkVowelsPositon(string):
    vowels = "AEIOUaeiou"
    res = []
    for ele in range(len(string)):
        if string[ele] in vowels:
            res.append(ele + 1)
    print("The vowel indices are : " + str(res))


def main():
    while True:
        user_string = input(
            "This program will check what a string contains, enter a string: ")
        print("----> a. Only the uppercase letters in the string. \n----> b. Every second letter of the string. \n----> c. The string, with all vowels replaced by anunderscore.\n----> d. The number of digits in the string. \n----> e. The positions of all vowels in the string.")
        choise = input(
            "What do you want to check? ---> 'all' for all ---> 'exit' for exit: ")
        if choise == 'a':
            checkForUpper(user_string)
        elif choise == 'b':
            everySecondLetter(user_string)
        elif choise == 'c':
            checkForVowels(user_string)
        elif choise == 'd':
            checkForDigits(user_string)
        elif choise == 'e':
            checkVowelsPositon(user_string)
        elif choise == 'all':
            checkForUpper(user_string)
            everySecondLetter(user_string)
            checkForVowels(user_string)
            checkForDigits(user_string)
            checkVowelsPositon(user_string)
        elif choise == 'exit':
            quit()


main()
