# Task 7
"""
Write a function def same_list (a, b) that checks whether two lists have the same elements in some order, 
ignoring duplicates. For example, the two lists  
"""

from collections import Counter

list_a = [1, 2, 3]
list_b = [1, 3, 2]


def same_List(a, b):
    return Counter(a) == Counter(b)


if same_List(list_a, list_b):
    print("The two lists are identical")
else:
    print("The two lists are not identical")
