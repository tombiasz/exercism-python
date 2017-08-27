def is_isogram(string):
    char_seen = set()
    for char in string.lower():
        if char.isalpha():
            if char in char_seen:
                return False
            char_seen.add(char)
    return True
