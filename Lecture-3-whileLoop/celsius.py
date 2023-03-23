

#  C * (9/5) + 32 = F

celsius = 0

print("Celsius | Fahrenheit")
print("--------+-----------")
while celsius < 100:
    celsius += 10
    fahrenheit = celsius * (9/5) + 32
    print(celsius, end='     |      ')
    print(fahrenheit)
