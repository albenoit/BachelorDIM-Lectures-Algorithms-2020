# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:45:46 2020

@author: polletb
"""
import math
##
#   \package algo_1
#   \autor polletb
#   \brief get average from array
#   \params @marks = array
#
def average_above_zero(marks:list):
    average = 0    
    
    for i in marks:
        average += i
    
    average = math.floor(average / len(marks))
    return average

#Question 1 : la variable sum n'existe pas donc erreur
#Question 2 : erreur pas divisible par 0


#print(average_above_zero([10.0, 20.0]))

def max_value(marks:list):
    return max(marks)

#print(max_value([10.0, 20.0, 30.0]))
    

def reverse_table(table:list):
    return table[::-1]

print(reverse_table([10,20]))