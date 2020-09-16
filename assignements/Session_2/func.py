# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:15:49 2020

@author: vanhouta
"""


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