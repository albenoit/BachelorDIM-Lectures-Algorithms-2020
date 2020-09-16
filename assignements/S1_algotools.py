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
    if Som never existed then it will make an eror 
    if Som already existed before this code, then Sum will already have a value
    
What can you expect if all the values are below zero ?
    N value will be 0 and because we divide a number with N there will be an error 

Translate this algorithm in the python3.x language within script of name:
"""
def average_above_zero(Tab):
    '''
    This function return th average of all he numbers above 0 in array
    Parameters:
        Tab: a table of numner 
    Returns: a reversed table 
    Raises: an error if there is no positive values in the list (Tab)
    '''
    Som = 0
    N = 0 
    for i in Tab :
        if i > 0 :
            Som = Som + i
            N = N + 1
        if N>0:
            Moy = Som/N
        else:
            raise ValueError('division par zero')
    return Moy

print(average_above_zero([1,2]))



"""
Session 1 Table maximum value
"""

"""
Propose changes on the previous algorithm to get the maximum value of
a table.
"""
def  max_value_without_index(Tab):
    '''
    This function return the highest value finded in a list
    Parameters:
        Tab: a list of number 
    Returns: highest value 
    '''
    Max = 0 
    for i in Tab :
        if i > Max :
            Max = Max                       
    return Max

print(average_above_zero([1,2,3]))
"""
Improve the previous changes by capturing the index of the last maximum
value.
"""
def  max_value(Tab):
    '''
    This function return the highest value finded in a list
    Parameters:
        Tab: a list of number 
    Returns: highest value and it's index (highestvalue,Index)
    '''
    Max = 0 
    N=0
    Index = 0
    for i in Tab :
        if i > Max :
            Max = i
            Index = N
        N+=1     
                              
    return (Max,Index)

print(max_value([4,2,3]))

"""
Session 1 Reverse a table 
"""
def reverse_table(tab):
    '''
    This function reverse a table
    Parameters:
        Tab: a table of numner 
    Returns: a reversed table 
    '''
    #ce code consome beaucoup plus de mémoire a cause de pop et insert 
    #listlen = len(tab)
    #for i in range (listlen):
    #    last=tab[-1]
    #    tab.pop(listlen-1)
    #    tab.insert(i,last)
    listlen = len(tab)
    for i in range(listlen//2):
        tmp=tab[i]
        endid=listlen-i-1
        tab[i] = tab [endid]
        tab[endid]=tmp
    return tab
 
        
print(reverse_table([1,2,3,4,5,6]))

"""
Session 1 Bounding box
"""

import numpy as np
H=100
W=1000
n = np.zeros((W,H),dtype=float)
n[45:450,70:91] = 1
#on peut aussi écrire: 
#n[2:4,3:5] = np.ones((2,2)) avec deux tableau de même taille
#trop lent 
#for c in range (45,55):
#    for d in range (70,91):
#        n[c,d]=1

def roi_bbox(image):
    '''
    This function return a numpy array with the coord of a bounding box
    Parameters:
        image: a numpy array  
    Returns: a numpy array with 4 coordinates
    '''
    
    upper_x =image.shape[1]+1
    upper_y =image.shape[0]+1
    lower_x =0
    lower_y =0
    x=0
    y=0
    for ligne in image:       
        for point in ligne:          
            if point != 0:
                if upper_x > x:
                    upper_x = x
                if upper_y > y:
                    upper_y = y
                if lower_x < x:
                    lower_x = x
                if lower_y < y:
                    lower_y = y                                
            y+=1
        y=0
        x+=1
    return np.array([upper_x,upper_y,lower_x,lower_y])
print(roi_bbox(n))
