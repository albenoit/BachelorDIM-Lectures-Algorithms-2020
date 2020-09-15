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
    for i in range(len(table)):
        if(table[i] > 0):
            n = n +1
            som = som + table[i]
    moy = som / n
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

        
    