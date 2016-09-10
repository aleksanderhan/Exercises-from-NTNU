from sys import stdin

Inf = float('Inf')
False = 0
True = 1

def mst(n, edges):
    mintree = kruskal(n, edges)
    return max([weight for (weight, from_, to) in mintree])

def kruskal(n, edges):
    edges.sort()
    T = range(n)
    K = [[i] for i in range(n)] 
    spantree = []
    trees = n
    for (weight, u, v) in edges:
        Tu = T[u] 
        Tv = T[v]
        if Tu != Tv:
            if len(K[Tu]) > len(K[Tv]):
                u, v = v, u
                Tu, Tv = Tv, Tu
            K[Tv] += K[Tu]
            for w in K[Tu]:
                T[w] = Tv
            K[Tu] = []
            spantree.append( (weight, u, v) )
            trees -= 1
            if trees == 1:
                break
    return spantree



edges = []
from_ = 0
for line in stdin:
    for k in line.split():
        data = k.split(':')
        to = int(data[0])
        weight = int(data[1])
        edges.append( (weight, from_, to) )
    from_ += 1
print mst(from_, edges)
