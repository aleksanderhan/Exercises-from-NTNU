from sys import stdin

def shortest_path(order, M, n):
	for k in xrange(n):
		for i in xrange(n):
			for j in xrange(n):
				temp = M[i][k] + M[k][j]
				if M[i][j] > temp:
					M[i][j] = temp
	res = 0
	for i in xrange(len(order)-1):
		res += M[order[i]][order[i+1]]
	res += M[order[-1]][order[0]]
	if res == float('inf'):
		res = 'umulig'
	return res


def main():
	nt = int(stdin.readline()) # number of tests to run
	for test in xrange(nt):
		nc = int(stdin.readline()) # number of cities to visit
		order = map(int, stdin.readline().split())
		neighbor_matrix = []
		for i in xrange(nc):
			temp = map(int, stdin.readline().split())
			for j in xrange(len(temp)):
				if temp[j] < 0:
					temp[j] = float('inf')
			neighbor_matrix.append(temp)
		print shortest_path(order, neighbor_matrix, nc)




main()

