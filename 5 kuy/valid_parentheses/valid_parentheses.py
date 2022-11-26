def valid_parentheses(str1):
    """Takes string of parentheses
    Returns true if the order of the parentheses in the string is valid, and false if it's invalid"""
    balance = 0
    for c in str1:
        if balance < 0:
            return False
        if c == "(":
            balance += 1
        if c == ")":
            balance -= 1
    return balance == 0
