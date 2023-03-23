from enum import Enum


class Grade(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"


def check_grade(score):
    if score < 0 or score > 100:
        print("Invalid Input. The score must be between 0 and 100.")
    elif score >= 90:
        return Grade.A
    elif score >= 80:
        return Grade.B
    elif score >= 70:
        return Grade.C
    elif score >= 60:
        return Grade.D
    else:
        return Grade.F


score = int(input("Enter your Score: "))
grade = check_grade(score)
if grade:
    print("Your Grade is : ", grade.value)
