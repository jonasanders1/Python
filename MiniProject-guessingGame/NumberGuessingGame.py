
from enum import Enum
import random  # For a random number


# Game function is responible for running the game:
# --> 1. Create a random number
# --> 2. Set amount of guesses to 5
#    --> 3. Create a while loop that runs until the user guesses is 0
#       --> 4. Inside the loop, aks for a guess from the user
#       --> 5. Decrement the user guesses each iteration of the loop
#          --> 6. Check if the user guess is equal to, less or grater than the random number
#             -- 7. If user guess is less than the random number print message (the loop wil continue)
#             -- 8. If user guess is greater than the random number print message (the loop wil continue)
#             -- 9. If user guess is equal to the random number print message and call retry function
#          --> 10. Outside the while, if the guesses is 0 and user has not guessed correct yet, call retry function

def Game():
    # Random number
    numer_to_guess = random.randint(1, 100)
    # print(numer_to_guess)
    # Amount of user guesses
    user_guesses = 5
    print(" ")
    print("------ WELCOME TO GUESS THE NUMBER ( 1 - 1000 ) ------")
    print(" ")
    # While user guesses is not 0, this loop will iterate
    while user_guesses > 0:

        # Ask user for a guess
        print("            ", "-You have", user_guesses, "attempts left-")
        print(" ")
        user_guess = int(input("Guess the number: "))
        print(" ")

        # Decrement the user_guesses with 1 each iteration of the loop
        user_guesses = user_guesses - 1

        # This is self explaining:
        if numer_to_guess < user_guess:
            print("        ", "The number is LESS then your guess")
        elif numer_to_guess > user_guess:
            print("       ", "The number is GREATER then your guess")

        # If guess is not greater or less then the number_to_guess it means the user guessed correct
        # Ask for a retry
        else:
            print("Congratulations!! You Guessed it")
            retry()

    # When the user has 0 guesses left and has not guessed right, print the display the number_to_guess to the user and call Retry() function
    if user_guesses == 0 and user_guess != numer_to_guess:
        print("The number is: ", numer_to_guess)
        retry()


# Retry function is responsible for calling the Game() or not calling the Game() based on the user input:
# --> 1. Ask user to retry and store the users awnser in a variable called "choice"
#    --> 2. Check if choice is equal to "yes
#       --> 3. if yes --> Call Game() function
#       --> 4. if no --> Call Build in Quit() function (just breaks out of the code)
#       --> 5. if choice is not "yes" or "no", tell user to enter eiher (yes or no) and call Retry() again

def retry():
    # aks user to try again
    choice = input("Do you want to try again?: (no or yes): ")

    # This is self explaining:
    if choice.lower() == "yes":
        print("Starting game...")
        Game()
    elif choice.lower() == "no":
        print("Quiting game...")
        quit()
    else:
        print("Please enter a valid awnser (yes or no): ")
        retry()


# Simple function call to start the game the first time
Game()
