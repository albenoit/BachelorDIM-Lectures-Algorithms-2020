# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""



#Q1 : Si 'som' n'est pas initialisé, le code va planter lorsqy'on fait
#som = som + p_list[i] car lors de la première addition, som n'aura pas de valeur.

#Q2: Si la liste ne contient que des 0, alors le code va planter car n vaudra 0
#or on ne peut pas faire de division par 0.

#Fonction permettant de calculer la moyenne d'une liste dont la valeur est
#supérieur à 0

# @brief : permet de faire la moyenne d'une liste dont les valeurs supérieur à 0
# @param table contient une liste de nombre (float)
# @return retourne la moyenne (float)
def average_below_zero(table:list):
    '''
        This function calculs the average of a list
        Args:
            table: a float list
        Returns the average of a list
    '''
    som = 0
    n = 0
    for i in range(len(table)): #for element in p_list
        if(table[i] > 0):
            n = n +1
            som = som + table[i]
    if(n > 0):
        moy = som / n
    else:
        raise ValueError("Division par 0")
    print(moy)
    return moy


# @brief : permet de trouver la valeur maximale d'une liste de float, ainsi que son index
# @param table contient une liste de nombre (float)
# @return maxi : la valeur maximale; maxiIndex : index de la valeur maximale de la liste table
def max_value(table:list):
    '''
        This function finds the highest value of a list
        Args:
            table: a float list
        Returns the highest value of a list and its index
        Raises
    '''
    maxi = 0
    maxiIndex = None
    for i in range(len(table)):
        if(table[i] > maxi):
            maxi = table[i]
            maxiIndex = i
    return maxi, maxiIndex



def reverse_table(table:list):
    '''
        This function reverse a list
        Args:
            table: a float list
        Returns a reversed list
    '''
    return table[::-1]



import numpy as np
def roi_bbox(input_image: nympy array):
    W = 100
    H = 100
    Xin = np.zeros((H,W),dtype=float)
    
    for c in range(45,56):
        for l in range(70,91):
            Xin[l,c] = 1
    '''
    ou
    Xin [70:91,45:56] = npones((20,10)dtype=float)
    '''

malist = [1,2,3,4,5,6,7,8,9]
print(reverse_table(malist))

z = [-1]
average_below_zero(z)

        
    