from sys import stdin
from itertools import product

    
class Node:
    def __init__(self):
        self.child = {}
        self.index = []


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def words(word, n):
    combinations = product(alphabet,repeat=n)
    words = set([])
    for combination in combinations:
        newWord = word
        for i in combination:
            newWord = newWord.replace('?',i,1)
        words.add(newWord)
    return words


def build_wordtre(words):
    root = Node()
    node = root
    index = 0
    for word in words:
        for c in word:
            if c in node.child.keys():
                node = node.child[c]
            else:
                newNode = Node()
                node.child[c] = newNode
                node = newNode
        node.index.append(index)
        index += len(word)+1
        node = root
    return root    


def main():
    WORDS = stdin.readline().split()
    wordtree = build_wordtre(WORDS)

    for line in stdin:
        word = line.strip()
        node = wordtree
        indices = []
        if '?' in word:
            n = word.count('?')
            searchWORDS = words(word, n)
        else:
            searchWORDS = [word]
        for WORD in searchWORDS:
            for c in WORD:
                if c in node.child.keys():
                    node = node.child[c]
                else:
                    break
            indices.extend(node.index)
            node = wordtree
        indices.sort()
        indices = [str(i) for i in indices]
        print "".join((word,": "," ".join(indices)))

main()
