def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    elif human_years >= 3:
        cat_years = 24 + (4 * (human_years -2))
        dog_years = 24 + (5 * (human_years -2))
        return [human_years, cat_years, dog_years]