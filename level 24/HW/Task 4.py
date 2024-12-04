a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = (input("Enter Operation: "))

if c == "+" :
    result = a + b
elif c == "-" :
    result = a - b
elif c == "*" :
    result = a * b
elif c == "/" :
    if b != 0:
        result = a / b
    else:
        result = "Error!!!: Division by zero"
    
    
print(result)



