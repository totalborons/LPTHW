def break_words(sentence):
    words = sentence.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    word = words.pop(0)
    print(word)


def print_last_word(words):
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    words = break_words(sentence)
    # sort on the basis of ASCII and with regard for the uppercase and lowercase.. hence lowercase after uppercase
    return sort_words(words)


def print_first_and_last_word(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_word_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
