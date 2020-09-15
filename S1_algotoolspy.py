# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:45:46 2020

@author: polletb
"""
import math
import numpy as np


def average_above_zero(marks:list):
    '''
    Get average from list
    Parameters:
            marks: list float
    Returns :
        average of list
    '''
    average = 0    
    
    for i in marks:
        average += i
    
    average = math.floor(average / len(marks))
    return average

#Question 1 : la variable sum n'existe pas donc erreur
#Question 2 : erreur pas divisible par 0

#print(average_above_zero([10.0, 20.0]))


def max_value(marks:list):
    '''
    Get max value of list
    Parameters:
            marks: list float
    Returns :
        max of list
    '''
    return max(marks), marks.index(max(marks))

#print(max_value([10.0, 20.0, 30.0]))
    

def reverse_table(table:list):
    '''
    Reverse an list
    Parameters:
            table: list
    Returns :
        list reverse
    '''
    return table[::-1]

#print(reverse_table([10,20]))
 
##
#   \package algo_4
#   \autor polletb
#   \brief get 
#   \params @table = array
#
def roi_bbox(input_image:np):
    input_image[2:5, 2:5] = np.ones((3,3), dtype=float)
    
        
    return input_image

print(roi_bbox(np.zeros((10,10), dtype=float)))

