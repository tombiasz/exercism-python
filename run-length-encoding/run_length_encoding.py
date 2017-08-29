def decode(string):
    if len(string) == 0:
        return ''

    mult = 0
    output = ''
    for char in string:
        if char.isdigit():
            mult = mult * 10 + int(char)
        else:
            if mult != 0:
                output += mult * char
                mult = 0
            else:
                output += char
    return output


def encode(string):
    if len(string) == 0:
        return ''

    chars_seen = []
    chars_count = []
    idx = 0
    chars_seen.insert(idx, string[0])
    chars_count.insert(idx, 1)
    for char in string[1:]:
        if chars_seen[idx] == char:
            chars_count[idx] += 1
        else:
            idx += 1
            chars_seen.insert(idx, char)
            chars_count.insert(idx, 1)

    output = []
    for count, char in zip(chars_count, chars_seen):
        if count != 1:
            output.append(str(count))
        output.append(char)

    return ''.join(output)
