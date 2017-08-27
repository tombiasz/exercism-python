def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError('DNA not equal')

    count = 0
    for n1, n2 in zip(dna1, dna2):
        if n1 != n2:
            count += 1
    return count
