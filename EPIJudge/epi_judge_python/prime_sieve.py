import math
from typing import List

from test_framework import generic_test

## brute force, very slow solution.
## checks 1, sqrt(2), sqrt(3)... sqrt(n)
## if it was 1,...,n, then run time is n(n+1)/2
## but since it's all square root... then maybe n(sqrt(n) + 1 )/2??
## definitely O(n * sqrt(n))
def brute_force(n: int) -> List[int]:
    primes = []
    for i in range(2, n+1):
        prime = True
        for divisors in range(2, int(math.sqrt(i)) + 1):
            if i % divisors == 0:
                prime = False
                break
        # print(f'number: {i} prime?: {prime}')
        if prime:
            primes.append(i)
    return primes

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    ## generate boolean array, O(n)
    primes = []
    # possible_prime = [True for x in range(0, n+1)]
    ## more correct EPI version
    possible_prime = [False, False] + [True] * (n-1) 
    for i in range(2, n+1):
        if possible_prime[i]:
            primes.append(i)
            for j in range(i, n+1, i):
                possible_prime[j] = False
    return primes


if __name__ == '__main__':
    # print('brute force')
    # generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
    #                                    brute_force)
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes)
