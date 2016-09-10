from sys import stdin


class Node:


	def __init__(self, key, value):
		self.key = key
		self.value = value



def main():
	

	for line in stdin:
		temp = line.split(':')
		posisjoner = map(int, temp[1].strip().split(','))





main()