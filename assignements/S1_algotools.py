
def average(tab):
    som=0
    n=0
    for i in range(len(tab)):
        if tab[i] > 0:
            som = som + tab[i]
            n = n+1
    moy = som/n
    print(moy)

average([100, 20, 30])