def twice_as_old(dad_years_old, son_years_old):
    result = dad_years_old - 2 * son_years_old
    if result < 0:
        result = -result
    return result