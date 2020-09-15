# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


"""
Session 1 Averaging 
"""

"""
Questions
What happens if Som initialization is forgotten ?
    if Som already existed before this code, then Sum will already have a value
    
What can you expect if all the values are below zero ?
    N value will be 0 and because we divide a number with N there will be an error 

Translate this algorithm in the python3.x language within script of name:
"""
def average_above_zero(Tab):
    Som = 0
    N = 0 
    for i in Tab :
        if i > 0 :
            Som = Som + i
             N += 1
    Moy = Som/N
    return Moy

print(average_above_zero([1,2,3]))