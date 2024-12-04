"""
დავალება 5
შექმენით სია, იპოვეთ კონკრეტული ელემენტის რაოდენობა 
count მეთოდის გამოყენებით და ამოიღეთ ეს ელემენტი სიიდან remove მეთოდით. 
დაბეჭდეთ ელემენტის რაოდენობა და განახლებული სია.

"""

arr = ["Nika", "Giorgi", "Luka", "Gela", "Vano", "Luka", "Vaso", "Luka"]

print("There is/are",arr.count("Luka"), "Luka(s)")
while "Luka" in arr:
    arr.remove("Luka")

print(arr)