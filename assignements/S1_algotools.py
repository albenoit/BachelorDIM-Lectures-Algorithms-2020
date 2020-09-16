# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:04 2020

@author: cuvellin
"""
import numpy as np

def average_above_zero(list_of_numbers):
    '''
    One will to compute the average of the positive elements of a table.
    
    Parameters:
        list_of_numbers
    Raise:
        Can call a raise ValueError if n == 0
    Returns:
        average of the positive elements of a table 
    '''
    n = 0
    som = 0
    sizeArray = len(list_of_numbers)
    for i in range(sizeArray):
        if list_of_numbers[i] > 0:
            som += list_of_numbers[i]
            n = n +1
    if (n != 0):
        moy = som / n
    else:
        raise ValueError('ZeroDivisionError')
    return float(moy)

def max_value(array):
    '''
    get the max value in array put in params
    
    Parameters:
        array
    Returns:
        max value in array put in params
    '''
    max = None
    for i in array:
        if max is None or i > max:
            max = i
            
    return max
        

def reverse_table(tab):
    '''
    reverse a table without the use of any other table
    
    Parameters:
        tab
    Returns:
        reverse of tab put in params
    '''
    listlen = len(tab)
    
    for i in range(len(tab)//2):
        tmp = tab[i]
        endid = listlen-i-1
        tab[i] = tab[listlen-1]
        tab[i] = tab[endid]
        tab[endid] = tmp
    return tab

def roi_bbox(input_image):
    '''
    algorithm able to compute the bounding box coordinates of the object
    
    Parameters:
        input_image as numpy tab
    Returns:
        a numpy array of shape 4x1 filled with the four 2D coordinates
    '''
    matrix_found_bb = np.where(matrix_bounding_box > 0)
    
    x1 = matrix_found_bb[0][0]
    y1 = matrix_found_bb[1][0]
    x2 = matrix_found_bb[0][len(matrix_found_bb[0])-1]
    y2 = matrix_found_bb[1][len(matrix_found_bb[1])-1]
    
    return np.array([x1,y1,x2,y2])
     

Tab = [4,2,45,-4,14,-95,-4,2,87,-56,65,1,3]
print(average_above_zero(Tab))

print(reverse_table([1,2,3,4,5]))


print(max_value([8,9,7, -9]))

matrix_bounding_box = np.array([[0,0,1,1,0,0,0,0,0,0],
                                [0,0,1,1,0,0,0,0,0,0],
                                [0,0,0,0,0,1,1,0,0,0],
                                [0,0,0,0,0,1,1,0,0,0],
                                [0,0,0,0,0,0,0,0,0,0]])

print(roi_bbox(matrix_bounding_box))
