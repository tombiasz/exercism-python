from collections import defaultdict


def word_count(phrase):
    phrase = ''.join([c if c.isalnum() else ' ' for c in phrase.lower()])

    word_count = defaultdict(int)
    for word in phrase.split():
        word_count[word] += 1
    return word_count
