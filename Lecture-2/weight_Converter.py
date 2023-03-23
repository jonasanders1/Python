def handle_input(a, type):
    type = input("(L)bs or (K)g: ")
    if type.lower() == "l":
        sum = a * 0.45
        print(f"You are {sum} kilo(s)")
    elif type.lower() == "k":
        sum = a * 2.2
        print(f"You are {sum} pounds")


def main():
    a = int(input("Enter your weight: "))
    handle_input(a, type)


main()
