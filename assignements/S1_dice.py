# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:18:16 2020

@author: bouvaran
"""
import random as rdm

#////////////////////////////////////////////
class TheDice(listIn):
    
    def Init():
        gameStart      = False
        round_hu_comp  = 0
        human_score    = 0
        computer_score = 0
        winner_score   = 100
        
    def alea(mini,maxi):
        return random.randint(mini, maxi)
        
    def Menue(gameStart):
        if gameStart == False:
            print("Welcome to the dice game")
            print("Do you want to play ? y / n ")
            
            if input() == y:
                print("Let's go !")
                gameStart = True
            else:
                print("ok, bye")
                quit()
                
    def Round():
        if round_hu_comp == 0:
            print("human round")
            #human_score
            round_hu_comp = 1
        else : 
            print("computer round")
            #computer_score
            round_hu_comp = 0
        return 1
    
    def Start(gameStart):
        if gameStart == True:
            print("Paf")  
        else:
            raise ValueError("Error, the game can't start")
