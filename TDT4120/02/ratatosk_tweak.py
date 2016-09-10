from sys import stdin

def main():
    stdin.readline()
    stdin.readline()
    rotnode = stdin.readline().strip()
    ratatosk = stdin.readline().strip()
    foreldre = {}
    nivaa = 0
    for linje in stdin:
        barn_liste = linje.split()
        far = barn_liste.pop(0)
        for barn in barn_liste:
            foreldre[barn] = far
        while ratatosk in foreldre:
            ratatosk = foreldre[ratatosk]
            nivaa+=1
        if ratatosk == rotnode :
            print nivaa
            return

main()
