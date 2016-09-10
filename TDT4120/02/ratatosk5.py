from sys import stdin

stdin.readline()
stdin.readline()
rot = stdin.readline().strip()
ratatosk = stdin.readline().strip()
data = stdin.read()
nivaa = 0
while ratatosk != rot:
    try:
        i = data.index("".join((" ",ratatosk," ")))
    except ValueError:
        i = data.index("".join((" ",ratatosk,"\n")))
    try:
        a = data.rindex("\n",0,i)
        ratatosk = data[a+1:data.index(" ",a)]
    except ValueError:
        ratatosk = data[:data.index(" ",0)]
    nivaa += 1

print nivaa

