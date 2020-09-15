# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:44:40 2020

@author: viardcrl
"""

import math;

##
# \package math
# \author viardcrl
# \details returns the average of an array passed in parameter
#
# Question : What happens if Som initialization is forgotten ?
# UnboundLocalError: local variable 'Som' referenced before assignment
# La variable sum n'existe pas
#
# Question : What can you expect if all the values are below zero ?
# AttributeError: module 'math' has no attribute 'float'
# On ne peut pas diviser 0
#
def average_above_zero(table:list):
    Som = 0;
    N = 0;
    
    for i in table:
        if i > 0:
            Som += i;
            N += 1;
    Moy = math.floor(Som / N);
    return "Average :", Moy;

print(average_above_zero([1,5,3,4,9,5]));

##
# \package math
# \author viardcrl
# \details returns the index and max value of an array passed in parameter
#
def max_value(table:list):
    return "Index :", table.index(max(table)), "Value :", max(table);

print(max_value([1,5,3,4,9,5]));

##
# \package math
# \author viardcrl
# \details returns the index and max value of an array passed in parameter
#
def max_value(table:list):
    return "Reversed Table :", table[::-1];

print(max_value([1,5,3,4,9,5]));