from sys import stdin
import re

def main():
    data = stdin.readline().strip()
    words = data.split()
    posdic = {}
    index = 0
    for word in words:
        if word in posdic.keys():
            posdic[word].append(index)
        else:
            posdic[word] = [index]
        index += len(word)+1

    for line in stdin:
        word = line.strip()
        indices = []
        
        if '?' in word:
            p = re.compile(word.replace('?','.'))
            for key in posdic.keys():
                if len(key) == len(word):
                    try:
                        indices.extend(posdic[p.match(key).group()])
                    except AttributeError:
                        continue
            indices.sort()
            print "".join((word,": "," ".join(map(str,indices))))
        else:
            try:
                indices = posdic[word]
                print "".join((word,": "," ".join(map(str,indices))))
            except KeyError:
                print "".join((word,": "))

main()



















