# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""
Q1 / Si on oublie l'initialisation de la variable on ne pourra pas l'utiliser 
dans le for ensuite.
"""

"""
Q2 / Si toutes les variables sont en dessous de 0, on ne passe pas dans le if, 
et donc on essaye de faire une division par 0 ce qui renvoie une erreur.
"""

def average_above_zero(table:list):
    sum = 0
    n = 0
    tab_size = len(table)
    for x in range(0, tab_size):
        if table[x]>0:
            sum += table[x]
            n += 1
    average = sum/n
    return average

print(average_above_zero([1, 2, 3]))