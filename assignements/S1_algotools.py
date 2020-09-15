# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:14:06 2020
@author: bouvaran
"""

Thetab = [1,2,3,4,5,6,7,8,9]

#////////////////////////////////////////////
"""
Q1 :If "som" isn't initialized, I have an error because the 
    variable have to be referenced before assignement
Q2 :I have an error, I can't split by 0 
    "ZeroDivisionError: division by zero"
"""

def average_above_zero(Thetab):
    """@function average_above_zero
    som = Contains the sum of the numbers in Thetab
    n = contains the number of loops
    return = the average of Thetab
    """
    som = 0
    n = 0
    
    for i in Thetab :
        if i > 0 :
            som += i
            n += 1
            
    Moy = som / n
    return float(Moy)
print("Average : " + str(average_above_zero(Thetab)))


#////////////////////////////////////////////
def max_value(Thetab):
    """@function max_value
    save = saves the highest number
    return = the highest number
    """
    save = 0
    
    for i in Thetab :
        if i > save :
            save = i
            
    return save
print("Max : " + str(max_value(Thetab)))


#////////////////////////////////////////////
def reverse_table(Thetab):
    """@function reverse_table
    return = reverse Thetab
    """
    return Thetab[::-1]
print("Reverse : " + str(reverse_table(Thetab)))



























