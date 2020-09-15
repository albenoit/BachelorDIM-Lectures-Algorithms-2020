# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def average(tab):
    
    '''
    
    This funtion calculates the average of a list
    
    Args : 
        tab: The list of number
        
    Returns the mean of the list
    
    '''
    
    som = 0
    n=0
    for i in range(len(tab)):
        if tab[i] > 0:
            som = som + tab[i]
            n = n+1
    if n>0:
        moy = som/n
    else:
        raise ValueError('no positive value found')
    return(moy)
    
    '''
    What happens if som initilization is forgotten ?
        L'erreur NameError: name 'som' is not defined
        Il faut donc la déclarer
        
    What can you expect if all the values are below zero ?
        Le calcul ne les prendra pas en compte  
    '''
    
def max_value(tab):
    max=tab[0]
    for i in tab:
        if i >= max:
            max=i
    print(max)