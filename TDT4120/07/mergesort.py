from sys import stdin


def main():
	# Making datastructures
	decks = []
	letters = {}
	for line in stdin:
		temp = line.split(':')
		deck = map(int, temp[1].strip().split(','))
		decks.append(deck)
		for number in deck:
			letters[number] = temp[0]

	# Merg sorting decks in decks list
	while len(decks) > 1:
		a = decks.pop(0)
		b = decks.pop(0)
		decks.append(merge(a,b))

	# Creating word from sorted decks
	word = ''
	for i in decks[0]:
		word += letters[i]
	print word


def merge(A, B):
	i, j = 0, 0
	res = []

	# Appending the values from list A and B to res in sorted order
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			res.append(A[i])
			i += 1
		else:
			res.append(B[j])
			j += 1

	# Appending the rest of the lists A and B to res
	while i < len(A):
		res.append(A[i])
		i += 1
	while j < len(B):
		res.append(B[j])
		j += 1

	return res


main()

