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

import numpy as np

def average_above_zero(table:list):
    """
    Fonction qui calcule la moyenne des valeurs d'un tableau donné, en 
    sélectionnant seulement les valeurs positives
    param:
        tab : tableau donné par l'utilisateur
    returns:
        average : moyenne avec les valeurs positives de tab
    """
    sum = 0
    n = 0
    tab_size = len(table)
    for x in range(0, tab_size):
        """Check if our value is positive"""
        if table[x]>0:
            sum += table[x]
            n += 1
    average = sum/n
    return average

#print(average_above_zero([1, 2, 3]))

def max_value(tab:list):
    """
    Fonction qui renvoie la valeur max d'un tableau ainsi que son index
    param:
        tab : tableau donné par l'utilisateur
    returns:
        max_var : valeur max du tableau
        max_var_index : index de la valeur max du tableau
    """
    max_var = max(tab)
    max_var_index = tab.index(max_var)
    return max_var, max_var_index

#print(max_value([1, 2, 3]))

def reverse_table(tab:list):
    """
    Fonction qui inverse le tableau
    param:
        tab : tableau donné par l'utilisateur
    returns:
        tab : tableau inversé
    """
    tab=tab[::-1]
    return tab;

#print(reverse_table([1, 2, 3]))

    
def roi_bbox(input_image): 
    """
    Fonction qui encadre une zone définie de 1
    param:
        input_image : matrice donnée de 0 avec une zone de 1
    returns:
        z : coordonées de la forme encadrant les 1
    """

    #Variables
    rows = np.where(input_image == 1)[0]
    cols = np.where(input_image == 1)[1]
    
    #Each coordinates
    left_up = [rows[0], cols[0]]
    left_down = [rows[-1], cols[0]]
    right_up = [rows[0], cols[-1]]
    #-1 récupère la dernière valeur du tableau 
    right_down = [rows[-1], cols[-1]]
    
    #Return
    z = ([left_up, right_up], [right_down, left_down])
    return z
    
rows = 5
cols = 5
input_image = np.zeros((rows, cols))   
#print(roi_bbox(input_image))
input_image[1:3,2:5] = np.ones((2, 3))
print(input_image)
print(roi_bbox(input_image))


'''     
for a in range(2,5):
    for b in range(1, 3):
        input_image[b, a] = 1
print(input_image)
'''

'''
input_image[1:3,2:4] = np.ones((2, 3))
'''



  
        