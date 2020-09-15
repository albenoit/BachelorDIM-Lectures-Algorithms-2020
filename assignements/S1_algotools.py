list = [12, 14, 16, 17, 18]

def average_above_zero(table:list):
    '''
        This function calculate the average of a list 
        Parameters:
            table: List of number
        Returns:
            the average
        Raises:
            Value error if no positive value n
    '''
    som=1
    n=0
    for i in range(1, len(table)):
        if table[i] > 0:
            som = som + table[i]
            n = n + 1
    if n > 0:
        Moy = som/n
        return print(float(Moy))
    else:
        raise ValueError('no positive value n')

average_above_zero(list)

# What happens if Som initialization is forgotten ?

# On a le message d'erreur: NameError: name 'som' is not defined. 
# Celle-ci signifie que la variable som n'est pas défini avant d'etre utilisé 


# What can you expect if all the values are below zero ?

#  On a le message d'erreur: ZeroDivisionError: division by zero
# Cela arrive quand l'on ne rentre pas dans la condition p_list[i] > 0 et donc que n reste nulle 


def max_value(table:list):
    '''
        This function search the maximum value of a list
        Parameters:
            table: List of number
        Returns:
            the maximum value of a list
    '''
    max_nb=0
    max_id=0
    for i in range(1, len(table)):
        if table[i] > 0 and table[i] > max_nb:
            max_nb = table[i] 
            max_id = i
    return print(float(max_nb),int(max_id))


max_value(list)


def reverse_table(table:list):
    '''
        This function reverse a list
        Parameters:
            table: List of number
        Returns:
            a reverse list
    '''

    return print(table[:: -1])


reverse_table(list)

import numpy as np

def roi_bbox(input_image:np array):
    W=10
    H=10
    Xin = np.zeros((H,W),dtype=float)
    for c in range(7,12):
        for l in range(7,9):
            Xin[l,c]=1
roi_bbox(10,10)