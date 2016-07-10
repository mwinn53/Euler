"""
    Primality Test
    --------------
    Implementation of a Primality Test that uses a cache to improve
    performance.

"""
from math import sqrt

CACHE_LIMIT = 10 ** 6
primes_cache_list = []
primes_cache_bool = []

def eratosthenes(end, start=2, return_boolean=False):
    """
    Finds all primes < `end`.

    :param end: An integer. The upper limit of the range to look for primes.
    :param start: An integer. The start of the range to look for primes.
    :param return_boolean: A boolean. Represents the type of return type.
    :rtype: Depending on `return_boolean` either returns boolean and primes or
            just the primes.
    """
    primes = []
    if end < start or end < 2:
        return []
    is_prime = [True for i in range(end + 1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, end + 1):
        if not is_prime[i]:
            continue
        if start <= i <= end:
            primes.append(i)
        j = i * i
        while j <= end:
            is_prime[j] = False
            j += i
    if return_boolean:
        return primes, is_prime
    return primes

def is_prime(number, cache=True):
    """
    Takes `number` and determines if it is prime.

    :param number: The integer to be tested for primality.
    :param cache: A boolean to determine if a cache should be used to
                  improve performance.
    :rtype: A boolean that signifies if `number` is prime.
    """
    if number < 2:
        return False
    global primes_cache_list, primes_cache_bool
    if cache and len(primes_cache_list) == 0:
        primes_cache_list, primes_cache_bool = eratosthenes(
            CACHE_LIMIT, return_boolean=True
        )
        for prime in primes_cache_list:
            primes_cache_bool[prime] = True
    if number < len(primes_cache_bool):
        return primes_cache_bool[number]

    sqrt_number = sqrt(number)
    for prime in primes_cache_list:
        if prime > sqrt_number:
            return True
        if number % prime == 0:
            return False

    to_check = 2
    if len(primes_cache_list) > 0:
        to_check = primes_cache_list[-1] + 1
    while to_check <= sqrt_number:
        if number % to_check == 0:
            return False
        to_check += 1
    return True
