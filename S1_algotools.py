# -*- coding: utf-8 -*-
import numpy as np

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

Tab=[2,54,-4]   #To use list.reverse(), I have change () to []
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
H = 12
L = 10
x1=255
y1=255
x2=0
y2=0
index = 0

matrix = np.zeros((H,L))
matrix[0:2, 7:9] = np.ones((2,2))
matrix[2:4, 3:5] = np.ones((2,2))*2
position = np.argwhere(matrix)
for c in position:
    if(x1>c[0]):
        x1=c[0]
    if(y1>c[1]):
        y1=c[1]
    if(x2<c[0]):
        x2=c[0]
    if(y2<c[1]):
        y2=c[1]        
bounding_box[0][0] = 11
print("bounding_box : " + str(bounding_box))
print("Ligne : " + str(x1) + " - colonne : " + str(y1))
print("Ligne : " + str(x2) + " - colonne : " + str(y2))
print(position[len(position)-1])
print(matrix)