from sys import stdin
#from time import clock



def subGraphDensity(M, start):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)j
        for child in M[node]:
            if child not in visited:
                queue.append(child)

    v = len(M) - len(visited)
    if v == 0:
        return 0.0
    else:
        e = 0
        for node in graph:
            for kant in M[node]:
                if kant in graph:
                    e += 1
        return float(e)/(v**2)


def main():
    n = int(stdin.readline())
    M = [[] for _ in xrange(n)]
        
    for i in xrange(n):
        line = stdin.readline().strip()
        for j in xrange(n):
            if line[j] == '1':
                M[i].append(j)  
                
    print M

    for line in stdin:
        start = int(line)
        #subGraphDensity(M, start)
        print "%.3f" % (subGraphDensity(M, start) + 1E-12)
    

   
main()
