from sys import stdin


class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0


def dfs(rot):
    stack = []
    node = rot
    while (node.ratatosk != True):
        node.nesteBarn += 1
        stack.append(node)
        try:
            node = node.barn[node.nesteBarn-1]
        except:
            stack.pop()
            node = stack.pop()
    return len(stack)


def bfs(rot):
    nivaa = -1
    nivaaNoder = [rot]
    found = False
    while not found:
        temp = []
        for node in nivaaNoder:
            if node.ratatosk == True:
                found = True
                break
            temp.extend(node.barn)
        nivaa += 1
        nivaaNoder = temp
    return nivaa


funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in xrange(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])
 

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print bfs(start_node)

