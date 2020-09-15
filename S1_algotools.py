# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:44:40 2020

@author: viardcrl
"""

import math;

##
# \package mypackage
# \author viardcrl
# \details returns the average of an array passed in parameter
#
# Question : What happens if Som initialization is forgotten ?
# UnboundLocalError: local variable 'Som' referenced before assignment
#
# Question : What can you expect if all the values are below zero ?
# AttributeError: module 'math' has no attribute 'float'
#
def average_above_zero(table:list):
    Som = 0;
    N = 0;
    
    for i in table:
        if i > 0:
            Som += i;
            N += 1;
    Moy = math.floor(Som / N);
    return Moy;

print(average_above_zero([1,5,3,4,9,5]));

##
# \package mypackage
# \author viardcrl
# \details returns the average of an array passed in parameter
#
# Question : What happens if Som initialization is forgotten ?
# UnboundLocalError: local variable 'Som' referenced before assignment
#
# Question : What can you expect if all the values are below zero ?
# AttributeError: module 'math' has no attribute 'float'
#
def max_value(table:list):
    return "Index :", table.index(max(table)), "Value :", max(table);

print(max_value([1,5,3,4,9,5]));