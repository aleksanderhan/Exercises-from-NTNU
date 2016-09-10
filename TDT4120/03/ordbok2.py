from sys import stdin
from itertools import product

    
class Node:
    def __init__(self):
        self.child = {}
        self.index = []


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def words(word, n):
    combinations = product(alphabet,repeat=n)
    words = []
    for combination in combinations:
        newWord = word
        for i in combination:
            newWord = newWord.replace('?',i,1)
        words.append(newWord)
    return words


def build_wordtree(words):
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


def index(word, node):
    for c in word:
        if c in node.child.keys():
            node = node.child[c]
        else:
            return []
    return node.index


def main():
    WORDS = stdin.readline().split()
    wordtree = build_wordtree(WORDS)

    for line in stdin:
        word = line.strip()
        if '?' in word:
            n = word.count('?')
            searchWords = words(word,n)
        else:
            searchWords = [word]
        indices = []
        for WORD in searchWords:
            indices.extend(index(WORD,wordtree))
        indices.sort()
        indices = [str(i) for i in indices]
        print "".join((word,": "," ".join(indices)))


main()
