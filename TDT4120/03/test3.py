from sys import stdin
from itertools import product


alphabet = 'abcdefghijklmnopqrstuvwxyz'
def words(word, nr):
    combinations = product(alphabet,repeat=nr)
    words = set([])
    for combination in combinations:
        newWord = word
        for i in combination:
            newWord = newWord.replace('?',i,1)
        words.add(newWord)
    return words
    
   
def main():
    data = stdin.readline().strip().split(' ')

    d = []
    for line in stdin:
        WORD = line.strip()
        if '?' in WORD:
            n = WORD.count('?')
            d.append((WORD,words(WORD,n),[]))
        else:
            d.append((WORD,set([WORD]),[]))

    index = 0
    for word in data:
        for x in d:
            if word in x[1]:
                x[2].append(str(index))
        index += len(word)+1
    
    for x in d:
        print "".join((x[0],': ',' '.join(x[2])))

main()



