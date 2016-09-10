from sys import stdin


def subGraphDensity(N, M, e, start):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        for child in N[node]:
            if child not in visited:
                queue.append(child)

    v = len(M) - len(visited)
    if v == 0:
        return 0.0
    else:
        for node in visited:
            e -= M[node].count('1')
        return float(e)/(v**2)


def main():
    n = int(stdin.readline())
    
    NLIST = [[] for _ in xrange(n)]
    M = [[] for _ in xrange(n)]
    
    e = 0
    for i in xrange(n):
        line = stdin.readline().strip()
        for j in xrange(n):
            M[j].append(line[j])
            if line[j] == '1':
                e += 1
                NLIST[i].append(j)
    for k in xrange(n):
        M[k] = "".join(M[k])

    for line in stdin:
        start = int(line)
        print "%.3f" % (subGraphDensity(NLIST, M, e, start) + 1E-12)


main()
