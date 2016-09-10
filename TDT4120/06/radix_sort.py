from sys import stdin
from math import log
#import random
#from time import clock

def getDigit(num, digitNum, base):
    return (num // base ** digitNum) % base
    
def makeBuckets(size):
    return [[] for i in xrange(size)]

def split(A, digitNum, base):
    buckets = makeBuckets(base)
    for num in A:
        buckets[getDigit(num,digitNum,base)].append(num)
    return buckets

def merge(A):
    B = []
    for a in A:
        B.extend(a)
    return B

def maxAbs(A):
    return max(abs(num) for num in A)

def radix_sort(A, base=10):
    n = int(round(log(maxAbs(A),base))+1)
    B = A[:]
    for digitNum in xrange(n):
        B = merge(split(B,digitNum,base))
    return B

'''
def makeUnsortedList(length):
    A = []
    random.seed()
    for i in xrange(length):
        A.append(random.randint(0,10000))
    return A
'''

def main():
    unsorted = map(int, stdin.readline().split())
    SORTED = radix_sort(unsorted)
    for line in stdin:
        nedre, ovre = map(int, line.split())
        finn(SORTED, nedre, ovre)


def finn(liste, nedre, ovre):
    a, b = None, None
    anf, bnf = True, True
    if liste[0] >= nedre:
            a = liste[0]
            anf = False
    i = 1
    while anf:
        a = liste[i]
        if liste[i+1] > nedre:
            anf = False
        i += 1

    if liste[-1] <= ovre:
        b = liste[-1]
        bnf = False
    i = -1
    while bnf:
        b = liste[i]
        if liste[i-1] < ovre:
            bnf = False
        i -= 1

    print a, b

    
main()
#finn([0,2,4,6,8],2,7)
#finn([11,12,13],10,14)



#unsorted =  makeUnsortedList(100000)
#t0 = clock()
#sorted = radix_sort(unsorted)
#t1 = clock()

#T0 = clock()
#unsorted.sort()
#T1 = clock()

#print "radix_sort:"
#print t1-t0

#print ".sort():"
#print T1-T0










