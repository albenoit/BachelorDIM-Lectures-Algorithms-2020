# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:14:06 2020

@author: bouvaran
"""


"""
Q1 : If "som" isn't initialized, the results adds up
Q2 : I have an error, I can't split by 0 
     "ZeroDivisionError: division by zero"
"""


tabMax = [1,2,3,4,5,6,7,8,9]
def average_above_zero(tabMax):
    som = 0
    n = 0
    
    for i in tabMax :
        if i > 0 :
            som += i
            n += 1
            
    Moy = som / n
    return float(Moy)

print(average_above_zero(tabMax))
