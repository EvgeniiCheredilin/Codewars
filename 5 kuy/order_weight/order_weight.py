def order_weight(strng):
    """Takes string of weights (positive numbers and whitespaces)
    Returns string of weights ordered by numbers weights (sum of its digits)"""
    if strng == '':
        return ''
    lst = strng.split()
    lst_sums = []
    for n in lst:
        sum1 = 0
        for i in n:
            sum1 += int(i)
        lst_sums.append(sum1)

    sorted_sums = lst_sums.copy()
    sorted_sums.sort()
    tek = sorted_sums[0]
    short_list = []
    ret_list = []
    index = -1
    for i in sorted_sums:
        if tek == i:
            index = lst_sums.index(i, index + 1)
            short_list.append(lst[index])
        else:
            tek = i
            index = -1
            short_list.sort()
            ret_list.extend(short_list)
            short_list.clear()
            index = lst_sums.index(i, index + 1)
            short_list.append(lst[index])

    short_list.sort()
    ret_list.extend(short_list)
    return ' '.join(ret_list)
