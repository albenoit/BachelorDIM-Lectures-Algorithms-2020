# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:28:10 2020

@author: vibertvg
"""

my_array=[6,18]

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

moy=average_above_zero(my_array)
print('my average',moy)

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


max_val=max_value(my_array)
print('the max value is',max_val)


