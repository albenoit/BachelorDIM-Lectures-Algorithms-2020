# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:14:06 2020

@author: bouvaran
"""

som = 0
n = 0
tabMax = [1,2,3,4,5,6,7,8,9]

for i in tabMax :
    if i > 0 :
        som += i
        n += 1
        
Moy = som / n
print(Moy)
