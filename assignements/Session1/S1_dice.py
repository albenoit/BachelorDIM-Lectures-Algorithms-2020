# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:39:41 2020

@author: derbaghc
"""

from random import *

"""
Fonction qui mélange un liste donnée
param:
    list_in : liste d'éléments
returns:
    list_in : renvoie la liste mélangée
"""
def shuffle(list_in:list):
    if isinstance(list_in, list):
        return list_in[randint(0, len(list_in)-1)]

#print(shuffle([1, 2, 3, 4, 5, 6]))
"""
Fonction qui regarde si le joueur/computer a gagné
param:
    player_score : integer
    tour : integer
returns:
    player_score : renvoie notre score
    tour : renvoie le nombre de tours qu'il a fallu pour gagner
"""
def isWin(score, tour):
    if(score >= 100):
        print("C'est gagné ! Le jeu a duré " + str(tour) + " tours")
    return score, tour

"""
Fonction qui illustre notre tour de jeu
param:
    list_in : liste (représente les faces du dé)
    player_score : integer
    tour : integer
returns:
    player_score : renvoie notre score à la fin du tour
    tour : renvoie le tour actuel
"""
def player(list_in, player_score, tour):
    score = shuffle(list_in)
    scoreTour = 0
    if (score == 1):
        print("---------------------------------------------------------")
        print("Votre tour est fini, vous avez fait 1. Score total : " + str(player_score))
        tour += 1
    else:
        print("---------------------------------------------------------")
        print("Dé : " + str(score))
        scoreTour += score
        print("Score joueur : " + str(scoreTour))
        choice = input("Voulez-vous continuer ? y/n ")
        while (choice == "y" and score > 1 and player_score < 100):
            score = shuffle(list_in)
            if(score != 1):
                print("Dé : " + str(score))
                scoreTour += score
                print("Score joueur :" + str(scoreTour))
                choice = input("Voulez-vous continuer ? y/n ")
            else:
                scoreTour = 0
                break
        #on vérifie si le joueur a gagné
        isWin(player_score, tour)

        #si on ne veut pas continuer le tour, si choice = "n"
        if(score != 1):
            player_score += scoreTour
            print("Votre tour est fini. Score total : " + str(player_score))
        else:
            player_score -= scoreTour
            print("Votre tour est fini, vous avez fait 1. Score total : " + str(player_score))
        tour += 1
    print("C'est au tour de l'ordinateur")
    return player_score, tour


def computer(list_in, computer_score, tour):
    score = shuffle(list_in)
    scoreTour = 0
    if (score == 1):
        print("---------------------------------------------------------")
        print("Le tour de l'ordinateur est fini, il a fait 1. Score total : " + str(computer_score))
        tour += 1
    else:
        print("---------------------------------------------------------")
        print("Dé : " + str(score))
        scoreTour += score
        choiceStat = randint(1, 2)
        choice = "y"
        if (choiceStat == 2):
            choice = "n"
        while (choice == "y" and score > 1 and computer_score < 100):
            score = shuffle(list_in)
            if (score != 1):
                print("Dé : " + str(score))
                scoreTour += score
            else:
                scoreTour = 0
                break
        #on vérifie si l'ordinateur a gagné
        isWin(computer_score, tour)

        if (score != 1):
            computer_score += scoreTour
            print("Le tour de l'ordinateur est fini. Score total : " + str(computer_score))
        else:
            computer_score -= scoreTour
            print("Le tour de l'ordinateur est fini, il a fait 1. Score total : " + str(computer_score))
        tour += 1
    print("C'est à votre tour")
    return computer_score, tour

game_start = input("Appuyez sur Entrée pour lancer le dé.")
if game_start == "":
    dice_faces = [1, 2, 3, 4, 5, 6]
    player_score = 90
    computer_score = 0
    tour = 1
    while(player_score < 100 or computer_score < 100):
        if(tour % 2 == 1):
            player_score, tour = player(dice_faces, player_score, tour)
            print("score boucle while player : " + str(player_score))
        else:
            computer_score, tour = computer(dice_faces, computer_score, tour)
            print("score boucle while computer : " + str(computer_score))


