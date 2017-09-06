import math


def sieve(n):
    A = [True] * n
    A[0] = False  # 1 is not prime

    for i in xrange(2, int(math.sqrt(n))+1):
        if A[i-1]:
            for j in xrange(i**2, n+1, i):
                A[j-1] = False

    return [idx + 1 for idx, value in enumerate(A) if value]
