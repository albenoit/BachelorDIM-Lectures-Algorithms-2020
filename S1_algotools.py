# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
from random import *

def average(tab):
    
    '''
    
    This funtion calculates the average of a list
    
    Args : 
        tab: The list of number
        
    Returns the mean of the list
    
    Raises:
        Value error if no positive value is find
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
    
    '''
    
    This function returns the maximum value of a list
    
    Args :
        tab: The list of number
        
    Returns the maximum value of the list given
    
    '''
    
    max=tab[0]
    for i in tab:
        if i >= max:
            max=i
    return(max)
    
def reverse_table(tab):
    '''
    
    This function returns the reverse of the input table
    
    Args :
        tab: input table
        
    Returns the inverted table
    
    '''
    listlen=len(tab)
    for i in range (len(tab)//2):
        tmp=tab[i]
        endid=listlen-i-1
        tab[i]=tab[endid]
        tab[endid]=tmp
    #tab=tab[::-1]
    return(tab)


boolean_matrix=np.zeros((12,10),dtype=bool)
for c in range (7,9):
    for l in range (4,9):
        boolean_matrix[l,c]=1


def roi_bbox(array):
    '''
    This function returns a numpy array of shape 4x2 filled with the four 2D coordinates
    
    Args:
        lx, ly : Gives x and y coordinates of non null values
        coordinates: np.array that contains coordinates of the object
    Returns a numpy array of shape 4x2 filled with the four 2D coordinates
    '''
    lx, ly = np.nonzero(array)
    if lx is None or ly is None:
        raise ValeurError("no non null value found")
    else:
        coordinates=np.array([
                [np.min(lx),np.min(ly)],
                [np.max(lx),np.max(ly)]
                ])
    return(coordinates)
    
char_matrix_empty=np.empty([10,10],dtype=str)


def random_fill_sparse(matrice,k):
    xmax=len(matrice)
    ymax=len(matrice[1])
    for loop in range(k):
        x,y=randint(0,xmax-1),randint(0,ymax-1)
        matrice[x,y]='X'
    return matrice