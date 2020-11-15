# -*- coding: utf-8 -*-

import numpy as np
import cv2
import random

"""
Session 1 Averaging

"""
"""
Questions
What happens if Som initialization is forgotten ?
    It will return an error

What can you expect if all the values are below zero ?
    It will return an error because it's impossible to divide by negative value

Translate this algorithm in the python3.x language within script of name:

"""

def average_above_zero(tab):
    '''
    This function give the average of positive values
    Parameters:
        tab: table of positive number
    Returns: average
    Raises: error if no positive values in tab
    '''
    som = 0
    n = 0
    for i in tab:
        if i > 0:
            som = som + i
            n = n + 1
    if n > 0:
        moy = som / n
    else:
        raise ValueError('impossible de diviser par zero')
    return moy

print('\nAverage above 0 : {0}'.format(average_above_zero([10, 2]))+ "\n")


"""
Session 1 Table maximum value
Propose changes on the previous algorithm to get the maximum value of
a table.

"""

def max_value_without_index(tab):
    '''
    This function return the highest value finded in a list
    Parameters:
        tab: list of number
    Returns: max value
    '''
    Max = 0
    for i in tab:
        if i > Max:
            Max = i
    return Max

print('Max value without index : {0}'.format(max_value_without_index([1,2,3,10]))+ "\n")

"""

Improve the previous changes by capturing the index of the last maximum value.

"""

def max_value(Tab):
    '''
    This function return the highest value finded in a list
    Parameters:
        Tab: list of number
    Returns: max value and his index
    '''
    Max = 0
    N = 0
    Index = 0
    for i in Tab:
        if i > Max:
            Max = i
            Index = N
        N += 1

    return (Max, Index)


print('Max value with index : {0}'.format(max_value([8, 3, 15])) + "\n")

"""
Session 1 Reverse a table 

"""

def reverse_table(tab):
    '''
    This function reverse a table
    Parameters:
        Tab: table of number
    Returns: the reversed table
    '''

    listlen = len(tab)
    for i in range(listlen // 2):
        tmp = tab[i]
        endid = listlen - i - 1
        tab[i] = tab[endid]
        tab[endid] = tmp
    return tab

print('Reverse table : {0}'.format(reverse_table([1, 2, 3, 4, 5, 6, 7, 8]))+ "\n")


"""
Session 1 Bounding box

"""
H = 1000
W = 1000
n = np.zeros((H, W), dtype=np.uint8)
n[45:200, 70:91] = 1

def find_top_y(matrix):
    for y in range(matrix.shape[0]):
        if np.sum(matrix[y, :]):
            return y
    raise ValueError("no non null value found")


def find_top_x(matrix):
    for x in range(matrix.shape[1]):
        if np.sum(matrix[:, x]):
            return x
    raise ValueError("no non null value found")


def find_down_y(matrix):
    for y in range(matrix.shape[0])[::-1]:
        if np.sum(matrix[y, :]):
            return y
    raise ValueError("no non null value found")


def find_down_x(matrix):
    for x in range(matrix.shape[1])[::-1]:
        if np.sum(matrix[:, x]):
            return x
    raise ValueError("no non null value found")


def roi_bbox(image):
    '''
    This function return a numpy array with the coord of a bounding box
    Parameters:
        image: numpy array
    Returns: numpy array with 4 coordinates
    '''
    return np.array([find_top_x(image), find_top_y(image), find_down_x(image), find_down_y(image)])

print('Bounding Box : {0}'.format(roi_bbox(n))+ "\n")


"""
Session 1 Random array filling 

"""

def fill_a_rand_cell(table):
    coord = (random.randint(0, table.shape[0] - 1), random.randint(0, table.shape[1] - 1))
    if table[coord] == "":
        table[coord] = "X"
    else:
        table = fill_a_rand_cell(table)
    return table

n = np.full((20, 20), [""], dtype=str)


def random_fill_sparse(table, K):
    '''
    This function return a numpy array with random cross in the array
    Parameters:
        table: an empty table
        K: number of cross
    Returns: the table with crosses inside
    '''
    numberofcase = table.shape[0] * table.shape[1]
    if numberofcase > K:
        for x in range(K):
            table = fill_a_rand_cell(table)
    else:
        raise ValueError("too much cross for the table")
    return table

print('Random fill sparse : \n {0}'.format(random_fill_sparse(n, 10))+ "\n")

"""

#Session 1 Remove whitespace in string

"""

def remove_whitespace(str):
    '''
    This function return a string without whitespace
    Parameters:
        table: str string
    Returns: the string without whitespace
    '''
    if len(str) == 0:
        raise ValueError('expected a non empty string')

    strReturn=""
    for i in str:
        if i != ' ':
            strReturn += i  
            
    return(strReturn)

print('Remove white space : {0}'.format(remove_whitespace("A L G O I S G O O D"))+ "\n")


"""
Session 1 Random item selection 

"""

def shuffle(tab):
    '''
    This function randomize index of values in table
        tab: a table
    Returns: the string randomized
    '''
    listlen = len(tab)
    for i in range(listlen):
        tmp=tab[i]
        pos=random.randint(0,listlen-1)
        tab[i] = tab[pos]
        tab[pos]=tmp
 
    return tab

print('Shuffle list : {0}'.format(shuffle([1,"hello",7,10]))+ "\n")


"""
Session 1 Selection Sort

"""

def sort_selective(list):
    '''
    This function sort value in ascending order
    Parameters:
        table: table of integer
    Returns: the table sorted ascendingly
    '''   

    for i in range(len(list)):
       min_index = i
       for j in range(i+1, len(list)):
           if list[min_index] > list[j]:
               min_index = j
                     
       temp = list[i]
       list[i] = list[min_index]
       list[min_index] = temp

    return list

print('Selective Sort : {0}'.format(sort_selective([10,15,7,1,3,3,9]))+ "\n")

"""
Questions :
    b- Yes, the more the vector will be longer more the number of iternation will be important 
    c- As many as there is number in the list
    d- As many as there is number in the list
    e- The number of item squared
    f- it's a difficulty of list squared

"""

"""
Session 1 Bubble Sort

"""
def sort_bubble(list):
    '''
    This function sort value in ascending order
    Parameters:
        table: table of integer
    Returns: the table sorted ascendingly
    ''' 

    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

print('Bubble Sort : {0}'.format(sort_bubble([10,15,7,1,3,3,9]))+ "\n")

"""
Questions :
    b- Yes, the more the vector will be longer more the number of permutation will be important  
    c- As many as permutation is needed
    d- As many needed until the value of every entry is lower than the next entry
    e- As many as there is iteration
    f- The list squared

"""