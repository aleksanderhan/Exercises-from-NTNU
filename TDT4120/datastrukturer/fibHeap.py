# Fibonacci heap
from math import log, ceil

class Fib_node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self
        self.right = self
        self.parent = None
        self.child = None
        self.degree = 0
        self.mark = False

    def append_child(self, y):
        child = self.child
        if child == None:
            child = y
        else:
            y.right = child.right
            y.left = child
            child.right = y
            y.right.left = y
        y.parent = self
        self.degree += 1

    def remove_child(self, x):
        self.child.remove(x)
        self.degree -= 1
        left = x.left
        right = x.right
        x.left, x.right, x.parent = None, None, None
        left.right = right
        right.left = left


class Fibonacci_heap(object):
    
    def __init__(self):
        self.nodes = [] # ikke i boka
        self.roots = []
        self.min = None
        self.n = 0

    def insert(self, key, value=None):
        x = Fib_node(key, value)
        self.nodes.append(x) # ikke i boka
        self.roots.append(x)
        if self.min == None:
            self.min = x
        elif key < self.min.key:
            self.min = x
        self.n += 1

    def merge(h2):
        self.roots += h2.roots
        if (self.min == None) or (h2.min != None and h2.min.key < self.min.key):
            self.min = h2.min
        self.n += h2.n

    def pop(self):
        z = self.min
        if z != None:
            x = z.child
            for i in xrange(z.degree):
                self.roots.append(x)
                x.parent = None
                x = x.right
            self.roots.remove(z)
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return z
 
    def _consolidate(self):
        Dn = int(ceil(log(self.n)))
        A = [None for i in xrange(Dn)]
        for x in self.roots:
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    temp = x
                    x = y
                    y = temp
                link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        self.min = None
        for i in xrange(Dn):
            if A[i] != None:
                if self.min == None:
                    self.roots = [A[i]]
                else:
                    self.roots.append(A[i])
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def _link(self, y, x):
        self.roots.remove(y)
        x.append_child(y)
        y.mark = False

    def decrease_key(self, x, k):
        if k > x.key:
            print 'error: new key is greater than current key'
        x.key = k
        y = x.parent
        if y != None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x, y):
        y.remove_child(x)
        self.roots.append(x)
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z != None:
            if y.mark == False:
                y.mark = True
            else:
                _cut(y, z)
                _cascading_cut(z)

    def delete(self, x):
        self.decrease_key(x, -float('inf'))
        self.pop()







'''test'''
H = Fibonacci_heap()
H.insert(3.5,'a')
H.insert(4,'b')
H.insert(float('inf'),'first out')
H.insert(9, 'm')
a = H.pop()
H.decrease_key(H.nodes[0], 2)

for fn in H.nodes:
    print fn.key
