# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:28:10 2020

@author: vibertvg
"""

som=0
N=0
Tab=[12,18,6,20,14,5,6,3,18,10]
for i in Tab:
    if i > 0:
        som = som + i
        N = N + 1
Moy = som/N
print(Moy)