from sys import stdin
stdin.readline()
stdin.readline()
rot = stdin.readline().strip()
ratatosk = stdin.readline().strip()
data = stdin.read().replace("\n",' .')
nivaa = 0
while ratatosk != rot:
    i = data.index("".join((" ",ratatosk," ")))
    try:
        a = data.rindex(".",0,i)
        ratatosk = data[a+1:data.index(" ",a)]
    except ValueError:
        ratatosk = data[:data.index(" ")]
    nivaa += 1
print nivaa
