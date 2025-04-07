# First Way

def feast(beast, dish):
    beast_name = beast[0] + beast[-1]
    dish_name = dish[0] + dish[-1]
    return beast_name == dish_name

# Second Way

def feast(beast, dish):
    return beast.endswith(dish[-1]) and beast.startswith(dish[0])