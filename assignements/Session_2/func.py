# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:15:49 2020

@author: vanhouta
"""
import numpy as np

def plusone(x):
    return x+1

def addition(a,b):
    return a+b

def average_above_zero(table:list):
    Som = 0 
    ## @var _Som
    # Sum of all number
    N = 0
    ## @var _N
    # Length of the table
    for i in range (1,len(table)):
        if(table[i] > 0):
            Som += table[i]
            N += 1
    if(N > 0):
        Moy = Som/N
    else:
        raise ValueError("no positive value in the table")
    return Moy

def maximum_value(table:list):
    '''
        This function find the highest value in the list
        Args:
            table: list of number
        Returns the maximum value of a list
    '''
    maxValue = float('-inf')
    index = 0
    for i in range (1,len(table)):
        if(table[i] > maxValue):
            maxValue = table[i]
            index = i+1
    return maxValue,index

def reverse_table(table:list):
    '''
        This funcion return a reversed list
        Args:
            table: list of number you want to reverse
        Returns the reversed list
    '''
    return table[::-1]

def roi_bbox(img):
    '''
        This funcion compute bounding box coordinates of an object
        Args:
            img: Binary image
        Returns the bounding box in numpy array
    '''
    (y,x)=img.shape
    x1 = x
    y1 = y
    x2 = 0
    y2 = 0
    for yImg in range(0,y):
        for xImg in range(0,x):
            if(img[yImg,xImg] == 1):
#                null = 0
#            elif(img[yImg,xImg] == 1 and null == 0):
                if(xImg < x1):
                    x1 = xImg
                if(yImg < y1):
                    y1 = yImg
                if(xImg > x2):
                    x2 = xImg
                if(yImg > y2):
                    y2 = yImg
    
                
    return np.array([x1,y1,x2,y2])






















