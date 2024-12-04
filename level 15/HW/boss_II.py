#||) შექმენით სია სადაც მოათავსებთ, 10 რაიმე ციფრს for loop ის გამოყენებით გავიგოთ ყველაზე პატარა ციფრი სიაი: [9,5,94,711,52,96,71,8]


num_list = [12, 17, 94, 3, 45, 76, 98, 976, 94, 20]

random_item = num_list[0]

for i in num_list:
    if i < random_item:
        random_item = i
    

print("Smallest Number from list is: ", random_item)