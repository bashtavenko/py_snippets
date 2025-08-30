"""5.9 Enumerate all primes to n."""

import math


def generate_primes_bf(n):
    """Trial division."""
    result = []
    for x in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i==0:
                is_prime = False
                break
        if is_prime:
            result.append(x)

    return result


def generate_primes(n):
    primes = []
    # Initially [F, F, T, ... Tn]
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n):
        if is_prime[p]:
            primes.append(p)
            # Once we have a prime p, sieve(filter) its multiples
            # meaning if we have 2 then 4, 6 and 8 could not be primes
            # The trick is the step parameter of range
            # range(2, 10, 2) => 2, 4, 6, 8
            # range(3, 10, 3) => 3, 6, 9
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes
