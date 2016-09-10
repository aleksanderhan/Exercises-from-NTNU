from sys import stdin


def safestPath(N, P, n):
	
	Q = [(P[0]*P[n-1],(0,n-1))]
	print Q
	i = 1
	while i < n:
		
		temp = P[0]*P[n-1]
		for j in xrange(1, n):
			



def main():
	n = int(stdin.readline())
	P = map(float, stdin.readline().split())
	if (P[0] == 0.0) or (P[-1] == 0.0):
		print 0
	else:
		N = []
		for _ in xrange(n):
			N.append(map(int, stdin.readline().split()))

		print N
		safestPath(N, P, n)
		


main()