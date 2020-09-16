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
            
    if  n > 0  :  
        Moy = som / n
    else:
        raise ValueError("No positive value found")

    return Moy
print("Average : " + str(average_above_zero(theTab)))
'''
my_list=[0,2,-3]
average = average_above_zero(my_list)
print("T1 Average : " + str(average))

my_list=9
average = average_above_zero(my_list)
print("T2 Average : " + str(average))
'''
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

def roi_bbox():
    """
    This function return a Bounding box
    
    Parameters :
        npTab: tab of a numpy array
        answer: all the coordonates of "1" in npTab
    Returns : 
        the coordinates of "1" in npTab
    """
    h = 100
    w = 100
    x1=None
    y1=None
    x2=None
    y2=None
    npTab = np.zeros((h,w),dtype = float)
    
    #for w in range(45,55):
    #   for h in range(60,85):
    #       npTab(h,w) = 1
    # OU
    npTab[60:85,45:55] = np.ones((25,10),dtype = float)   
    
    """
    matrice = np.argwhere(npTab == 1)
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
    matrice = np.where(npTab == 1)
    x1 = np.min(matrice[1])
    y1 = np.min(matrice[0])
    x2 = np.max(matrice[1])
    y2 = np.max(matrice[0])

    return np.array([x1, y1, x2, y2])
print("Bounding box : " + str(roi_bbox()))


#////////////////////////////////////////////
def random_fill_sparse():
    """
    This function return an array with random X
    
    Parameters :
    Returns : 
    """
   
    k = 0
    
    
    return k
print("random_fill_sparse : " + str(random_fill_sparse()))
























