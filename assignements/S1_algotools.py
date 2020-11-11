#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14/09/2020

@author: fchambon
"""

import numpy as np
import random

a=1
# b='e'+a


def average_above_zero(nbr_list):
    '''
    Makes an average with all numbers above 0 provided by the nbr_list table
    
    Parameters:
        nbr_list: the table that have numbers

    Returns: the calculated sum of all numbers in the list
    '''

    sum = 0
    n = 0

    for i in range(len(nbr_list)):
        if nbr_list[i] > 0:
            sum = sum + nbr_list[i]
            n = n + 1

    moy = sum / n
    return moy

def max_value(nbr_list):
    '''
    Gets the last biggest number index

    Parameters:
        nbr_list: the table that have numbers

    Returns: index of last biggest number
    '''

    idx = -1
    big_value = -1
    
    for i in range(len(nbr_list)):
        if(nbr_list[i] > big_value):
            idx = i
            big_value = nbr_list[i]
    
    return idx

def reverse_table(nbr_list):
    '''
    Reverse table order

    Parameters:
        nbr_list: the table that have numbers

    Returns: the reversed table
    '''

    rvrsd_table = []

    for i in range(len(nbr_list), 0, -1):
        rvrsd_table.append(nbr_list[i-1])

    return rvrsd_table

def roi_bbox(mtrx):
    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1
    foundX1 = False

    for i in range(len(mtrx)): # ligne
        foundY1 = False
        for j in range(len(mtrx[i])): # col
            if mtrx[i, j] > 0:
                if not foundX1:
                    x1 = j
                    foundX1 = True
                else:
                    x2 = j

                if not foundY1:
                    y1 = i
                    foundY1 = True
                else:
                    y2 = i
                
            # print(mtrx[i, j])
    return x1, y1, x2, y2

def roi_bbox_2(mtrx):
    '''
    Finds the bounding box of an array

    Parameters:
        mtrx: The matrix of 0 and 1

    Returns: The coordinates of all corners
    '''

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    # top left
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if mtrx[i, j]:
                x1 = j
                y1 = i
                break

    # top right
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            if mtrx[i, j]:
                x2 = j
        break

    # bottom left
    for i in range(len(mtrx), 0, -1):
        for j in range(len(mtrx[i-1])):
            if mtrx[i-1, j]:
                if i-1 > y1:
                    x2 = j
                    y1 = i-1
                    
                break

    # bottom right
    for i in range(len(mtrx), 0, -1):
        for j in range(len(mtrx[i-1]), 0, -1):
            if mtrx[i-1, j-1]:
                if j-1 > x1:
                    x2 = j-1
                    y2 = i-1
                    
        break

    return x1, y1, x2, y2

def alea(max):
    '''
    Returns a random number between 0 and max

    Parameters:
        max: Integer

    Returns: Random number defined by max
    '''
    return random.randrange(0, max)

def random_fill_parse(mtrx, nbr):
    '''
    Fill matrix at random positions with random values only when cell is empty

    Parameters:
        mtrx: The empty matrix
        nbr: The number of iteration

    Returns: An array filled with random numbers at random positions
    '''

    i=0

    if nbr > mtrx.size:
        print("Erreur: Le nombre est trop grand par rapport à la taille de la matrice.")
        return

    while i < nbr:
        rdmX = alea(len(mtrx[0]))
        rdmY = alea(len(mtrx))

        if mtrx[rdmY, rdmX] <= 0:
            mtrx[rdmY, rdmX] =  alea(100)
            i=i+1
            
    return mtrx

def remove_whitespace(strlist):
    if type(strlist) is list:
        for i in range(0, len(strlist)):
            strlist[i] = strlist[i].strip()

    return strlist

def shuffle(shuffleList):
    shuffledList = []
    if type(shuffleList) is list:
        for i in range(0, len(shuffleList)):
            pick = random.randint(0, len(shuffleList) - 1)
            shuffledList.append(shuffleList[pick])
            shuffleList.pop(pick)
    return shuffledList


# nbr_list = [1, -5, 3]
# h = 12
# w = 10
# mtrx = np.zeros((h, w))
# mtrx[0:1, 3:5] = np.ones(1)
# mtrx[2:5, 1:3] = np.ones(1)
# mtrx2 = np.zeros((h, w))
wsarray = [" test", "test2 ", "   test3  "]
shufflearray = [0,1,2,3,4,5,6,7,8,9]

# print('Average of list is: ' + str(average_above_zero(nbr_list)))
# print('Max biggest number index is: ' + str(max_value(nbr_list)))
# print('Reversed table is: ' + str(reverse_table(nbr_list)))
# print('Bounding box of matrix is: ' + str(roi_bbox_2(mtrx)))
# print(random_fill_parse(mtrx2, 121))
# print(mtrx2.size)
# print("wsarray without whitespace is: " + str(remove_whitespace(wsarray)))
print("Randomized optimized array: " + str(shuffle(shufflearray)))