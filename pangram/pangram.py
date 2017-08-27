import string


def is_pangram(input):
    input = input.lower()
    for char in string.lowercase:
        if char not in input:
            return False
    return True
