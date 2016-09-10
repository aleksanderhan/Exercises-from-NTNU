from sys import stdin
from collections import deque
from time import clock


def checkBit(num, n):
    if (num & (1<<n)):
        return True
    else:
        return False


def main():
    n = int(stdin.readline())
    M = []
    for i in xrange(n):
        M.append(int(stdin.readline().strip(),2))

    B = [set([]) for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if checkBit(M[i], n-1-j):
                B[i].add(j)

    for line in stdin:
        t0 = clock()
        start = int(line)
        vertices = set(range(n))
        dq = deque([start])
        visited = set([])
        while dq:
            vertex = dq.popleft() 
            visited.add(vertex)
            for i in (vertices-visited):
                if checkBit(M[vertex], n-1-i):
                    dq.append(i)
        t1 = clock()
        subGraph = vertices - visited
        v = len(subGraph)
        print subGraph
        print B
        if v == 0:
            print "%.3f" % (0.0)
        else:
            e = 0
            for i in subGraph:
                e += len(B[i]&subGraph)
            density =  float(e)/(v**2)
            print "%.3f" % (density + 1E-12)
        t2 = clock()
        print (t1-t0)*100
        print (t2-t1)*100
        

main()
