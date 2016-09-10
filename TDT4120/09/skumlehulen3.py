from sys import stdin


def main():
    n, ns, ne = map(int, stdin.readline().split()) # nodes, start nodes, end nodes
    if n == 1: 
        print '1'   #  
        return;   #  Flow problem solved
    startRom = map(int, stdin.readline().split())
    utgang = map(int, stdin.readline().split())
    iS = [False] * n
    iE = [False] * n
    #iS = []
    #iE = []

    for s in startRom:
        #iS.append(True)
        iS[s] = True

    for u in utgang: 
        iE[u] = True

    for line in stdin:
        if not iE[u]:
            L[u] = [v for v in xrange(n) if line[2*v] == '1' and not iS[v]]



    vei = 0
    for s in startRom:
        if iE[s]:
            iE[s] = False
            continue;
        P = [-1] * n
        Q = [s]
        qpop = Q.pop
        q_append = Q.append
        while Q:
            u = qpop(0)
            for v in L[u]:
                if P[v] == -1:
                    P[v] = u
                    if not iE[v]:
                        q_append(v)
                    else:
                        iE[v] = False
                        w = v
                        while w != s:
                            L[w] = L[P[w]] + [P[w]]
                            w = P[w]
                        Q = []
                        vei += 1
                        break;
    print str(vei)

main()
