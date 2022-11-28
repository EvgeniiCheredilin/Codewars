def minimum(arr):
    """Takes list of integers
    Returns the lowest number in the list"""
    arr.sort()
    return arr[0]


def maximum(arr):
    """Takes list of integers
    Returns the largest number in the list"""
    arr.sort()
    return arr[-1]


# A simpler and faster solution, but here only knowledge of the built-in mechanisms
def minimum2(arr):
    """Takes list of integers
    Returns the lowest number in the list"""
    return min(arr)


def maximum2(arr):
    """Takes list of integers
    Returns the largest number in the list"""
    return max(arr)
