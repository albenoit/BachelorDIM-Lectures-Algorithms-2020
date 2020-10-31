# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:44:40 2020

@author: viardcrl
"""

import math;
import numpy as np
import random as rd

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 1 ------------------------------#
#----------------------------UNIT TEST : DONE----------------------------#

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
    Som = 0
    N = 0
    
    for i in table:
        if i > 0:
            Som += i
            N += 1
        elif i < 0:
            raise Exception('Negative value')
        elif i == 0:
            raise ZeroDivisionError('Divide by zero is impossible', ZeroDivisionError)
        elif isinstance(i,int) == False and isinstance(i,float) == False:
            raise TypeError('It isn\'t an integer or a float', TypeError)
        elif i == None:
            raise TypeError('None value detected', TypeError)
    return math.floor(Som / N);

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 2 ------------------------------#
#----------------------------UNIT TEST : DONE----------------------------#

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
    for value in table:
        if value == None:
            raise TypeError('None value detected', TypeError)
        elif isinstance(value,int) == False and isinstance(value,float) == False:
            raise TypeError('It isn\'t an integer or a float', TypeError)
    return table.index(max(table))

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 3 ------------------------------#
#----------------------------UNIT TEST : DONE----------------------------#


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
    for value in table:
        if value == None:
            raise TypeError('None value detected', TypeError)
        elif isinstance(value,int) == False and isinstance(value,float) == False:
            raise TypeError('It isn\'t an integer or a float', TypeError)
    return table[::-1];

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 4 ------------------------------#
#----------------------------UNIT TEST : FALSE---------------------------#

def roi_bbox(input_image:np.array):
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
    
    row = np.any(input_image, axis=1);
    column = np.any(input_image, axis=0);
    
    rowMin, rowMax = np.where(row)[0][[0, -1]];
    columnMin, columnMax = np.where(column)[0][[0, -1]];
    
    return [columnMin, rowMin],[columnMax, rowMax];

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 5 ------------------------------#
#----------------------------UNIT TEST : FALSE---------------------------#

def random_fill_sparse(table:np.array, K:int):
    '''
        package:
            math, numpy, random
        author:
            viardcrl
        Parameters:
            table:np.array
            K:int
        Returns:
            returns 
    '''
    
    print('X number :', K);
    xNumber = 0;
    while(xNumber < K):
        row = table[alea(0,len(table)-1)];
        randomNumber = alea(0, len(row)-1);
        if(row[randomNumber] == 'X'):
            pass
        else:
            row[randomNumber] = 'X';
            xNumber += 1;
    return table;

def alea(xMin:int, xMax:int):
        return rd.randint(xMin, xMax);

table = np.empty((alea(1,10), alea(1,10)), dtype=str);

caseNumber = 0;
for row in table:
    for column in row:
        caseNumber += 1;

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 6 ------------------------------#
#----------------------------UNIT TEST : FALSE---------------------------#

def remove_whitespace(sentence:str):
    '''
        package:
            math, numpy, random
        author:
            viardcrl
        Parameters:
            table:np.array
            K:int
        Returns:
            returns 
    '''
    return sentence.replace(" ", "")

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 7 ------------------------------#
#------------------------------------------------------------------------#

def shuffle(list_in:list):
    rd.shuffle(list_in)
    return list_in

stuff = ['Baptiste', 'Car', 'Cutecumber']