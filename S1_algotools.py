# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:44:40 2020

@author: viardcrl
"""

import math;
import numpy as np

'''
    Question : What happens if Som initialization is forgotten ?
        UnboundLocalError: local variable 'Som' referenced before assignment
        La variable sum n'existe pas
    
    Question : What can you expect if all the values are below zero ?
        AttributeError: module 'math' has no attribute 'float'
        On ne peut pas diviser 0
'''
def average_above_zero(table:list):
    '''
    Calculate the sum of a list of integer
        package:
            math
        author:
            viardcrl
        Parameters:
            table: list of integer
        Returns:
            returns the average of an array passed in parameter
    '''
    Som = 0;
    N = 0;
    
    for i in table:
        if i > 0:
            Som += i;
            N += 1;
    Moy = math.floor(Som / N);
    return "Average :", Moy;

print(average_above_zero([1,5,3,4,9,5]));


def max_value(table:list):
    '''
        package:
            math
        author:
            viardcrl
        Parameters:
            table: list of integer
        Returns:
            returns the index and max value of an array passed in parameter
    '''
    return "Index :", table.index(max(table)), "Value :", max(table);

print(max_value([1,5,3,4,9,5]));


def reverse_table(table:list):
    '''
        package:
            math
        author:
            viardcrl
        Parameters:
            table: list of integer
        Returns:
            returns an inversed array
    '''
    return "Reversed Table :", table[::-1];

print(reverse_table([1,5,3,4,9,5]));


def roi_bbox(input_image:np):
    '''
        package:
            math, numpy
        author:
            viardcrl
        Parameters:
            input_image: 
        Returns:
            returns 
    '''
    input_image[2:5,2:5] = np.ones((3,3),dtype=float);
    return input_image;

print(roi_bbox(np.zeros((10,10), dtype=float)));

