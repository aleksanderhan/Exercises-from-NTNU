from sys import stdin
import timeit, time


class Node:
    def __init__(self):
        sself.child = {}
        self.index = []
        self.keySet = set([])


#NTNUTweak
class NTNUTweak:

    def main():
        # Leser inndata
        ordliste = stdin.readline().split()
        sok = stdin.read()
                
        # Opprettholder en dict med referanser mellom ord og en liste med deres posisjoner.
        ordbok = {}
        pos = 0
                            
        # Bygger ordlisten. Dersom det finnes '?' blant oppslagene, lager vi ogsa et tre utfra bokstavene i hvert ord.
        if '?' in sok:
            ord_tre = ({}, [])
            for t in ordliste:
                if t not in ordbok:
                    n = ord_tre
                    for c in t:
                        if c not in n[0]:
                            n[0][c] = ({},[])
                        n = n[0][c]
                    ordbok[t] = n[1]
                ordbok[t].append(pos)
                pos += len(t) + 1
        else:
            for t in ordliste:
                if t not in ordbok:
                    ordbok[t] = []
                ordbok[t].append(pos)
                pos += len(t) + 1

        # Gjennomforer oppslagene, ord for ord. Der vi har mulighet, slaar vi direkte opp i ordboken.
        # Skriver ut svarene underveis.
        for ord in sok.split():
            if ord in ordbok:
                posi = ordbok[ord]
            elif '?' in ord:
                # Der det dukker opp '?', maa vi huske paa alle mulighetene
                noder = [ord_tre]
                for c in ord:
                    nye = []
                    for n in noder:
                        if c == '?':
                            nye.extend(n[0].values())
                        elif c in n[0]:
                            nye.append(n[0][c])
                    noder = nye
                posi = []
                for n in noder:
                    posi.extend(n[1])
                ordbok[ord] = posi
            else:
                posi = []
                ordbok[ord] = posi
            posi.sort()
            print ord + ":",
            for p in posi:
                print p,
            print



class Ordbok5: 

    def index(word, root):
        if '?' in word:
            nodes = [root]
            for c in word:
                temp_nodes = []
                for node in nodes:
                    if c == '?':
                        temp_nodes.extend(node.child.values())
                    elif c in node.keySet:
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













































