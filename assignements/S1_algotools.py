# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:14:06 2020
@author: bouvaran
"""

theTab = [1,2,3,4,5,6,7,8,9]

#////////////////////////////////////////////
"""
Q1 :If "som" isn't initialized, I have an error because the 
    variable have to be referenced before assignement
Q2 :I have an error, I can't split by 0 
    "ZeroDivisionError: division by zero"
"""

def average_above_zero(theTab):
    """
    This function calculates the average of the table
    
    Parameters :
        som: Contains the sum of the numbers in theTab
        n: contains the number of loops
    Returns :
        the average of theTab
    """
    som = 0
    n = 0
    
    for i in theTab :
        if i > 0 :
            som += i
            n += 1
            
    Moy = som / n
    return float(Moy)
print("Average : " + str(average_above_zero(theTab)))


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
print("Max : " + str(max_value(theTab)))


#////////////////////////////////////////////
def reverse_table(theTab):
    """
    This function reverse the table
    
    Returns :
        the reverse of theTab
    """
    return theTab[::-1]
print("Reverse : " + str(reverse_table(theTab)))


#////////////////////////////////////////////
import numpy as np

def roi_bbox(theTab):
    """
    This function return a Bounding box
    
    Parameters :
        npTab: tab of a numpy array
    Returns : 
        the coordinates of "1" in npTab
    """
    npTab = np.array([
            [1,0,1],
            [0,1,0],
            [1,0,1]
        ])
    
    answer = np.argwhere(npTab == 1)
    
    return answer
print("Bounding box : " + str(roi_bbox(theTab)))


#////////////////////////////////////////////














