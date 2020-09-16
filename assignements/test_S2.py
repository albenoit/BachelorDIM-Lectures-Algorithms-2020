# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:38:37 2020

@author: derbaghc
"""
def average_above_zero(table:list):
    """
    Fonction qui calcule la moyenne des valeurs d'un tableau donné, en 
    sélectionnant seulement les valeurs positives
    param:
        tab : tableau donné par l'utilisateur
    returns:
        average : moyenne avec les valeurs positives de tab
    """
    sum = 0
    n = 0
    tab_size = len(table)
    for x in range(0, tab_size):
        """Check if our value is positive"""
        if table[x]>0:
            sum += table[x]
            n += 1
    average = sum/n
    return average

def test_average(table):
    assert average_above_zero(1,2,3) == 2
   