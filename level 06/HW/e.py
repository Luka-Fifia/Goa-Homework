number = int(input("enter a two-digit number: " ))
dozen = ( number // 10 )
unit = (number % 10)

print(dozen + unit)