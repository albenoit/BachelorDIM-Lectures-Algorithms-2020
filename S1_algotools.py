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

#Test
z = [1,2,5,4]
if(average_below_zero(z) == 3):
    print("test1 average_below_zero: Correct")
else:
    print("test1 average_below_zero: Incorrect")
#test raise
#z = [-1]


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

#Test
z = [5,1,3,12,4,7,8,9,2]
if(max_value(z) == (12,3)):
    print("test1 max_value: Correct")
else:
    print("test1 max_value: Incorrect")


def reverse_table(table:list):
    '''
        This function reverse a list
        Args:
            table: a float list
        Returns a reversed list
    '''
    return table[::-1]

z = [1,2,3,4,5,6,7,8,9]
if(reverse_table(z) == [9,8,7,6,5,4,3,2,1]):
    print("test1 reverse_table: Correct")
else:
    print("test1 reverse_table: Incorrect")


import numpy as np
def roi_bbox(input_image: np.array):
    '''
        This function find out the coordinate of a square which got the entire
        '1' area
        Args:
            input_image: is a numpy.array of 0 and 1 values
        Returns a 4x2 numpy.array which got the coordinate (X,Y) of the square
        which got the entire '1' area
    '''
    minX = input_image.shape[0]
    maxX = 0
    minY = input_image.shape[1]
    maxY = 0
    for i in range(input_image.shape[0]):
        for j in range(input_image.shape[1]):
            if(input_image[i,j] == 1):
                if(i < minX):
                    minX = i
                if(i > maxX):
                    maxX = i
                if(j < minY):
                    minY = j
                if(j > maxY):
                    maxY = j
    return np.array([[minX,minY],[maxX,minY],[minX,maxY],[maxX,maxY]])

#Test                
W = 100
H = 100
Xin = np.zeros((H,W),dtype=float)
    
for c in range(45,56):
    for l in range(70,91):
        Xin[l,c] = 1   
        
for c in range(5,11):
    for l in range(75,86):
        Xin[l,c] = 1   
    '''
    ou
    Xin [70:91,45:56] = npones((20,10)dtype=float)
    '''

#Test
#if(roi_bbox(Xin) == np.array([[70,5],[90,5],[70,90],[90,55]])):
#    print("test1 roi_bbox: Correct")
#else:
#    print("test1 roi_bbox: Incorrect")
print(roi_bbox(Xin))




        
    