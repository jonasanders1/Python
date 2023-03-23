month = input("Enter the name of a month: ")

# .capitalize() can be used to capitalize the string

# start by assuming that the number of days is 31. Then update the number of days if necessary
if month == "January" or month == "March" or month == "May" or month == "July" \
    or month == "August" or month == "October" or month == "December":
        days = 31

elif month == "April" or month == "June" or month == "September" or month == "November":
    days = 30

elif month == "February":
    days = "28 or 29"
    
else:
    days = 0
    
if days == 0:
    print("Invalid month name.")
else:
    print(month, "has", days, "days in it.")