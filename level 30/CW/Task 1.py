def high_and_low(num):
    nums = num.split()
    return "{0} {1}".format(min(nums) , max(nums))

print(high_and_low("1 2 3 4 5"))

# second way

def higher_lower(str):
    res = str.split(" ")
    arr = []
    for element in res:
            arr.append(int(element))
    return f"{max(arr)} {min(arr)}"

print(higher_lower("1 2 3 4 5"))


a = [1, 2, 3]
print(len(a))