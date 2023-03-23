import random


# Taks 2
values = []


for i in range(10):  # 0 - 9
    # each iteration --> get a random number
    random_number = random.randint(1, 100)
    # each iteration --> add number to list
    values.append(random_number)

print("2. List with 10 random numbers:", values)


# Task 3

# A) Printing all elements of the list in a single row, separated by spaces
def formatList():
    print("3. a) All numbers on same line:")
    for item in values:
        print(item, end=' ')


# B) Computing the sum of all elements in the list.
def total():
    total = 0
    for item in values:
        total = total + item
    print()
    print("3 b) The total of all numbers in list: ", total)

# C Computing how many elements in the list are even numbers.


def evenNums():
    # for each item in list
    evenNumList = []
    for item in values:
        # check if the item module 2 is equal to 0 --> aka even number (no rest)
        if item % 2 == 0:
            # if so --> add them to the list
            # print(item)
            evenNumList.append(item)
    # print the lenght of the list where i stored all even numbers
    print("3 c) Total of even numbers in the list:", len(evenNumList))


# Task 4
"""
Consider the list generated in Exercise 2 (values) and separate the even and odd numbers into two different 
lists even_values, odd_values. 
"""


def seperateValues():
    evenList = []
    oddList = []

    for item in values:
        if item % 2 == 0:
            evenList.append(item)
        else:
            oddList.append(item)
    print("Task 4")
    print("Seperate list with all even numbers", evenList)
    print("Seperate list with all odd numbers", oddList)


# Task 5
"""
Consider the list generated in Exercise 2 (values) and remove the odd elements from the list.  
"""


def removeOddNumbers():
    for item in values:
        if item % 2 == 1:
            values.remove(item)
    print(values)


# formatList()
# total()
# evenNums()
# seperateValues()
# removeOddNumbers()
