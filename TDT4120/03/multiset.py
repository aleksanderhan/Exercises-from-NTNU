from sys import stdin
import re



def main():
    data = stdin.readline().split()
    
    posdic = {}
    index = 0
    for word in data:
        try:
            posdic[word].append(index)
        except KeyError:
            posdic[word] = [index]
        index += len(word)+1

    dataSet = set(data)

    for line in stdin:
        word = line.strip()
        if word in dataSet:
            print "".join((word,": "," ".join(map(str,posdic[word]))))
        elif '?' in word:
            p = re.compile(word.replace('?','.'))
            indices = []
            for w in dataSet:
                m = p.match(w)
                try:
                    if len(m.group()) == len(w):
                        indices.extend(posdic[w])
                except AttributeError:
                    continue
            indices.sort()
            print "".join((word,": "," ".join(map(str,indices))))
        else:
            print "".join((word,":"))
                
    
main()
