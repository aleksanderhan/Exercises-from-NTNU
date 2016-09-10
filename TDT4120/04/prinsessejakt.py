from sys import stdin
from heapq import *
from collections import deque
from time import clock


def walk(G, s):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P):
            Q.add(v)
            P[v] = u   
    return P


def bfs(G, s):
    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P[v] = u
            Q.append(v)
    return P



def subGraphDensity(G, start):
    n = len(G)
    
    

    




def main():
    t0 = clock()
    n = int(stdin.readline())
    NLIST = [set([]) for _ in xrange(n)]
    for i in xrange(n):
        line = stdin.readline().strip()
        for j in xrange(n):
            if line[j] == '1':
                NLIST[i].add(j)
    t1 = clock()
    print t1 -t0
    
    for line in stdin:
        start = int(line)
        #subGraphDensity(NLIST, start)
        #print "%.3f" % (subGraphDensity(NLIST, start) + 1E-12)
        t0 = clock()
        #print walk(NLIST, start)
        t1 = clock()
        #print bfs(NLIST, start)
        t2 = clock()
        print 'walk: ', t1-t0
        print 'bfs: ', t2-t1

main()
