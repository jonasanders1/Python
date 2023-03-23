import random

# Task 6
"""
Write a program that generates a sequence of 20 random values between 0 and 99, stores them in a list, 
prints the sequence, sorts it, and prints the sorted sequence. Use the sort method.
"""


def sortRandomNumbers():
    my_list = []
    for i in range(20):
        randomNumber = random.randint(0, 99)
        my_list.append(randomNumber)
    print(my_list)

    print(sorted(my_list))


sortRandomNumbers()
