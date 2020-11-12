# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:39:41 2020

@author: derbaghc
"""

from random import *

def shuffle(list_in:list):
    """
    Fonction qui joue pour l'ordinateur
    param:
        list_in : liste d'éléments
    returns:
        computer_score -> renvoie le score de l'ordinateur
    """
    if isinstance(list_in, list):
        return list_in[randint(1, len(list_in)-1)]

#print(shuffle([1, 2, 3, 4, 5, 6]))

def player(list_in, player_score, tour):
    score = shuffle(list_in)
    scoreTour = 0
    if (score == 1):
        player_score = 0
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

        if (player_score >= 100):
            print("Bravo, vous avez gagné ! Le jeu a duré " + str(tour) + " tours")
            return
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
        computer_score = 0
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
        if (computer_score >= 100):
            print("La prochaine, vous gagnerez ! Le jeu a duré " + str(tour) + " tours et l'ordinateur a fait " + str(computer_score))
            return
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
    player_score = 0
    computer_score = 0
    tour = 1
    while(player_score < 100 or computer_score < 100):
        if(tour % 2 == 1):
            player_score, tour = player(dice_faces, player_score, tour)
        else:
            computer_score, tour = computer(dice_faces, computer_score, tour)


