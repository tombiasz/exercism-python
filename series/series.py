def slices(string, size):
    if not 0 < size <= len(string):
        raise ValueError()

    return [
        list(map(int, string[index:size + index]))
        for index in range(len(string) - size + 1)
    ]
