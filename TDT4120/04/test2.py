from sys import stdin

def subGraphDensity(G, inE, start):
    visited = set()
    Q = set([start])
    pop = Q.pop
    while Q:
        u = pop()
        visited.add(u)
        for v in G[u].difference(visited):
            if v in Q: continue
            Q.add(v)
    v = len(G) - len(visited)
    if v == 0:
        return 0.0
    else:
        e = sum(inE)
        for i in visited:
            e -= inE[i]
        return float(e)/(v**2)

def main():
    n = int(stdin.readline())
    G = [set([]) for _ in xrange(n)]
    inE = [0]*n
    for i in xrange(n):
        line = stdin.readline().strip()
        for j in xrange(n):
            if line[j] == '1':
                G[i].add(j)
                inE[j] += 1
    
    before = {}
    for line in stdin:
        start = int(line)
        if start not in before:
            before[start] = subGraphDensity(G,inE,start) 
            print "%.3f" % (before[start] + 1E-12)
        else:
            print "%.3f" % (before[start] + 1E-12)

main()
