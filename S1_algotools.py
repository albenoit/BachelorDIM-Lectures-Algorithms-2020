# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:44:40 2020

@author: viardcrl
"""

import math;
import numpy as np
import random as rd
import test_S2

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 1 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 1------------\n',
      '----------------------------------\n')

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
    try:
        for i in table:
            if i > 0:
                Som += i;
                N += 1;
        Moy = math.floor(Som / N);
    except:
        raise Exception('Error : divide by zero is impossible')
    return Moy;

print('Average : ', average_above_zero([1,5,3,4,9,5]));

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 2 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 2------------\n',
      '----------------------------------\n')

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
    return table.index(max(table));

print('Index : ', max_value([1,5,3,4,9,5]));

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 3 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 3------------\n',
      '----------------------------------\n')

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
    return table[::-1];

print('Reversed Table : ', reverse_table([1,5,3,4,9,5]));

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 4 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 4------------\n',
      '----------------------------------\n')

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
    print('Numpy array :\n', input_image);
    
    row = np.any(input_image, axis=1);
    column = np.any(input_image, axis=0);
    
    rowMin, rowMax = np.where(row)[0][[0, -1]];
    columnMin, columnMax = np.where(column)[0][[0, -1]];
    
    return [columnMin, columnMax],[rowMin, rowMax];

print('\nCoordonates : ',roi_bbox(np.zeros((10,10), dtype=float)));

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 5 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 5------------\n',
      '----------------------------------\n')

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

print('Case number :',caseNumber);
print('Table : \n', random_fill_sparse(table,rd.randint(1,caseNumber)));

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 6 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 6------------\n',
      '----------------------------------\n')

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
    return sentence.replace(" ", "");

print('Sentence without space : \'', remove_whitespace('I love Python and Alexandre Benoit'), '\'');

#------------------------------------------------------------------------#
#------------------------------ EXERCISE 7 ------------------------------#
#------------------------------------------------------------------------#

print('\n ----------------------------------\n',
      '------------Exercise 7------------\n',
      '----------------------------------\n')

def shuffle(list_in:list):
    return list_in;

stuff = ['Baptiste', 'Car', 'Cutecumber']

print(shuffle(stuff));

