from sys import stdin

def insertionSort(A):
	for i in xrange(1,len(A)):
		x = A[i]
		j = i
		while j > 0 and A[j-1] > x:
			A[j] = A[j-1]
			j -= 1
		A[j] = x
	return A

def main():
	deck = {}
	for line in stdin:
		temp = line.split(':')
		posisjoner = map(int, temp[1].strip().split(','))
		for pos in posisjoner:
			deck[pos] = temp[0]

	word = []
	for i in insertionSort(deck.keys()):
		word.append(deck[i])

	print "".join(word)

main()
print 'hello'