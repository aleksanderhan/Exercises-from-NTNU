from sys import stdin

class Graph:
	def __init__(self, V, E):
		self.V = V
		self.E = E



class Vertex:
	def __init__(self, d, pi):
		self.d = d
		self.pi = pi




def initialize_single_source(G, s):
	for v in G.V:
		v.d = float('inf')
		v.pi = None
	s.d = 0


def w(u,v):
	

def relax(u, v, w):
	if v.d > u.d + w



def safestPath(N, P, n):
	initialize_single_source(G,s)
	S = set()
	Q = set(range(n))
	while Q:
		u = extract_min(Q)
		S.add(u)
		for v in N[u]:
			print





def main():
	n = int(stdin.readline())
	P = map(float, stdin.readline().split())
	if (P[0] == 0.0) or (P[-1] == 0.0):
		print 0
	else:
		N = []
		for line in stdin:
			N.append(set(map(int, line.split())))

		#print safestPath(N,P,n)

	
main()