from sys import stdin

stdin.readline()
stdin.readline()
rot = "".join((" ",stdin.readline().strip()," "))
ratatosk = "".join((" ",stdin.readline().strip()," "))


data = stdin.read()
nivaa = 0
while ratatosk != rot:
    try:
        i = data.index(ratatosk)
    except ValueError:
        i = data.index("".join((ratatosk.rstrip(" "),"\n")))

    try:
        a = data.rindex("\n",0,i)
    except ValueError:
        a = 0

    b = data.index(" ",a)
    ratatosk = "".join((" ",data[a+1:b]," "))
    nivaa += 1  

print nivaa

