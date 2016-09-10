from sys import stdin


class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v  
        self.capacity = w

    def __str__(self):
        return 'u: ' + str(self.source)+ ' v: '+ str(self.sink)+ ' w: '+ str(self.capacity)

    def __repr__(self):
        return self.__str__()


class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}
 
    def add_vertex(self, vertex):
        self.adj[vertex] = []
 
    def get_edges(self, v):
        return self.adj[v]
 
    def add_edge(self, u, v, w=0):
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0
 
    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path(edge.sink, sink, path + [edge]) 
                if result != None:
                    return result
 
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))


def main():
    n, ns, ne = map(int, stdin.readline().split())
    fn = FlowNetwork()
    startNodes = map(int, stdin.readline().split())
    endNodes = map(int, stdin.readline().split())


    for i in xrange(n):
        fn.add_vertex(i)
    for i in xrange(n):
        edges = map(int, stdin.readline().split())
        for j in xrange(len(edges)):
            if edges[j] == 1:
                fn.add_edge(i, j, 1)

    # adds super source and super sink
    n1 = n+1 # super source node number
    n2 = n+2 # super sink node number
    fn.add_vertex(n1)
    fn.add_vertex(n2)
    fn_addEdge = fn.add_edge
    for sn in startNodes:
        fn_addEdge(n1, sn, 1)
    for en in endNodes:
        fn_addEdge(en, n2, 1)

    
    for k, v in fn.adj.iteritems():
        print 'k: ', str(k)
        print 'v: ', str(v)


    # find the max flow
    print fn.max_flow(n1, n2)


main()