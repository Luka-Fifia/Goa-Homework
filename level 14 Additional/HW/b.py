num1 = int(input("Enter first number: "))
num2 = int(input("Enter sexond number: "))
for i in range(num1,num2):
    if i % 2 == 0 and i % 3 == 0:
        print("2-ის და 3-ის ჯერადია ერთდროულად: ", i)
    else:
        print("2-ის და 3-ის ჯერადი არ არის: ", i)