while True:
    print("Calculate numbers: ")
    a = int(input("Enter a number e = exit: "))
    b = int(input("Enter a number e = exit: "))
    operator = input("Enter operator type ( + - / or * ): ")

    def add(a, b):
        sum = a + b
        print(f"The sum is: {sum}")

    def sub(a, b):
        sum = a - b
        print(f"The sum is: {sum}")

    def mul(a, b):
        sum = a * b
        print(f"The sum is: {sum}")

    def div(a, b):
        if b > 0:
            sum = a / b
            print(f"The sum is: {sum}")
        else:
            print("Cant divide with 0")

    if operator == "+":
        add(a, b)
    elif operator == "-":
        sub(a, b)
    elif operator == "*":
        mul(a, b)

    elif operator == "/":
        div(a, b)
    else:
        print("invalid")
