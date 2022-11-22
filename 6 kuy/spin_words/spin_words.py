def spin_words(sentence):
    """Takes sentence string
    Returns sentence string with all five or more letter words reversed."""
    my_sentence = sentence
    my_list = my_sentence.split()
    for i in my_list:
        if len(i) > 4:
            my_sentence = my_sentence.replace(i, i[::-1])
    return my_sentence
