num_sides = int(input("Enter the number of sides: "))

if num_sides == 3:
    name = "Triangle"
    
elif num_sides == 4:
    name = "Quadrilateral"

elif num_sides == 5:
    name = "Pentagon"
    
elif num_sides == 6:
    name = "Hexagon"
    
elif num_sides == 7:
    name = "Heptagon"
    
elif num_sides == 8:
    name = "Octagon"
    
elif num_sides == 9:
    name = "Nonagon"
    
elif num_sides == 10:
    name = "Decagon"
    
else:
    name = ""
    
if name == "":
    print("That number of sides is not supported by this program.")
else:
    print("That's a", name)