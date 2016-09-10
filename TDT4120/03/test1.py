from sys import stdin
from time import clock


def key_words(word, keys):
    keys = [key for key in keys if (len(key) == len(word))]
    for i in xrange(len(word)):
        keyWords = []
        for key in keys:    
            if (word[i] == key[i]) or (word[i] == '?'):
                keyWords.append(key)
        keys = keyWords
    return keys
            

def main():
    words = stdin.readline().split()
    posdic = {}
    index = 0
    t0 = clock()
    for word in words:
        if word in posdic.keys():
            posdic[word].append(index)
        else:
            posdic[word] = [index]
        index += len(word)+1
    t1 = clock()

    for line in stdin:
        word = line.strip()
        if '?' in word:
            keyWords = key_words(word,posdic.keys())
            indices = []
            for kw in keyWords:
                indices.extend(posdic[kw])
            indices.sort()
            print "".join((word,": "," ".join(map(str,indices))))
        else:
            try:
                indices = posdic[word]
                indices.sort()
                print "".join((word,": "," ".join(map(str,indices))))
            except KeyError:
                print "".join((word,": "))

    t2 = clock()
    print t1-t0
    print t2-t1
main()
