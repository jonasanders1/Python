
while True:
    print()
    print("*** Welcome to the temerature calculator ***")
    print("______ PRESS 3 TO STOP THE PROGRAM ______")

    user_choise = int(input(
        "Enter 1 to convert from Celsius to Fahrenheit\nEnter 2 to convert from Fahrenheit to Celsius: "))
    print()

    def convertToFahrenheit(celsius):
        F = (9/5) * celsius + 32
        print(F)

    def converToCelsius(fahrenheit):
        C = (5/9)*(fahrenheit-32)
        print(C)

    if user_choise == 1:
        print("You chose Celsius to Fahrenheit")
        temp = int(input("Enter the Celcius temperature: "))
        convertToFahrenheit(temp)
    elif user_choise == 2:
        print("You chose Fahrenheit to Celsius")
        temp = int(input("Enter the fahrenheit temperature: "))
        converToCelsius(temp)
    elif user_choise == 3:
        print("Stopping program...")
        quit()
