# et ord
name = input("Enter a word: ")

# en variabel som forteller hvor mange bokstaver som er i ordet
i = len(name)

# så lenge lengden på ordet er større enn 0
while i > 0:
    # print bokstaven med index i]
    print(name[i], end=' ')
    i = i - 1
