def captianjack():
    gold_coin = int(input("Enter Amount of Gold Coins That You Have: "))
    choice = int(input("Ship Prices: 1) 150 Gold 2) 200 Gold 3) 250 Gold 4) 300 Gold 5) 350 Gold (Enter 1-5): "))
    if choice == 1 and gold_coin < 150 or choice == 2 and gold_coin < 200 or choice == 3 and gold_coin < 250 or choice == 4 and gold_coin < 300 or choice == 5 and gold_coin < 350:
        return "The crew mutinied"
    return "You have successfully purchased a ship"

print(captianjack())