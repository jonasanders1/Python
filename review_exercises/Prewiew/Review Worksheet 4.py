side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 < 1 or side2 < 1 or side3 < 1:
    print("Invalid side lengths.")

else:
    if side1 == side2 and side2 == side3:
        triangle_type = "Equilateral"
    
    elif side1 == side2 or side2 == side3 or side3 == side1:
        triangle_type == "Isosceles"
    
    else:
        triangle_type = "Scalene"
        
    print("Thst's a", triangle_type, "triangle.")