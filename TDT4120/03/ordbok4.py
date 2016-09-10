from sys import stdin
    
class Node:
    def __init__(self):
        self.child = {}
        self.index = []

def build_wordtree(words):
    root = Node()
    node = root
    index = 0
    uniqueWords = set([])
    for word in words:
        if word not in uniqueWords:
            for c in word:
                if c in node.child.keys():
                    node = node.child[c]
                else:
                    node.child[c] = Node()
                    node = node.child[c]
            node.index.append(index)
            index += len(word)+1
            node = root
            uniqueWords.add(word)
        else:
            for c in word:
                node = node.child[c]
            node.index.append(index)
            index += len(word)+1
            node = root
    return root    

def index(word, root):
    if '?' in word:
        nodes = [root]
        for c in word:
            temp_nodes = []
            for node in nodes:
                if c == '?':
                    temp_nodes.extend(node.child.values())
                elif c in node.child.keys():
                    temp_nodes.append(node.child[c])
            nodes = temp_nodes
        indices = []
        for node in nodes:
            indices.extend(node.index)
        return indices
    else:
        node = root
        for c in word:
            try:
                node = node.child[c]
            except KeyError:
                return []
        return node.index

def main():
    WORDS = stdin.readline().split()
    wordtree = build_wordtree(WORDS)
    for line in stdin:
        word = line.strip()
        indices = index(word, wordtree)
        indices.sort()
        print "".join((word,": "," ".join(map(str,indices))))

main()
