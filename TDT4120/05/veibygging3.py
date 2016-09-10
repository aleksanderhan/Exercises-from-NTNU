from sys import stdin
from heapq import *



def prim(G):
	





def main():
	dyrest = float(1e3000)
	G = []
	for line in stdin:
		d = {}
		kanter = line.split()
		for kant in kanter:
			v, pris = map(int, kant.split(':'))
			d[v] = pris
		G.append(d)


			

main()