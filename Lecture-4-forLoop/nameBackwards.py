name = input("Enter a word: ")

for i in range(len(name) - 1, -1, -1):
    print(name[i], end="")
