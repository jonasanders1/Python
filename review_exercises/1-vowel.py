# 1. get user letter
# 2. loop

vowels = "aeiouAEIOU"

while True:
    letter = str(input("Enter a letter (stop to stop program):"))
    if letter.lower() in vowels:
        print("It`s a Vowel")
    elif letter.lower() == "y":
        print("Sometimes it's a vowel ... Sometimes it's a constant.")
    elif letter.lower() == "stop":
        break
    else:
        print("It`s a constant")
