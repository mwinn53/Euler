# coding=utf-8

"""
PROBLEM 5:
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

APPROACH:
    (1) Compute the prime factorization (pollard_rho) of all numbers from 2..n (e.g., 2..20), storing the highest
        frequency of factors in a dictionary (key:value = factor:highest_frequency).

    (2) The smallest positive number that is evenly divisible by all of the numbers is the product of all of
        highest-frequency prime factorizations. Therefore, for each element in the dictionary factor^highest_frequency.

    Source: https://www.math.toronto.edu/mathnet/questionCorner/lcm.html
        1..10
        2 = 2, 3 = 3, 4 = 2*2 , 5 = 5, 6 = 3*2 , 7 = 7, 8 = 2 * 2 * 2 , 9 = 3 * 3, and 10 = 5 * 2
        (2) (2 2) (2) (2 2 2) (2)   = 2^3 = 8
        (3) (3) (3 3)               = 3^2 = 9
        (5) (5)                     = 5^1 = 5
        (7)                         = 7^1 = 7
                                    8 * 9 * 5 * 7 = 2,520
"""
import pollard_rho

def main():

    mostFactors = {}
    maxRange = 20       # Hard coded for testing; should be passed as a parameter

    for i in range(2, maxRange):
        list = pollard_rho.pollard_rho(i)       # pollard_rho returns the prime factorization of i as a list
                                                #   where each element in the list is a factor
                                                #   (i.e., [2 2 3] = 2^2 * 3^1)
        
        freq = {}                               # convert the list into a dictionary key (base): value (power)
        for item in list:                       #   (i.e. {2: 2, 3: 1} = 2^2 * 3^1)
            freq[item] = freq.get(item, 0) + 1

        for item in freq:                       # add the most frequently occurring prime factorization of i
            if (item in mostFactors):           #   to a master dictionary of highest-frequency prime factorizations
                if (freq[item] > mostFactors[item]):
                    mostFactors[item] = freq[item]
            else:
                mostFactors[item] = freq[item]

    # To calculate the product of all of the highest-frequency prime factorizations
    #   multiply (and store) each key^value to the running product. Intermediate steps are printed for debuggin.
    product = 1
    for item in mostFactors:
        product = product * (int(item) ** int(mostFactors[item]))
        print '{0}^{1}={2}'.format(int(item), int(mostFactors[item]), product)

    print 'product: {0}'.format(product)

if __name__ == '__main__':
    main()
