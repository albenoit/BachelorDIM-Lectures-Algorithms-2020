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
    """Variables initialization"""
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
    max_var = max(tab)
    max_var_index = tab.index(max_var)
    return max_var, max_var_index

#print(max_value([1, 2, 3]))

def reverse_table(tab:list):
    tab=tab[::-1]
    return tab;

#print(reverse_table([1, 2, 3]))

    
def roi_bbox(input_image): 
    
    #Variables
    rows = input_image.shape[0]
    cols = input_image.shape[1]
    
    #Each coordinates
    left_up = [0,0]
    left_down = [(rows-1),0]
    right_up = [0, (cols-1)]
    right_down = [(rows-1), (cols-1)]
    
    #Return
    z = ([left_up, right_up], [right_down, left_down])
    return z
    
lines = 5
cols = 5
input_image = np.zeros((lines, cols))   
#print(roi_bbox(input_image))
test = input_image[1:3,2:4] = np.ones((2, 3))
print(test)
'''     
for a in range(2,5):
    for b in range(1, 3):
        input_image[b, a] = 1
print(input_image)
'''

'''
input_image[1:3,2:4] = np.ones((2, 3))
'''



  
        