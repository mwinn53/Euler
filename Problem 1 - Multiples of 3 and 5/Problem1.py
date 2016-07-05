# ---------------------------------------------------------------------------
# Problem 1 
# ---------------------------------------------------------------------------
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Observations: The first attempt assumed this problem seemed as simple as
# computing the sum of the multiples of 3 between 1 and 1000, plus the sum
# of multiples of 5 between 1 and 1000, using the formula Sn = n/2 (a1 + an)
# each multiple. Closer analysis of the problem revealed that the answer is
# looking for the UNIQUE multiples of both 3 and 5, so the revised solution
# builds a list of each of the multiples, merges them together, then sums the
# resulting values.


# function: SumofMultiples(max, factors)        Slick or Naiive
#   input:  (int) maximum number, (list) factors to sum
#   output: sum of all multiples of each of the factors, from 1 to max_num

def SumofMultiplesSlick(max, factors):

    sum = 0
    
    for f in factors:    
        # find the multiples (n) of f from 1 to max
        #   adjust the max term to a multiple of f
        for i in range(max-1, max-f-1, -1):
            if i % f == 0:
                end = i
                break

        # adjust the starting term to a multiple of f
        for i in range(1, f+1, 1):
            if i % f == 0:
                start = i
                break

        # an = a1 + (n - 1)d OR n = (an - a1 + d)/d
        n = (end - start + f) / f

        sum += int((n/2.0)*(start + end))

    strFactors = str(factors)
        
    print 'The sum of all natural numbers below {0} that are multiples of {1} is {2}' \
          .format(max, strFactors, sum)
    
    return sum

def SumofMultiplesNaiive(max, factors):
    sum = 0
    
    for f in factors:    
        for i in range(f, max, f):
            sum = sum + i
    
    strFactors = str(factors)

    print 'The sum of all natural numbers below {0} that are multiples of {1} is the {2}' \
          .format(max, strFactors, sum)
        
    return sum

# function: SumofMultiples2(max, factors)
#   input:  (int) maximum number, (list) factors to sum
#   output: sum of all multiples of each of the factors, from 1 to max_num

def SumofMultiples2(max, factors):

    sum = 0
    multiples = []
    
    for f in factors:
        templist = []
        
        for i in range(f, max, f):
            templist.append(i)

        strList = str(templist)
        print 'The list of multiples of {0} is \n{1}\n'.format(f, strList)
 
        multiples.append(templist)

    combo = []
    
    for l in multiples:
       combo = list(set(combo + l)) 

    for c in range(0, len(combo)):
        sum = sum + combo[c]
    
    strFactors = str(factors)

    strCombo = str(combo)
    print 'The consolidated list of unique multiples of {0} is \n{1}\n' \
          .format(strFactors, strCombo)

    print 'The sum of all natural numbers below {0} that are multiples of {1} is the {2}' \
          .format(max, strFactors, sum)
        
    return sum
