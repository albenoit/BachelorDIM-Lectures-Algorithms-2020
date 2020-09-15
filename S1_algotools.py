# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def average_above_zero(table:list):
    Som = 0
    for i in table:
        if(i > 0):
            Som = Som + i
    Moy = Som/len(table)
    return(Moy)

def max_value(table:list):
    Max = 0
    for i in table:
        if(Max < i):
            Max = i
    return(Max)
    
Tab=(10,21,32,43)
print("Moyenne : " + str(average_above_zero(Tab)))
print("Max : " + str(max_value(Tab)))