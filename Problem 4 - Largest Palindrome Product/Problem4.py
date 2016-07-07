# coding=utf-8
"""
PROBLEM 4:
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

APPROACH:
    (1) Iterate through two ranges, each from 100-999. Compute the product of each pair.

    (2) Determine if each product is a palindrome. If not, continue to the next product pair

    (3) If the product is a palindrome, compare it to the currently stored highest palindrome. If it's greater than,
        store the value (e.g., overwrite) in the highest palindrome variable. If not, continue to the next product pair

    (4) Return the highest palindrome variable
"""
import time

def is_palindrome(s):
    '''
    Evaluates whether a string is a palindrome
    :param s: A string
    :return: True (is palindrome) or False (is not palindrome)
    '''

    s = str(s)
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start = start + 1
        end = end - 1
    return True

def main():

    ## Testing the is_palindrome function
    # testlist = [9009, 10101, 3456, 34567, 'moon', 'noob', 'noon']
    # for item in testlist:
    #     print 'Testing palindrome: {0} is {1}'.format(item, is_palindrome(item))
    #

    range_start = 100
    range_stop = 999

    max_palindrome = 0

    for i in range(range_start, range_stop+1):
        for j in range(range_start, range_stop+1):
            product = i * j
            test = is_palindrome(product)
            if test:
                print 'Product of {0}*{1} = {2} [{3}\t{4}]'.format(i, j, product, test, max_palindrome)

                if product > max_palindrome:
                    max_palindrome = product
        # time.sleep(1)


    print 'Process complete. Max Palindrome is {0}'.format(max_palindrome)

if __name__ == '__main__':
    main()
