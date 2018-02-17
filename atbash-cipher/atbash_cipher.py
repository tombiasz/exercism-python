import string


def partition(string, size=5):
    return [string[i:i+size] for i in range(0, len(string), size)]


def encode(plaintext):
    plaintext = plaintext.lower()
    chars_to_delete = ''.join([string.punctuation, string.whitespace])
    translation = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[::-1],
        chars_to_delete
    )
    ciphertext = plaintext.translate(translation)
    return ' '.join(partition(ciphertext))


def decode(ciphertext):
    chars_to_delete = string.whitespace
    translation = str.maketrans(
        string.ascii_lowercase[::-1],
        string.ascii_lowercase,
        chars_to_delete
    )
    return ciphertext.translate(translation)
