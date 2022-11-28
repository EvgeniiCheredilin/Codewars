def split_string(s):
    """Takes string
    Returns list of pairs of two characters
    If the number of characters in the string is odd, then the last character will be paired with underscore"""
    result = []
    for i in range(0, len(s), 2):
        if i == len(s) - 1:
            result.append(s[i] + '_')
        else:
            result.append(s[i] + s[i + 1])
    return result
