def decode(string):
    if len(string) == 0:
        return ''

    mult = ''
    output = ''

    for c in string:
        if c.isdigit():
            mult += c
        else:
            if mult != '':
                mult = int(mult)
                output += mult * c
                mult = ''
            else:
                output += c
    return output


def encode(string):
    if len(string) == 0:
        return ''

    char_count = 1
    last_char = string[0]
    output = []
    for c in string[1:]:
        if c != last_char:
            if char_count != 1:
                output.append(str(char_count))
            output.append(last_char)
            last_char = c
            char_count = 1
        else:
            char_count += 1

    if char_count != 1:
        output.append(str(char_count))
    output.append(last_char)

    return ''.join(output)
