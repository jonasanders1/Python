user_string = input("Enter a string: ")


def only_upper(n):
    upper_chars = ""
    # for hver bokstav i setningen
    for char in n:
        # sjekk om bokstanven er stor
        if char.isupper():
            # hvis bokstaven er stor putt den store bokstaven inn i en variabel
            upper_chars += char
    print(upper_chars)


only_upper(user_string)
