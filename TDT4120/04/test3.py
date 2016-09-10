from sys import stdin

def subGraphDensity(G, start):
    visited = set()
    Q = set([start])
    while Q:
        u = Q.pop()
        visited.add(u)
        for v in G[u].difference(visited):
            if v in Q: continue
            Q.add(v)
    v = len(G) - len(visited)
    if v == 0:
        return 0.0
    else:
        e = 0
        for i in G:
            if i in visited: continue
            for j in i:
                if j not in visited:
                    e+=1
        return float(e)/(v**2)

def main():
    n = int(stdin.readline())
    G = [set([]) for _ in xrange(n)]
    for i in xrange(n):
        line = stdin.readline().strip()
        for j in xrange(n):
            if line[j] == '1':
                G[i].add(j)

    for line in stdin:
        start = int(line)
        print "%.3f" % (subGraphDensity(G, start) + 1E-12)

main()
