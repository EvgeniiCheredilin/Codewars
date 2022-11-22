def disemvowel(string):
    """Takes string
    Returns string with all vowels removed."""
    newstr = ""
    for char in string:
        if char not in "aeiouAEIOU":
            newstr += char
    return newstr
