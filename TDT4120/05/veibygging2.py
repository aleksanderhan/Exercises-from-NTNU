from sys import stdin


def prim(E, V, p):
	visited = set()
	Q = set([0])
	pop = Q.pop
	while Q:
		u = pop()
		E
		for v in V[u]:
			if E
		visited.add(u)




def main():
	p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
	dyrest = float(1e3000)
	E = {}
	V = []
	u = 0
	for line in stdin:
		kanter = line.split()
		s = set()
		for kant in kanter:
			v, pris = map(int, kant.split(':'))
			s.add(v)
			if v <= u: continue
			E[p[u]*p[v]] = pris
		V.append(s)
		u += 1




main()