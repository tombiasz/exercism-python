import re


def abbreviate(phrase):
    words = re.split(r'[\s-]', phrase)
    first_chars = [w[0].upper() for w in words]
    return ''.join(first_chars)
