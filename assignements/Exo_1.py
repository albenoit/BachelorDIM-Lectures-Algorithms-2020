# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:26:05 2020

@author: vanhouta
"""

Tab = [1,5,9,8,7,5,9,6,7,2]

## Documentation for average_above_zero
# @param _table table with number above zero
def average_above_zero(table:list):
    Som = 0 
    ## @var _Som
    # Sum of all number
    N = 0
    ## @var _N
    # Length of the table
    for i in range (1,len(table)):
        if(table[i] > 0):
            Som += table[i]
            N += 1
            
    Moy = Som/N
    print(Moy)

average_above_zero(Tab)

# 1. Si Som n'est pas défini, Som ne s'initialisera jamais à 0 lors du
#   du lancement du programme
# 2. Si toutes les valeus sont en dessous de 0, N restera à 0 et donc une
#   erreur apparaitra à "Moy = Som/N"