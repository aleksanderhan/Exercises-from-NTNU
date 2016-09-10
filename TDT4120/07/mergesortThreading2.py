from sys import stdin
import threading


def main():
	# Making datastructures
	decks = []
	letters = {}
	decks_append = decks.append
	for line in stdin:
		temp = line.split(':')
		deck = map(int, temp[1].strip().split(','))
		decks_append(deck)
		for number in deck:
			letters[number] = temp[0]

	# Calling merge function

	decks = [decks[:len(decks)/2], decks[len(decks)/2:]]
	t1 = threading.Thread(target=merge, args=(decks[0],))
	t2 = threading.Thread(target=merge, args=(decks[1],))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	decks = decks[0]+decks[1]
	merge(decks)

	
	# Creating word from sorted decks
	print ''.join(map(letters.get, decks[0]))


def merge(decks):
	# Merg sorting decks in decks list
	pop = decks.pop
	decks_append = decks.append
	while len(decks) > 1:
		A = pop(0)
		B = pop(0)
		i, j = 0, 0
		res = []

		# Appending the values from list A and B to res in sorted order
		res_append = res.append
		while i < len(A) and j < len(B):
			if A[i] < B[j]:
				res_append(A[i])
				i += 1
			else:
				res_append(B[j])
				j += 1

		# Appending the rest of the lists A and B to res
		while i < len(A):
			res_append(A[i])
			i += 1
		while j < len(B):
			res_append(B[j])
			j += 1

		decks_append(res)


main()

