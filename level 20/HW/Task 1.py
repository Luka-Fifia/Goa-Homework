'''
დავალება 1:
შექმენით სია სადაც ინაქბა სხვადასხვა ასეობი და მხოლოდ ხმოვნები დაითვალეთ

'''

arr = ["a", "s", "b", "c", "r", "o", "e", "e", "m", "n", "f", "c", "r", "a", "t" "h"]

count = 0

for i in arr:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1

print("There is/are", count, "vowel(s)")