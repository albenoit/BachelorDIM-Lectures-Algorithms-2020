# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:38:43 2020

@author: albentmp
"""

from random import *

def shuffle():
    pointA = 0
    pointB = 0
    tour = 0
    lON = ['o','n']
    
    while (pointA <100 and pointB <100):
        de = 0
        temp = 0
        strUser = ""
        tour += 1

        while (de != 1 and strUser != "n"):
            de = randint(1,6)
            temp += de
            print("Dé : ",de)

            if(de != 1):
                if (tour % 2 != 0):
                    #Humain
                    strUser = ""
                    while(strUser not in lON):
                        strUser = input("Score temporaire: " + str(temp) + ".Relancer? (o/n)")
                    if(strUser == 'n'):
                        pointA += temp
                else:
                    #Bot
                    strUser = "o"
                    print("Score temporaire: " + str(temp))
                    if(randint(0,1)):
                        print("Le bot relance")
                    else:
                        strUser = "n"
                        print("Le bot s'arrête")
                        pointB += temp
            else:
                print("Le dé affiche 1. Vous ne gagnez pas de point.")
                
        print("-------------------------")
        print("Score joueur :" + str(pointA))
        print("Score bot :" + str(pointB))
        print("-------------------------")

        
    if(pointA > 100):
        print("Humain a gagné")
    else:
        print("Bot a gagné")

shuffle()

