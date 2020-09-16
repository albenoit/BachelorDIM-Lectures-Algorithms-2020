# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:45:46 2020

@author: polletb
"""
import math
import numpy as np
import random

def average_above_zero(marks:list):
    '''
    Get average from list
    Parameters:
            marks: list float
    Returns :
        average of list
    '''
    average = 0  
    try :
        for i in marks:
            average += i
        
        average = math.floor(average / len(marks))
    except:
        raise Exception("Sorry average is null or equal 0") 
    
    return average

#Question 1 : la variable sum n'existe pas donc erreur
#Question 2 : erreur pas divisible par 0

#print(average_above_zero([10.0,20.0]))


def max_value(marks:list):
    '''
    Get max value of list
    Parameters:
            marks: list float
    Returns :
        max of list
    '''
    try:
       max_value = max(marks) 
       max_value_index = marks.index(max(marks))
    except:
        raise Exception("Sorry marks is null, empty")
    
    return max_value, max_value_index

#print(max_value([10.0, 20.0, 30.0]))
    

def reverse_table(table:list):
    '''
    Reverse an list
    Parameters:
            table: list
    Returns :
        list reverse
    '''
    try:
        #reverse_table = table[::-1]
        #or
        lenght = len(table)
        for i in range(lenght//2):
            tmp = table[i]
            endindex = lenght-i-1
            table[i] = table[endindex]
            table[endindex] = tmp
    except:
        raise Exception("Sorry table is null or empty")
        
    return table

#print(reverse_table([10,20,30,40]))
    
 
def roi_bbox(input_image:np):
    '''
    Get bouding box of numpy array with value equal 1
    Parameters:
            input_image: numpy
    Returns :
        input_image as numpy
        tuples with coords of min and max bounding box
    '''
    try:
        input_image[2:5, 2:5] = np.ones((3,3), dtype=float)
        
        row = np.any(input_image, axis=1)
        column = np.any(input_image, axis=0)
    
        rmin, rmax = np.where(row)[0][[0, -1]]
        cmin, cmax = np.where(column)[0][[0, -1]]
    except:
        raise Exception("Sorry numpy is null or empty")
        
    return  input_image, ([rmin, cmin], [rmax, cmax])

#print(roi_bbox(np.zeros((10,10), dtype=float)))
    

def alea(min:int, max:int):
    '''
    Get random number
    Parameters:
            min: int
            max: int
    Returns :
        alea_value as int
    '''
    try:
        alea_value = random.randint(min, max)
    except:
        raise Exception("alea_value is null or empty")
    return alea_value


def random_fill_sparse(table:np, K:int):
    '''
    Get random numpy with random X in
    Parameters:
            table: numpy
            K: int
    Returns :
        table as numpy
    '''
    try:
        for i in range(K):
            row = table[alea(0,len(table)-1)]
            row[alea(0,len(row)-1)] = 'X'
    except:
        raise Exception("table or K is null or empty")
    return table

#print(random_fill_sparse(np.empty((alea(1,10),alea(1,10)), dtype=str), 5))
    

def remove_whitespace(string_value:str):
    '''
    Remove whitespace in string
    Parameters:
            string_value: str
    Returns :
        string_value as str
    '''
    try:
        string_value.replace(" ","")
    except:
        raise Exception("string_value is null")
        
    return string_value

#print(remove_whitespace("Je suis une patate"))
    

def function_shuffle(list_in:list):
    '''
    Shuffle list
    Parameters:
            list_in: list
    Returns :
        list_in as list
    '''
    try:
        random.shuffle(list_in)
    except:
        raise Exception("list_in is null or empty")
    return list_in

print(function_shuffle([10,20,30,40,50]))