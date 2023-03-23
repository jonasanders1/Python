

user_number = int(input("Enter a number of sides (between 3-10): "))


if user_number == 3:
    shape_name = "Triangle"
elif user_number == 4:
    shape_name = "Square"
elif user_number == 5:
    shape_name = "Pentagon"
elif user_number == 6:
    shape_name = "Hexagon"
elif user_number == 7:
    shape_name = "Heptagon"
elif user_number == 8:
    shape_name = "Octagon"
elif user_number == 9:
    shape_name = "Nonagon"
elif user_number == 10:
    shape_name = "Decagon"
else:
    print("Enter a number between 3-10")
    exit()

print(f"The shape with {user_number} sides is called {shape_name}.")
