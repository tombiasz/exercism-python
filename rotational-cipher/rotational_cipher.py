import string


def shift(string, amount):
    return string[amount:] + string[:amount]


def build_alphabet(rotate=0):
    return ''.join([
        shift(string.ascii_lowercase, rotate),
        shift(string.ascii_uppercase, rotate),
    ])


def rotate(plaintext, key):
    alphabet_in = build_alphabet()
    alphabet_out = build_alphabet(rotate=key)
    translation = string.maketrans(alphabet_in, alphabet_out)
    return plaintext.translate(translation)
