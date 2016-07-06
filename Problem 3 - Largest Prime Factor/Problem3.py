"""
Problem 3
    # The prime factors of 13195 are 5, 7, 13 and 29.
    # What is the largest prime factor of the number 600851475143 (e.g. 10^11)?

APPROACH: Build a list of primes up to sqrt(n) using Sieve of Eratosthenes (SieveOfEratosthenes)
          Use trial division from largest prime in Sieve
"""

import argparse, math
import prime_sieves

def main():
    parser = argparse.ArgumentParser(description="A program to generate prime numbers with various methods",)
    parser.add_argument("number", help="Maximum number of which to generate prime numbers.")
    args = parser.parse_args()

    # THEOREM: If n is a composite integer, then n has a prime divisor less than or equal to the square root of n
    #           https://en.wikipedia.org/wiki/Prime_number
    number = int(args.number)
    maxfactors = math.ceil(math.sqrt(int(args.number)))

    s = list(prime_sieves.SieveOfEratosthenes3(maxfactors))

    print 'Original number:\t{0}'.format(number)
    print 'Sieve based on sqrt({0}):\t{1}'.format(number, maxfactors)
    print 'Number of primes in s:\t{0}'.format(len(s))
    # print s
    print '----------------------------------------------------------------------'
    print 'Prime factors of {0}'.format(number)
    for item in reversed(s):
        test = number % item
        if test == 0:
            print '{0}\t{1}'.format(item, test)
    print '----------------------------------------------------------------------\n'



if __name__ == '__main__':
    main()
