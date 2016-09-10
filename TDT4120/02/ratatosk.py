from sys import stdin


class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    forelderNode = None
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0
        self.forelderNode = None


def dfs(rot):
    node = rot
    nivaa = 0
    while (node.ratatosk != True):
        node.nesteBarn += 1
        try:
            node = node.barn[node.nesteBarn-1]
            nivaa += 1
        except:
            node = node.forelderNode
            nivaa -= 1
    return nivaa


def bfs(rot):
    nivaa = -1
    nivaaNoder = [rot]
    found = False
    while found == False:
        for node in nivaaNoder:
            if node.ratatosk == True:
                found = True
        nivaa += 1
        temp = []
        for node in nivaaNoder:
            temp.extend(node.barn)
        nivaaNoder = temp
    return nivaa


funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])
        for barn in temp_node.barn:       
            barn.forelderNode = temp_node 


if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print dfs(start_node)
