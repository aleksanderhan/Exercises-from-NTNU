from sys import stdin


def safestPath(N,P,n):
	dist = [[float("inf"), -1] for _ in xrange(n)]
	dist[0] = [P[0], -1]
	print dist

	S = set([0])
	allN = set(range(0,n))
	for i in xrange(n):
		cS = allN-S
		print cS
		nearest = (float("inf"),-1)
		for node in cS:  #intersection something something...
			for j in S&set(N[node]):
				#weight = dist[j][0]*P[j]*P[node]
				
				'''
				weight = dist[node][0]
				k = node
				print k
				while k != -1:
					weight *= dist[k][0]
					k = dist[k][1]
				'''

				weight = dist[node][0]*dist[j][0]
				

				if dist[node][0] < weight: continue
				dist[node][0] = weight
				dist[node][1] = j
				if weight < nearest[0]:
					nearest = (weight, node)
		print nearest
		S.add(nearest[1])


		print dist


	



def main():
	n = int(stdin.readline())
	P = map(float, stdin.readline().split())
	if P[0] == 0.0:
		print 0
	else:
		N = []
		#prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
		for line in stdin:
			N.append(map(int, line.split()))

		safestPath(N,P,n)

	

main()