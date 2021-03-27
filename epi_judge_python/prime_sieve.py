from typing import List

from test_framework import generic_test
import math

PRIMES = set([2])
COMPOSITES = set()

# Initial try
#def is_prime(n: int) -> bool:
#    if n in PRIMES:
#        return True
#    elif n in COMPOSITES:
#        return False
#
#    for i in range(3, math.floor(math.sqrt(n)), 2):
#        if n % i == 0:
#            COMPOSITES.add(n)
#            return False
#
#    #for p in PRIMES:
#    #    if n % p == 0:
#    #        COMPOSITES.add(n)
#    #        return False
#        
#    PRIMES.add(n)
#
#
#    return True



# Given n, return all primes up to and including n.
def _generate_primes(n: int) -> List[int]:

    primes = []
    if n >= 2:
        primes.append(2)

    for i in range(3, n+1, 2):
        if is_prime(i):
            primes.append(i)

            # pregenerate prime multiples
            for j in range(3, 100, 2):
                mult = i*j
                COMPOSITES.add(mult)

    return primes


# Dumb solution, O(n²)
def __generate_primes(n: int) -> List[int]:
    if n < 2: return []
    if n == 2: return [2]

    is_prime = [True]*(n+1)
    primes = [2]

    is_prime[0], is_prime[1] = False, False

    for i in range(3, n+1):
        for j in range(2, math.ceil(math.sqrt(i))+1):
            if i % j == 0:
                is_prime[i] = False
                break

        if is_prime[i]:
            primes.append(i)

    return primes


# Improved runtime given in book
def generate_primes(n: int) -> List[int]:
    # Added this bit to avoid an edge case
    if n < 2:
        return []


    size = math.floor(0.5 * (n-3)) + 1
    primes = [2]
    is_prime = [True]*n

    for i in range(size):
        if is_prime[i]:
            p = i*2 + 3
            primes.append(p)

            j = (i*i*2) + 6*i + 3
            while j < size:
                is_prime[j] = False
                j += p

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
