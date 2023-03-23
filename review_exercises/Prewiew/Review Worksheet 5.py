month = input("Enter the name of the month: ")
day = int(input("Enter the day number: "))

if day < 1 or day > 31:
   print("Invalid day!")

else:
    if month == "January" or month == "February":
        season = "Winter"
        
    elif month == "March":
        if day < 20:
            season = "Winter"
        else:
            season = "Spring"
            
    elif month == "April" or month == "May":
        season = "Spring"
        
    elif month == "June":
        if day < 21:
            season = "Spring"
        else:
            season = "Summer"
            
    elif month == "July" or month == "August":
        season = "Summer"
        
    elif month == "September":
        if day < 22:
            season = "Summer"
        else:
            season = "Fall"
    
    elif month == "October" or month == "November":
        season = "Fall"
        
    elif month == "December":
        if day < 21:
            season = "Fall"
        else:
            season = "Winter"
    else:
        month = ""
    
    
    if month != "":   
        print(month, day, "is in", season)
    else:
        print("Invalid month name.")