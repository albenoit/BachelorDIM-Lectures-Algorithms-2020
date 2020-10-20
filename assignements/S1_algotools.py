def my_addition(a,b):
    return (a+b)

def average_above_zero(table:list):
    '''
    This function calculate the average of a list of numbers
    
    Parameters :
        list : the list of numbers
    
    Return : 
        the average of the list

    Raises : 
        Value error if no positive value in the division
    '''
    som=0
    n=0
    for i in range(1, len(table)) :
        if (table[i] > 0):
            som = som + table[i]
            n = n + 1
        else:
            raise ValueError('No positive value in the division')
    moy = som/n
    return print(moy)

# liste = [8, 15, 14, 12, 6, 18, 10, 2, 20]
# average_above_zero(list)

# What happens if Som initialization is forgotten ?
# On a une erreur qui nous dit que Som n'est pas défini NameError: name 'som' is not defined

# What can you expect if all the values are below zero ?
# On a un message d'erreur qui nous dit qu'on ne peut pas diviser par 0 : ZeroDivisionError: division by zero
# Et on vérifie ça avec le if (p_list[i] > 0):

def get_maximum_value(table:list):
    '''
    This function found the max value of a list of numbers
    
    Parameters :
        list : the list of numbers
    
    Return : 
        the max value of a list and the position
    '''
    max=0
    rg=0
    for i in range(1, len(table)):
        if table[i] > 0 and table[i] > max:
            max = table[i]
            rg = i
    return print(float(max), int(rg))

# get_maximum_value(list)

def reverse_table(table:list):
    '''
    This function reverse a table
    Parameters :
        list : the list of numbers
    
    Return : 
        the table reverse
    '''

    return print(table[:: -1])

# reverse_table(list)

import numpy as np 

H=10
W=10
matrix=np.zeros((H,W), dtype=float)
matrix[2:4, 3:5]=np.ones((2,2), dtype=float)
for c in range(7,10):
    for l in range(7,10):
        matrix[l,c] = 1

def roi_bbox(img):

    '''
    This function return the bounding box coordinates of a matrix
    Parameters :
        img : the matrix
    
    Return : 
        the coordinates of the bounding box
    '''

    (x,y)=img.shape
    x1=x; y1=y; x2=0; y2=0
    for c in range(0,x):
        for l in range(0,y):
            if img[c,l]==1:
                l_temp = l
                c_temp = c
                if l_temp < x1:
                    x1 = l_temp
                if c_temp < y1:
                    y1 = c_temp
                if l_temp > x2:
                    x2 = l_temp
                if c_temp > y2:
                    y2 = c_temp

    return np.array([x1,y1,x2,y2])
# print(matrix)
# print(roi_bbox(matrix))

phrase = "phrase avec espaces"
def remove_whitespace(string):
    '''
        This function delete the spaces in a sentence
        Parameters:
            string: the sentence
        Returns:
            the sentence without wthitespace
    '''
    phrase2 = ""
    for i in string:
        if i != ' ':
            phrase2+=i
    return phrase2
# print(remove_whitespace(phrase))