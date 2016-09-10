from sys import *
import traceback
from collections import deque
from time import clock

def subgraftetthet(nabomatrise, startnode):
    t0 = clock()
    n = len(nabomatrise)
    Q = deque()
    Q.append(startnode)
    visited = {}
    while len(Q) != 0:
        v = Q.popleft()
        if v in visited:
            continue
        visited[v] = True
        for j in range(0,n):
            if nabomatrise[v][j]:
                Q.append(j)
    t1 = clock()
    print t1-t0
    noder = 0
    kanter = 0
    for i in range(0,n):
        if i in visited:
            continue
        noder = noder + 1
        for j in range(0,n):
            if nabomatrise[i][j] and j not in visited:
                kanter = kanter + 1
    t2 = clock()
    print t2-t1
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


try:
    n = int(stdin.readline())
    #t0 = clock()
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    #t1 = clock()
    #print t1-t0
    for linje in stdin:
        start = int(linje)
        #t2 = clock()
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
        #t3 = clock()
        #print t3-t2
except:
    traceback.print_exc(file=stderr)
