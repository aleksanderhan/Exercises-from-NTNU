from sys import stdin
from itertools import product

data = "".join((" ",stdin.readline().strip()," "))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def words(word, nr):
    combinations = product(alphabet,repeat=nr)
    words = []
    for combination in combinations:
        newWord = word
        for i in combination:
            newWord = newWord.replace("?",i,1)
        words.append(newWord)
    return words
    
        

for line in stdin:
    WORD = "".join((" ",line.strip()," "))
    indices =[]
    
    if '?' in WORD:
        nr = WORD.count("?")
        wordCombinations = words(WORD,nr)
        for word in wordCombinations:
            temp = []
            while True:
                try:
                    i = data.index(word,temp[-1]+1)
                    temp.append(i)
                except IndexError:
                    try:
                        i = data.index(word,0)
                        temp.append(i)
                    except ValueError:
                        break
                except ValueError:
                    indices.extend(temp)
                    break
        indices.sort()
        
    else:
        while True:
            try:
                i = data.index(WORD,indices[-1]+1)
                indices.append(i)
            except IndexError:
                try:
                    i = data.index(WORD,0)
                    indices.append(i)
                except ValueError:
                    break
            except ValueError:
                break

    indices = [str(i) for i in indices]
    print "".join((WORD.strip(" "),': '," ".join(indices)))
