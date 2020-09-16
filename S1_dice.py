# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:38:43 2020

@author: albentmp
"""

from random import *

def shuffle():
    pointA = 0
    pointB = 0
    while (pointA <100 and pointB <100):
        de = 0
        temp = 0
        while (de != 1 and strUser != "n"):
            de = randint(0,6)
            temp += de
            input("Score temporaire",temp,".Le garder? (o/n)")
        if(de != 1):
            pointA += temp
        temp = 0
            
            