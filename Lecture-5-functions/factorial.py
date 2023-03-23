"""
The factorial of a number is the product of all the integers from 1 to that number. For example, the factorial 
of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one, 
0! = 1. Write a function to find the factorial of a number passed to the function. 
"""


def calculate(number):
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


print("The factorial is:", calculate(6))
