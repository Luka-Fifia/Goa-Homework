def password(st):
    has_upper = False
    has_lower = False
    has_digit = False

    if len(st) < 8:
        return False
    
    for char in st:
        if "A" <= char <="Z":
            has_upper = True
        elif "a" <= char <= "z":
            has_lower = True
        elif "0" <= char <= "9":
            has_digit = True

    return has_upper and has_lower and has_digit 

# print(password("asdasdAasd12"))          testing