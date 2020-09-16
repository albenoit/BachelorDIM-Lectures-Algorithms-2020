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
    for i in range(len(table)//2): # // permet de faire une division entière
        tmp = table[i]
        table[i] = table[len(table) - i -1]
        table[len(table) - i -1] = tmp
    
    #return table[::-1]
    return table

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
    if(1 in input_image):
        maxX = 0
        maxY = 0
        minX = input_image.shape[0]       
        minY = input_image.shape[1]       
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
    else:
        raise ValueError("La matrice ne possède pas de '1'")
    return np.array([[minX,minY],[maxX,minY],[minX,maxY],[maxX,maxY]])
#On peut, en python, renvoyer plusieurs données comme ceci:
    #return x,y,z
#Pour les récupérer, il suffit de faire:
    #a,b,c = roi_bbox(Xin)
#ou
    #mybbox = roi_bbox(Xin)
    #a = mybbox[0]
    #b = mybbox[1]
    #c = mybbox[2]

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


from random import *
def alea(v):
    '''
        This function generates a random int
        Arg:
            v: int, this is the maximum value of the random
        Returns an int, a random number between 0 and v
    '''
    return randint(0,v)

def random_fill_sparse(table:np.array, k:int):
    '''
        This function fill a chosen number of cell with a 'X' in a matrice
        Args:
            table: numpy.array, is a matrice
            k: int, is the number of cell we want to fill with a 'X'
        Returns the matrice with k 'X'
    '''
    if(k > table.size): #dans le cas où K est supérieur à la taille de la matrice
    #alors on remplit toute la matrice
        table = np.full(shape=(table.shape[0],table.shape[0]),fill_value="X")
    else:
        for i in range(k):
            rdmX = alea(table.shape[0]-1)
            rdmY = alea(table.shape[0]-1)            
            while(table[rdmX,rdmY] == "X"):
                rdmX = alea(table.shape[0]-1)
                rdmY = alea(table.shape[0]-1) 
            table[rdmX,rdmY] = "X"
    return table
    
#Test                
W = 5
H = 5
Xin = np.zeros((H,W),dtype=str)
print(random_fill_sparse(Xin,5))


def remove_whitespace(table:str):
    '''
        This function removes white space
        Arg:
            table: string, is a sentence
        Return a string, table without white space
    '''
    return table.replace(' ','')

#Test
print(remove_whitespace("bonjour les amis"))


def shuffle(list_in:list):
    '''
        This function shuffle a list
        Arg:
            list_in: a list of items
        Return a suffled list
    '''
    rdmIndex = alea(len(list_in) -1)
    resultat = [list_in[rdmIndex]]
    listIndex = [rdmIndex]
    for i in range(len(list_in) -1):
        while rdmIndex in(listIndex):
            rdmIndex = alea(len(list_in) -1)
        resultat.append(list_in[rdmIndex])
        listIndex.append(rdmIndex)
    return resultat
        

#z = [5,1,2,3,4,9,4,7,5]
z = [1,2,3,4,5,6,7,8,9]
print(shuffle(z))