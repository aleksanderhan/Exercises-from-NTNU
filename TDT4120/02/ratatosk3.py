from sys import stdin

stdin.readline()
stdin.readline()
rot = str(int(stdin.readline()))
ratatosk = str(int(stdin.readline()))


tre = []
for line in stdin:
    tall = line.split()
    tre.append((tall[0], set(tall[1:])))

nivaa = 0
while ratatosk != rot:
    for i in tre:
        if ratatosk in i[1]:
            ratatosk = i[0]
            nivaa += 1
            tre.remove(i)

print nivaa
