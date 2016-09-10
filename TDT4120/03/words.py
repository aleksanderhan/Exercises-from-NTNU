from itertools import product
from time import clock



#alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = 'abc'
def words1(word, n):
    combinations = product(alphabet,repeat=n)
    words = []
    for combination in combinations:
        newWord = word
        for i in combination:
            newWord = newWord.replace('?',i,1)
        words.append(newWord)
    return words



def words2(word, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    combinations = product(alpha,repeat=n)
    words = []
    for combination in combinations:
        newWord = word
        for i in combination:
            newWord = newWord.replace('?',i,1)
        words.append(newWord)
    return words


def words3(word, n):
    #alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = 'abc'
    for i in xrange(n):
        alpha = "".join(alpha)
    return alpha
    
    

print words3('??',2)
print words1('??',2)

'''
t1 = clock()
words1('????',4)
t2 = clock()
print t2-t1
print

t3 = clock()
words2('????',4)
t4 = clock()
print t4-t3
print
'''
