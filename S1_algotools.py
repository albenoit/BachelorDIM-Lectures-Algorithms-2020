# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:44:40 2020

@author: viardcrl
"""

import math;

##
# \package mypackage
# \author me
# \brief A one-liner
# \details Lots and lots of lines of usage information
#
def average_above_zero(table:list):
    Som = 0;
    N = 0;
    
    for i in table:
        if i > 0:
            Som += i;
            N += 1;
    Moy = math.float(Som / N);
    return Moy;

print(average_above_zero([1,5,3,4,9,5]));