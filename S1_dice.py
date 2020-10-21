#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:34:05 2020

@author: carlitos
"""
from random import *

playerScore = 0
computerScore = 0


def ComputerThrow() :
    diceComputer = randint(1, 6)
    if(diceComputer==1) :
     return 0
    else :
     return diceComputer
  
    
    

while playerScore < 100 and computerScore <100:
    
    dice = 0
     
    
    print("Lancez le dée : y puis Entrez")  
    choice = input()
    if(choice =="y") :
     dice = randint(1,6)
     retry = True
     while retry :    
         print("valeur du dée : " + str(dice))  
         if(dice==1) :
            print("C'est un 1, 0 point et vous ne pouvez pas relancer") 
            break
         else :
             print("Voulez vous conserver ce lancer ? y/n")
             choice = input()
             if(choice =="y") :
                 playerScore = playerScore + dice
                 retry = False    
             else :
                 dice = randint(1,6)
         #print("Votre score est :" + str(playerScore))
     computerScore = computerScore + ComputerThrow()
     print("le score de l'ordinateur est : " + str(computerScore) + " le vôtre " + str(playerScore))
    
if(playerScore > computerScore) :
 print("Vous avez gagné !!!!")
else :
 print('Tu est mauvais')    
         
        

    
    