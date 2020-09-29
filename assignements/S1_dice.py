# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:29:13 2020

@author: tapiev
"""

def dicegame():
    score_pc = 0
    score_joueur=0
    gagnant ='pc'
    while score_pc<100:
        score_joueur += play_manche_joueur()
        if score_joueur>=100:
            gagnant = 'joueur'
            break
        score_pc += play_manche_pc()  
    print("test")
    

import random as random

def play_manche_pc():   
    
    print()

def play_manche_joueur():
    print()

def play_manche():
    print()
    
def lancer_le_de():
    return(random.randint(1,6))
    
import pyautogui as py
while(True):
    if py.keyDown("alt"):
        print("yo")