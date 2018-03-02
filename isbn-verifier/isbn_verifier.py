import re

ISBN_CHARS_TO_INTETGER = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'X': 10,
}

def clean_isbn(isbn):
    return isbn.replace('-', '')

def validate_format(isbn):
    return bool(re.match('^\d{9}[\dX]$', isbn))

def calculate_checksum(isbn):
    checksum = 0
    for index, char in zip(range(10,0,-1), isbn):
        checksum += index * ISBN_CHARS_TO_INTETGER[char]
    return checksum

def verify_checksum(checksum):
    return checksum % 11 == 0

def verify(isbn):
    isbn = clean_isbn(isbn)
    if not validate_format(isbn):
        return False
    checksum = calculate_checksum(isbn)
    return verify_checksum(checksum)
