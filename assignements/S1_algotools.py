# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:14:06 2020
@author: bouvaran
"""
import numpy as np
import random

#////////////////////////////////////////////
"""
Q1 :If "som" isn't initialized, I have an error because the 
    variable have to be referenced before assignement
Q2 :I have an error, I can't split by 0 
    "ZeroDivisionError: division by zero"
"""
def average_above_zero(theTab:int):
    """
    This function calculates the average of the table
    
    Parameters :
        som: Contains the sum of the numbers in theTab
        n: contains the number of loops
    Returns :
        the average of theTab
    """
    som = 0
    n   = 0
    for i in theTab :
        if i > 0 :
            som += i
            n   += 1 
        elif i < 0:
            raise Exception("No positive value found")
        elif i == 0:
            raise ZeroDivisionError("You can't divide by zero",ZeroDivisionError)
        elif type(i) != "int" or i == None:
            raise TypeError("Not an integer",TypeError)
        
             
    Moy = som / n
    return Moy

#////////////////////////////////////////////
def max_value(theTab):
    """
    This function return the max value of the table
    
    Parameters :
        save: saves the highest number
    Returns :
        the highest number
    """
    save = 0
    
    for i in theTab :
        if i > save :
            save = i
    return save

#////////////////////////////////////////////
def reverse_table(theTab):
    """
    This function reverse the table
    
    Returns :
        the reverse of theTab
    """
    for i in range(len(theTab)//2):
        tmp            = theTab[i]
        endVal         = len(theTab)-i-1
        theTab[i]      = theTab[endVal]
        theTab[endVal] = tmp
    
    #return theTab[::-1]
    return theTab

#////////////////////////////////////////////
def roi_bbox(npTab:np.array):
    """
    This function return a Bounding box
    
    Parameters :
        npTab: tab of a numpy array
        matrice: all the coordonates of "1" in npTab
        x,y: the max and min coordonates
    Returns : 
        the coordinates max and min in x and y for 
        create a bounding box
    """
    #x1 = None
    #y1 = None
    #x2 = None
    #y2 = None
    
    #for w in range(45,55):
    #   for h in range(60,85):
    #       npTab(h,w) = 1
    # OU
    npTab[60:85,45:55] = np.ones((25,10),dtype = float)   
    
    """
    matrice    = np.argwhere(npTab == 1)
    for i in matrice:
        if x1 is None or i[0] < x1:
            x1 = i[0]
        if y1 is None or i[1] < y1:
            y1 = i[1] 
        if x2 is None or i[0] > x2:
            x2 = i[0] 
        if y2 is None or i[1] > y2:
            y2 = i[1] 
    """
    lx, ly = np.where(npTab != 0)
    if lx is None or ly is None:
        raise ValueError('X or Y is null')
    else:
        return np.array([
            [np.min(lx),np.min(ly)],
            [np.max(lx),np.max(ly)]
        ])

#////////////////////////////////////////////
def alea(mini,maxi):
    """
    This function generate a number

    Parameters :
        x: max number
    Returns :
        return random number
    """
    return random.randint(mini, maxi)

#////////////////////////////////////////////
def random_fill_sparse(table:np.array,k:int):
    """
    This function fill random cells with X

    Parameters :
        table: the empty table
        k: number of 'X'
    Returns :
        return array with random cells fill with X
    """
    for i in range(k):
        table[alea(0,table.shape[0]-1),alea(0,table.shape[1]-1)] = 'X'

    return table
    
#////////////////////////////////////////////
def remove_whitespace(phrase):
    """
    This function remove all the whitespace of a string

    Parameters :
        phrase: the string
    Returns :
        return string whitout whitespace
    """
    return phrase.replace(' ', '')

#////////////////////////////////////////////
def shuffle(list_in):
    """
    This function remove all the whitespace of a string

    Parameters :
        phrase: the string
    Returns :
        return string whitout whitespace
    """
    answer=[]
    for i in range(len(list_in)):
        random = alea(0,len(list_in)-1)
        answer.append(list_in[random])
        list_in.pop(random)
    return answer


#////////////////////////////////////////////
theTab = [1,2,3,4,5,6,7,8,9]
print("Average : "            + str(average_above_zero(theTab)))
'''
my_list=[0,2,-3]
average = average_above_zero(my_list)
print("T1 Average : " + str(average))
my_list=9
average = average_above_zero(my_list)
print("T2 Average : " + str(average))

'''
print("Max : "                + str(max_value(theTab)))
print("Reverse : "            + str(reverse_table(theTab)))
print("Bounding box : "       + str(roi_bbox(np.zeros([100,100],dtype = float))))
print("random_fill_sparse : " + str(random_fill_sparse(np.empty([alea(1,10),alea(1,10)], dtype=str), alea(1,10))))
print("remove_whitespace : "  + str(remove_whitespace("J'adore python, mettez moi 20, merci :D")))
print("shuffle : "            + str(shuffle(theTab)))


