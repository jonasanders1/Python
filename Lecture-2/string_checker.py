print("This program wil check what a string contains: ")
user_string = input("Enter a string: ")


def check_string(string):
    print("The string is all characters: ", string.isalpha())
    print("The string is a digit: ", string.isdigit())
    print("The string is all lowecase: ", string.islower())
    print("The string is all uppercase: ", string.isupper())
    print("The string starts with a uppercase: ", string[0].isupper())
    print("The string ends with a period: ", string.endswith("."))


def main():
    check_string(user_string)


main()
