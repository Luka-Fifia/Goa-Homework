#5)დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი და ლუწი.

num = int(input("Enter number: "))

if num % 2 == 0 and num >= 100:
    print("Your Number is Even and More than 100")
