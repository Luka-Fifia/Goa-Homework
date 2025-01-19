def manual_difference(first_set, second_set):
    result = set()
    for char in first_set:
        if char not in second_set:
            result.add(char)
    return result

# set1 = {"banana", "apple", "mango"}       ⬇️
# set2 = {"apple", "banana"}                ➡️➡️     Testing function
#                                           ⬆️
# print(manual_difference(set1, set2))      ⬆️