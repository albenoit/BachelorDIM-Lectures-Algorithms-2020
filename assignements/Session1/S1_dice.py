# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:39:41 2020

@author: derbaghc
"""

def alea(n):
    """
    Fonction qui encadre une zone définie de 1
    param:
        n : nombre de chiffres que l'on veut générer et max de la valeur (non 
        incluse)
    returns:
        z : coordonées de la forme encadrant les 1
    """
    return randint(1, n)

def game(tab_user):
    for i in range(len(tab_user)):
        alea(6)
        
