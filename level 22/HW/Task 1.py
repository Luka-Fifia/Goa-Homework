'''
დავალება 1
შექმენით სია list_of_names, რომელშიც ინახება სახელები. დაწერეთ კოდი, რომელიც ითვლის, რამდენჯერ მეორდება კონკრეტული სახელი (მაგალითად, "დავით") სიაში.

'''

arr = ["Nika", "Giorgi", "Luka", "Gela", "Vano", "Luka", "Vaso", "Luka"]
count = 0

for i in range(len(arr)):
    if arr[i] == "Luka":
        count += 1

print(count)