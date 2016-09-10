from sys import stdin


def edit_distance(s, t):

	m = len(s)
	n = len(t)

	d = [[0]*(n+1)]*(m+1)
	for i in xrange(m):
		d[i][0] = i
	for j in xrange(n):
		d[0][j] = j

	for j in xrange(n):
		for i in xrange(m):
			if s[i] == t[j]:
				d[i+1][j+1] = d[i-1][j-1]
			else:
				d[i+1][j+1] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+1)

	return d[m][n]


print edit_distance('ab','gt')


def main():
	words = []
	for line in stdin:
		words.append(line.strip())

	distances = []
	for i in xrange(len(words)-1):
		temp = []
		for j in xrange(1, len(words)-i):
			temp.append(edit_distance(words[i], words[j]))
		distances.append(temp)

	print distances

main()
