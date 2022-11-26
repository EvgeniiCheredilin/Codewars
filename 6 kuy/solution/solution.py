def solution(n):
    """Takes number
    Returns the sum of all the multiples of 3 or 5 below the number passed in"""
    s = 0
    for i in range(n):
        if i % 5 == 0 or i % 3 == 0:
            s = s + i
    return s
