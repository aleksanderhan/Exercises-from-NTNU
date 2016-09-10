from sys import stdin


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
	merge(decks)
	
	# Creating word from sorted decks
	print ''.join(map(letters.get, decks[0]))


def merge(decks):
	# Merg sorting decks in decks list
	decks_pop = decks.pop
	decks_append = decks.append
	while len(decks) > 1:
		A = decks_pop(0)
		B = decks_pop(0)
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

