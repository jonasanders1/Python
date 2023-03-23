"""
Write a program using a function called multiple that determines for a pair of integers whether the second 
integer is a multiple of the first. The function should take 2 integer arguments and return appropriate values 
if the second one is a multiple of the first or not. 
"""


def multiple(num1, num2):
    if num1 % num2 == 0:
        return f" {num2} is a multiple of {num1}"
    else:
        return f" {num2} is not a multiple of {num1}"


print(multiple(36, 6))
