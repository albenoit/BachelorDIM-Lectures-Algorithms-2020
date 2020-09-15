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
    return Moy

print(average_above_zero(Tab))
# 1. Si Som n'est pas défini, le programme ne fonctionne plus
# 2. Si toutes les valeus sont en dessous de 0, N restera à 0 et donc une
#   erreur apparaitra à "Moy = Som/N"

def maximum_value(table:list):
    '''
        This function find the highest value in the list
        Args:
            table: list of number
        Returns the maximum value of a list
    '''
    maxValue = 0
    index = 0
    for i in range (1,len(table)):
        if(table[i] > maxValue):
            maxValue = table[i]
            index = i+1
    return maxValue,index
    
(maxi,index) = maximum_value(Tab)
print("Valeur Max : {} , index de la valeur max : {}".format(maxi,index))

