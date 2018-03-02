def is_armstrong(number):
    digits = [int(char) for char in str(number)]
    count = len(digits)
    powers = [digit**count for digit in digits]
    return number == sum(powers)

