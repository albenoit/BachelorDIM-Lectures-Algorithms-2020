# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:04 2020

@author: cuvellin
"""

Tab = [4,2,45,-4,14,-95,-4,2,87,-56,65,1,3]

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

def reverse_table(array):
    '''
    reverse a table without the use of any other table
    
    Parameters:
        array
    Returns:
        reverse of array put in params
    '''
    return array[::-1]

print(average_above_zero(Tab))

print(reverse_table([1,2,3,4,5]))
        