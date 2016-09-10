from sys import stdin


def safestPath(N,P,n):
	dist = [[0, -1] for _ in xrange(n)]
	dist[0] = [P[0], -1]
	V = set(xrange(n))
	i = 0
	S = set([0])
	while i < n+1:
		safest = (0,-1)
		for v in (V-S):
			'''
			innSet = set()
			for s_idx in xrange(n):
				if v in N[s_idx]:
					innSet.add(s_idx)
			'''
			for u in S:
				if v in N[u]:
					temp = 1-dist[u][0] + dist[u][0]*P[v]
					if temp > dist[v][0]:
						dist[v][0] = temp
						dist[v][1] = u


			if dist[v][0] > safest[0]:
				safest = (dist[v][0], v)
		S.add(safest[1])
		i += 1
		#print dist
	k = n-1
	path = [k]
	while k != 0:
		k = dist[k][1]
		path.append(k)

	path.reverse()
	return "-".join(map(str, path))





def main():
	n = int(stdin.readline())
	P = map(float, stdin.readline().split())
	if (P[0] == 0.0) or (P[-1] == 0.0):
		print 0
	else:
		N = []
		for line in stdin:
			N.append(set(map(int, line.split())))

		print safestPath(N,P,n)

	
main()