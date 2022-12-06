import re


def format_duration(seconds):
    """Takes a non-negative integer
    Returns string"""
    if seconds == 0:
        return 'now'
    names = [' second', ' minute', ' hour', ' day', ' year']
    durations = [1, 60, 60 * 60, 60 * 60 * 24, 60 * 60 * 24 * 365]
    result_list = []
    result_string = ''
    for i in range(len(durations)):
        if i == len(durations) - 1:
            result_list.append(seconds // durations[i])
        else:
            result_list.append(seconds % durations[i + 1] // durations[i])
    for i in range(len(result_list)):
        if result_list[i] != 0:
            result_string = ' ' + str(result_list[i]) + names[i] + ('s' if result_list[i] > 1 else '') + result_string
    result_list = re.findall(r'\d\d?\d? \w*', result_string)
    if len(result_list) == 1:
        return ''.join(result_list)
    elif len(result_list) == 2:
        return ' and '.join(result_list)
    else:
        return ', '.join(result_list[:-1]) + ' and ' + result_list[-1]
