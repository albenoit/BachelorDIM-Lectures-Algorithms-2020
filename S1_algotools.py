# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def average(tab):
    sum = 0
    n = 0
    tab_size = len(tab)
    for x in range(0, tab_size):
        if tab[x]>0:
            sum += tab[x]
            n += 1
    average = sum/n
    return average

print(average([1, 2, 3]))