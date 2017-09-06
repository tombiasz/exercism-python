import string


def partition(string, size=5):
    return [string[i:i+size] for i in xrange(0, len(string), size)]


def encode(plaintext):
    plaintext = plaintext.lower()
    translation = string.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[::-1]
    )
    deletechars = ''.join([string.punctuation, string.whitespace])
    ciphertext = plaintext.translate(translation, deletechars)
    return ' '.join(partition(ciphertext))


def decode(ciphertext):
    translation = string.maketrans(
        string.ascii_lowercase[::-1],
        string.ascii_lowercase
    )
    deletechars = string.whitespace
    return ciphertext.translate(translation, deletechars)
