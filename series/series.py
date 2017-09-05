def slices(string, size):
    if not 0 < size <= len(string):
        raise ValueError()

    return [
        map(int, list(string[index:size + index]))
        for index in xrange(len(string) - size + 1)
    ]
