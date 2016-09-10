from sys import stdin

stdin.readline()
stdin.readline()
rot = stdin.readline().strip()
ratatosk = stdin.readline().strip()

tre = []
nivaa = 0
for line in stdin:
    tall = line.split()
    node = (tall[0], tall[1:])
    if ratatosk in node[1]:
        ratatosk = node[0]
        nivaa += 1
    else:
        tre.append(node)

while ratatosk != rot:
    for node in tre:
        if ratatosk in node[1]:
            ratatosk = node[0]
            nivaa += 1

print nivaa

