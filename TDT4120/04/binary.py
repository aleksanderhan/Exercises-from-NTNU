from sys import stdin


def checkBit(num, n):
    if (num & (1<<n)):
        return True
    else:
        return False


def setBit(num, n):
    return num | (1<<n)


def unsetBit(num, n):
    return num & ~(1<<n)


def matrixMult(B, x):
    n = len(B)
    y = 0
    for i in xrange(n):
        if B[i] & x != 0:
            y = setBit(y, n-i-1)
    return y


def vertices(y):
    return bin(y).count('1')


def edges(B, y):
    n = len(B)    
    rows = set([])
    for i in xrange(n):
        if checkBit(y, n-1-i):
            rows.add(i)
    e = 0
    for i in rows:
        for j in (rows - set([i])):
            if checkBit(B[j],n-1-i):
                e += 1
    return e

def subGraphDensity(M, start):
    n = len(M)
    B = [int(i,2) for i in M]

    x = setBit(0, n-1-start)  
    y = matrixMult(B,x)|x
    while x != y:
        temp = y
        y = matrixMult(B,y)
        y = y|temp
        x = temp
    
    y = y ^ (2**n -1)
    
    e = edges(B, y)
    v = vertices(y)
    if v == 0:
        return 0.0
    else:
        return float(e)/(v**2)
    

def main():
    n = int(stdin.readline())
    M = [[] for _ in xrange(n)]
    for i in xrange(n):
        line = list(stdin.readline().strip())
        for j in xrange(n):
            M[j].append(line[j])
    for i in xrange(n):
        M[i] = "".join(M[i])
    print M
    for line in stdin:
        start = int(line)
        print "%.3f" % (subGraphDensity(M, start) + 1E-12)


main()

    
