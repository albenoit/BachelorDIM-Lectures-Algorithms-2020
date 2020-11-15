# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:39:41 2020

@author: derbaghc
"""

from random import *

#https://stackoverflow.com/a/287944/13988436
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[35m'

"""
Fonction qui mélange un liste donnée - représente le lancé de dés
param:
    list_in : liste d'éléments
returns:
    list_in : renvoie la liste mélangée
"""
def shuffle(list_in:list):
    if isinstance(list_in, list):
        return list_in[randint(0, len(list_in)-1)]

player_score = 0
computer_score = 0
dice = [1, 2, 3, 4, 5, 6]

"""
Fonction qui illustre le tour d'un lancer de dé
param:
    state : bool, qui représente si True = joueur, False = ordinateur
returns:
    
"""
def tour(state):
    global player_score
    global computer_score
    score = shuffle(dice)
    scoreTour = score

    if(state):
        if (score == 1):
            print("dé est égal à 1")
            return
        print(bcolors.MAGENTA + "--- PLAYER ---" + bcolors.ENDC)
        choice = input("Vous avez fait : " + str(score) + " Continuer ? y/n ")
        while(choice == "y"):
            score = shuffle(dice)
            if(score == 1):
                print("1, tour fini")
                return
            scoreTour += score
            choice = input("Vous avez fait : " + str(score) + " Continuer ? y/n ")
        player_score += scoreTour
        return
    else:
        if (score == 1):
            print("dé est égal à 1")
            return
        print(bcolors.OKCYAN +"--- COMPUTER ---" + bcolors.ENDC)
        #0 = non , 1 = oui
        choice = shuffle([0, 1])
        while (choice == 1):
            score = shuffle(dice)
            if (score == 1):
                print("1, tour fini")
                return
            scoreTour += score
            print("Computer a fait " + str(score))
            choice = shuffle([0, 1])
        computer_score += scoreTour
        return

print("")
state = True
while player_score <= 20 and computer_score <= 20:
    tour(state)
    print("player score " + str(player_score))
    print("computer score " + str(computer_score))
    state = not state
print("gagné")







