from sys import stdin

wordPos = ['']*5000000
wordNeg = ['']*5000000
for line in stdin:
	temp = line.split(':')
	index = map(int, temp[1].strip().split(','))
	for idx in index:
		if idx >= 0:
			wordPos[idx] += temp[0]
		else:
			wordNeg[idx] += temp[0]

print "".join(wordNeg+wordPos)