"""
    Sieve of Eratosthenes
    ---------------------
    Is a simple, ancient algorithm for finding all prime numbers
    up to any given limit. It does so by iteratively marking as composite
    (i.e. not prime) the multiples of each prime, starting with the multiples
    of 2.

    The sieve of Eratosthenes is one of the most efficient ways
    to find all of the smaller primes (below 10 million or so).

    Time Complexity: O(n log log n)

    Pseudocode: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


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


# ---------------------------------------------------------------------------
# function: SieveOfEratosthenes()
#   description:    Calculate a series of prime numbers from 2 to N, using
#                       various implementations of the Sieve of Earatostheneses
#   input:  	    (int) N, the maximum number of primes
#   output:	        list of prime numbers from 2 to N
# ---------------------------------------------------------------------------
def SieveOfEratosthenes1(n):
    '''Returns a list of the prime numbers from 2..n'''

    # Naiive approach; fast, but uses alot of memory (runs out at N=10000000 e.g., 10^7)

    #		Variant 	ms		iter    	bytes  	elements
    #		------- 	--  		----   	-----   	--------
    #		Sieve1  	7.0		193393  800072  	100001
    #		n: 100000
    #		Number of primes in s:  9592

    #  (1) Stores 2..n in memory, then marks composites
    #  (2) Returns the 2..n list, filtered by those that are not marked as composite

    np1 = n + 1
    A = range(np1)  # initialize an list of of n+1 elements, with the index number as it's value
    #   (e.g., A[1]=1, A[2]=2, ...)
    sqrtn = int(round(n ** 0.5))

    A[1] = 0  # 1 in not a prime number, so set it to "false" and start with 2

    iterations = 0
    starttime = time.time() * 1000

    for i in range(2, sqrtn + 1):
        iterations += 1
        if A[i]:
            rng = len(range(i * i, np1, i))
            A[i * i:np1: i] = [0] * rng
            # List comprehension for setting all values of A from i^2 to np1, in incrememnts of i to [0] by
            #   merging the list of multiples of i from i^2 to np1 with a list of [0] that is the length of
            #   the same number of values
            #       [2,4,6,8,10...]
            #       [0,0,0,0,0 ...]
            # Equivalent to the pseudocode:
            #   for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n:
            #       A[j] := false

            # Don't be fooled; the list comprehension performs slightly better than a regular for loop
            iterations += rng

    endtime = time.time() * 1000

    print("Variant\tms\t\titer\tbytes\telements")
    print("-------\t--\t\t----\t-----\t--------")
    print 'Sieve1\t{0}\t\t{1}\t{2}\t{3}'.format(endtime - starttime, iterations, sys.getsizeof(A), len(A))

    return filter(None, A)


# ---[ VARIATION 2 ]---------------------------------------------------------
def SieveOfEratosthenes2(n):
    '''Returns a list of the prime numbers from 2..n'''

    # Uses less memory, but considerably slower. Becomes infeasible (time) after N=100000 (10^5)

    #		Variant	ms        iter    	bytes   	elements
    #		-------	--        ----    	-----   	--------
    #		Sieve2 	5973.0  266385	786704	9592
    #		n: 100000
    #		Number of primes in s:  9592

    # Uses a dictionary to maintain the list of primes (key) and multiples (value) and a generator
    #   to "yield" the primes as they are found. The sieve yields a prime if it is not found in the
    #   dictionary after incrementing all of the multiples of previously found prime numbers.

    #	A (up to j = 11):
    #  	2:    2, 4, 6, 8, 10, 12
    #  	3:    3, 6, 9, 12
    #   5:    5, 10, 15
    # 	7:    7, 14

    j, A = 2, {}

    iterations = 0
    starttime = time.time() * 1000

    while j <= n:
        for i in A:  # for the each of the elements in A
            while A[i] < j:  # as long as the incrementor is less than j
                iterations += 1
                A[i] += i  # add a multiple of i to the prime j (e.g., 2i, 3i, 4i,...) until greater than j
            if A[i] == j:
                break  # fall out of the for loops and proceed to the next value of j

        else:  # 'i' is not in the dictionary, so 'j' is prime
            A[j] = j  # Add j to the dictionary with the initial value j (which denotes the incrementer i
            yield j  # "RETURN" the prime j to the variable that's collecting the output and continue

        j += 1

        endtime = time.time() * 1000

    print("Variant\tms\t\titer\tbytes\telements")
    print("-------\t--\t\t----\t-----\t--------")
    print 'Sieve2\t{0}\t{1}\t{2}\t{3}'.format(endtime - starttime, iterations, sys.getsizeof(A), len(A))


# ---[ VARIATION 3 ]---------------------------------------------------------
def SieveOfEratosthenes3(n):
    '''Returns a list of the prime numbers from 2..n'''

    # Becomes infeasible after N=100000000 (10^9); runs out of memory

    #		Variant	ms		iter    	bytes		elements
    #		------- 	--         ----    	-----   	--------
    #		Sieve3	20.0      49999   	12560 	64
    #		n: 100000
    #		Number of primes in s:  9592

    # Uses a dictionary to maintain the list of odd non-primes and a generator
    #   to "yield" the primes as they are found. The test number is removed
    #   from the dictionary to conserve memory, and keys beyond the maximum (n)
    #   are not stored in the dictionary.

    yield 2  # 2 is the only even prime number, "RETURN" it and initialize q
    A = {}  # initialize the dictionary
    j = 3  # initialize to the first odd prime odd number

    iterations = 0
    starttime = time.time() * 1000

    while j <= n:
        iterations += 1
        i = A.pop(j, 0)  # retrieve (and remove) the value associated with key 'j' from dict A,
        # which represents the incrementer "2i" from the pseudocode.
        # Use '0' if the key is not in the dictionary.

        #        print 'Starting loop {3} with {0} ({0}<{1}). i={2}'.format(j,n,i, iterations)

        if i:  # If there is a key associated with 'j' in the dictionary
            x = j + i  # This sum represents the next even coefficient of "i"
            # (e.g. the "i^2+4i, +6i, ..." in the pseudocode).

            #            print '\t{0} IS NOT prime.\tx:{1} i:{2}'.format(j,x,i)

            while x in A:  # If the temp variable 'x' already has a value in A, increment
                x += i  # to the next multiple of "i" until not found in the dictionary
                #                print '\t\t{0} is already marked. Incrementing by {1}'.format(x,i)
            A[x] = i  # Finally, associate the incrementer 'i' to it's key 'x'.

        # print '\t\tMarked A[{0}] = {1}'.format(x,i)

        else:  # If the key 'j' is NOT in the dictionary...
            #            print '!\t {0} IS prime.\t Marked A[{1}] = {2}'.format(j,j*j,2*j)
            yield j  # 'j' is a prime, so "RETURN" it to the variable that's collecting the output
            # and continue
            j2 = j * j
            if (j2 <= n):  # no need to store keys to square beyond n (the stopping point)...
                A[j2] = 2 * j  # Seeds the square of the prime as composite (e.g. i^2+2i). Odd i coefficients
                #   (e.g., i^2+i, +3i, +5i, ...) are omitted because they result in even numbers,
                #   which are already excluded for efficiency

        j += 2  # Incrementing j by 2 (initailized to 3) screens out even numbers (all evens >2 are composite)

    # print'\tNext LOOP {0}'.format(j)
    #        print '----------------------------------------------------------------------'

    endtime = time.time() * 1000
    print("Variant\tms\t\titer\tbytes\telements")
    print("-------\t--\t\t----\t-----\t--------")
    print 'Sieve3\t{0}\t\t{1}\t{2}\t{3}'.format(endtime - starttime, iterations, sys.getsizeof(A), len(A))


#    print 'List of odd non-primes:\n{0}'.format(A)ps

# [TODO] ADD OTHER APPROACHES:
#   Lenstra elliptic curve factorization (<10^{25})
#   Quadratic sieve	(<10^{100})
#   General number field sieve (>10^{100})

