# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:28:10 2020

@author: vibertvg
 """
import numpy as np

my_array=[-5,-10,0]

def average_above_zero(array_of_data):
    """
        Function who work with an array of numbers greater than 0
        Parameters:
            som: the addition of all number average
            N: the number of iterations (équivalant to the size of the array)
            Moy: the sum of all numbers divided by the number of itérations
        Returns:
            The average calculated with the variable Moy
    """
    som=0
    N=0
    for i in array_of_data:
        if i > 0:
            som = som + i
            N = N + 1
    if N > 0:
        Moy = som/N
    else:
        raise ValueError('problem, a number is equivalent or under 0')
    return float(Moy)


"""

moy=average_above_zero(my_array)
print('my average',moy)

"""

"""
    What happens if Som initialization is forgotten ?
        The variable 'som' do not reset for each time you press the run button
        local variable 'som' referenced before assignment
        
    What can you expect if all the values are below zero ? 
        We cant divide by zero. It will make an error
"""

def max_value(array_of_data):
    """
        Function who work with an array of numbers greater than 0
        Parameters:
            N: the number of iterations (équivalant to the size of the array)
        Returns:
            highest_number: the max value of the array is returned as float
    """
    N=0
    highest_number=0
    for i in array_of_data:
        if i > 0:
            N += 1
            if i > highest_number:
                highest_number = i
    if N < 0:
        raise ValueError('problem, a number is equivalent or under 0')
    return float(highest_number)

"""
max_val=max_value(my_array)
print('the max value is',max_val)
"""




def reverse_table(array_of_data):
    """
        Function who reverse the array given (using function array[::-1])
        Parameters:
            array_of_data: array given by the user not reversed
        Returns:
            res: array of data reversed
    """
    res = array_of_data[::-1]
    return list(res)
  
"""
table_not_revesed=my_array
table_reversed=reverse_table(my_array)
print('Array not reversed is :',table_not_revesed)  
print('Array reversed is :',table_reversed)   
"""    



def create_image_matrice(rows,cols):
    """
        Function who create a matrice of 0
        Parameters:
            rows: size of rows (int) both given by the user
            cols: size of cols (int)
        Returns:
            mat: matrice returned created filled only with 0
    """
    mat=np.zeros((rows,cols),dtype=int)
    return mat


def add_ones_to_matrice(mat,x1,x2,y1,y2):
    """
        Function who add 1 in a matrice already created
        Parameters:
            x1: first point x who significate the beginning of number 1 création
            y1: first point y who significate the beginning of number 1 création
            x2: second point x who end the création of ones
            y2: second point x who end the création of ones
            size_x: Size x of number 1 matrice 
            size_y: Size y of number 1 matrice 
        Returns:
            mat: matrice returned created filled with 1
    """
    size_x = x2 - x1
    size_y = y2 - y1
    mat[y1:y2,x1:x2]=np.ones((size_y,size_x))
    return mat


"""
matrice = create_image_matrice(6,6)
matrice=add_ones_to_matrice(matrice,2,4,2,6)
print(matrice)
"""
"""
def roi_bbox(mat):
    
    for x in range(mat.shape[1]):
        for y in range(mat.shape[0]):
            print(mat[y,x])
    return 0
    
roi_bbox(matrice)
"""