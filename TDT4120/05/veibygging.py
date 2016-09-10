from sys import stdin





def main():
	dyrest = float(1e3000)
	G = []	
	for line in stdin:
		kanter = line.split()
		if i not in G.keys(): 
			G[i] = {}
		for kant in kanter:
			kant = map(int, kant.split(':'))
			if kant[0] <= i: continue

			G[i][kant[0]] = kant[1]
			G[kant[0]][i] = kant[1]

	print a

main()