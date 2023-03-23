"""
##
# This program prints the average of salary values that are terminated with a 
sentinel.
#
# Initialize variables to maintain the running total and count.
total = 0.0
count = 0
# Initialize salary to any non-sentinel value.
salary = 0.0
# Process data until the sentinel is entered.
while salary >= 0.0:
    salary = float(input("Enter a salary or -1 to finish: "))
    if salary >= 0.0:
        total = total + salary
        count = count + 1
# Compute and print the average salary.
if count > 0:
    average = total / count
    print("Average salary is", average)
else:
    print("No data was entered.")
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Welcome {first_name} {last_name}")

total = 0.0
count = 0
# Initialize salary to any non-sentinel value.
score = 0.0
# Process data until the sentinel is entered.

score = float(input("Enter a score or -1 to finish: "))

while score >= 0.0:
    total = total + score
    count = count + 1
    score = float(input("Enter a score or -1 to finish: "))

# Compute and print the average score.
if count > 0:
    average = total / count
    print("Average score is", average)
else:
    print("No data was entered.")
