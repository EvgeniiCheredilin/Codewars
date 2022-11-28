def digital_root(n):
    """Takes number
    Returns digit (the recursive sum of all the digits in a number)"""
    sum_of_digits = n
    while len(str(n)) > 1:
        sum_of_digits = 0
        for i in str(n):
            sum_of_digits += int(i)
        n = sum_of_digits
    return sum_of_digits
