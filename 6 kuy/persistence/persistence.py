def persistence(n):
    """Takes positive number
    Returns number of times you must multiply the digits in n until you reach a single digit."""
    p = 0
    while len(str(n)) > 1:
        my_sum = 1
        for char in str(n):
            my_sum *= int(char)
        n = my_sum
        p += 1
    return p
