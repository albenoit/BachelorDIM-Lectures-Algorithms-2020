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

"""
Définition des variables globales
"""
my_score = 0
computer_score = 0
dice = [1, 2, 3, 4, 5, 6]

"""
Fonction qui vérifie si le score est égal à 1 ou non
param:
    score : integer, score qui représente le lancer de dé 
returns:

"""
def isScore1(score):



"""
Fonction qui illustre le tour d'un lancer de dé
param:
    player : bool, qui représente si True = joueur, False = ordinateur
returns:
    scoreTour : score accumulé pendant ce tour
"""
def tour(player):
    global my_score
    global computer_score
    score = shuffle(dice)
    scoreTour = score

    print(bcolors.MAGENTA + "--- PLAYER ---" + bcolors.ENDC) if player else print(bcolors.OKCYAN + "--- COMPUTER ---" + bcolors.ENDC)

    if (score == 1):
        print(bcolors.FAIL + "-------------------:(-------------------")
        print("Dé est égal à 1. Tour fini.")
        print("----------------------------------------" + bcolors.ENDC)
        scoreTour = 0
        return scoreTour

    print("Vous avez fait : " + str(score)) if player else print("Score IA : " + str(score))
    choice = input("Continuer ? y/n ") if player else shuffle(["y", "n"])
    while (choice == "y"):
        score = shuffle(dice)
        if (score == 1):
            print(bcolors.FAIL + "Dé = 1, tour fini" + bcolors.ENDC)
            scoreTour = 0
            return scoreTour
        scoreTour += score

        print("Vous avez fait : " + str(score)) if player else print("Score IA : " + str(score))
        choice = input("Continuer ? y/n ") if player else shuffle(["y", "n"])

    return scoreTour

def game(state):
    global my_score
    global computer_score

    if(state):
        player = True
        my_score += tour(player)
        return
    else:
        player = False
        computer_score += tour(player)
        return

print("----------------------------------------")
print("|              DICE GAME               |")
print("----------------------------------------\n")
state = True
while my_score <= 20 and computer_score <= 20:
    game(state)
    print(bcolors.OKGREEN + "\n---------------- SCORES ----------------")
    print("Mon score total " + str(my_score))
    print("Score total de l'IA " + str(computer_score))
    print("----------------------------------------\n" + bcolors.ENDC)
    state = not state
print("gagné")







