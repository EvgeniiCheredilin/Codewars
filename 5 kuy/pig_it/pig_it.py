def pig_it(text):
    """Takes string
    Returns pig latina string."""
    words = text.split(' ')
    new_words = []
    for word in words:
        if word in ',.!?':
            new_words.append(word)
        else:
            new_words.append(word[1:] + word[0] + 'ay')
    return ' '.join(new_words)
