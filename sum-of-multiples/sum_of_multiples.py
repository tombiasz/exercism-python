def is_divisible(value, dividers):
    return any(map(lambda divider: value % divider == 0, dividers))


def sum_of_multiples(n, dividers):
    return sum([v for v in range(n) if is_divisible(v, dividers)])
