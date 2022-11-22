def find_uniq(arr):
    """Takes array of numbers
    Returns unique number."""
    s = set(arr)
    for n in s:
        if arr.count(n) == 1:
            return n
