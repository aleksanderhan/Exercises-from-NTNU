from sys import stdin



def main():
	n = int(stdin.readline().strip())
	probabilities = map(float, stdin.readline().strip().split(' '))
	nabomatrix = []
	for line in stdin:
    	row = [0] * n
    	neighbors = map(int, linje.strip().split(' '))
    	for neighbor in neighbors:
        	row[neighbor] = 1
    	nabomatrix.append(row)

main()
