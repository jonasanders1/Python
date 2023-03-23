# 2. Program that validaes the users input and gives feedback


def welcome_user():
    print("Welcome to the number input program!")


def validate_number(number):
    if number < 1:
        print("The number you entered is < 1")
    elif number > 10:
        print("The number you entered is > 10")
    else:
        print(f"The number you entered ({number}) is in the range 1 - 10!")


def main():
    welcome_user()
    user_number = int(input("Enter a number: "))
    validate_number(user_number)


main()
