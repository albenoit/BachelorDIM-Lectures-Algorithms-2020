# -*- coding: utf-8 -*-
import numpy as np
from random import *

def average_above_zero(table:list):
    '''
        This function calcul average from number list
        Only number above zero is add to the average
        
        Parameters:
            table:list: the list of number .
        Returns: 
            the average of table:list
        Raises:
            If list is empty
            If no value abrove zero
    '''
    if(len(table)):
        Som = 0
        positif_element = 0
        for tableValue in table:
            if(tableValue>0):
                Som += tableValue
                positif_element+=1
        if(positif_element>0):
            Moy = Som/positif_element
        else:
            raise ValueError('No value abrove zero in the list')
        return(Moy)
    else:
        raise ValueError('List is empty')

def max_value(table:list):
    '''
        This function find the max value on a number list
        
        Parameters:
            table:list: the list of number.            
        Returns: 
            the max number on table:list
        Raises:
            If list is empty
    '''
    if(len(table)):
        Max = 0
        for tableValue in table:
            if(Max < tableValue):
                Max = tableValue
        return(Max)
    else:
        raise ValueError('List is empty')

def reverse_table(table:list):
    '''
        This function reverse a list
        
        Parameters:
            table:list: the list of number.            
        Returns: 
            reverse of table:list
        Raises:
            If list is empty
    '''
    if(len(table)):
        table.reverse()
        return table
    else:
        raise ValueError('List is empty')

def roi_bbox(input_image:np):
    '''
        This function find border of bounding box
        
        Parameters:
            input_image:np: array numpy.            
        Returns: 
            bounding box of input_image
        Raises:
            If input_image is empty
    '''
    if(len(input_image)):
        x1=len(input_image[0])           #nombre de lignes
        y1=len(input_image)             #nombre de colonnes
        x2=0
        y2=0
        bounding_box = np.zeros((4,2))
        position = np.argwhere(input_image)         #Trouve toutes les positions != 0
        if(len(position)):
            for c in position:
                x=c[0]
                y=c[1]
                if(x1>x):
                    x1=x
                if(y1>y):
                    y1=y
                if(x2<x):
                    x2=x
                if(y2<y):
                    y2=y
            bounding_box[0] = [x1,y1]           #Haut gauche
            bounding_box[1] = [x1,y2]           #Haut droit
            bounding_box[2] = [x2,y1]           #Bas gauche
            bounding_box[3] = [x2,y2]           #Bas droit
            return bounding_box
        else:
            raise ValueError('No value found')
    else:
        raise ValueError('Image is empty')


def random_fill_sparse(table:np, K:int):
    if (K<(len(table)*len(table[0]))):
        i=0
        while i<K:
            x=randint(0,len(matrix[0])-2)
            y=randint(0,len(matrix)-2)
            if((matrix[y,x])==0):
                matrix[y:(y+1),x:(x+1)] = randint(1, 255)
                i+=1
        return table
    else:
        raise ValueError('K abrove table size')


Tab=[2,54,-4]
print("Moyenne : " + str(average_above_zero(Tab)))
print("Max : " + str(max_value(Tab)))
print("Liste avant : "+ str(Tab))
print("Liste après : "+ str(reverse_table(Tab)))
'''
Tab = 3
print("Moyenne : " + str(average_above_zero(Tab)))
print("Max : " + str(max_value(Tab)))
print("Liste avant : "+ str(Tab))
print("Liste après : "+ str(reverse_table(Tab)))
'''
'''
H = 0
L = 0
matrix = np.zeros((H,L))
'''
H = 12
L = 10
matrix = np.zeros((H,L))

matrix[0:2, 7:9] = np.ones((2,2))
matrix[2:4, 3:5] = np.ones((2,2))*2

print(matrix)
print(roi_bbox(matrix))


matrix = np.zeros((H,L))

print(random_fill_sparse(matrix, 10))

