# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:39:41 2020

@author: derbaghc
"""

from random import *
import S1_algotools as main

def shuffle(list_in:list, player_score, computer_score, tour):
    """
    Fonction qui joue pour l'ordinateur
    param:
        list_in : liste d'éléments
    returns:
        computer_score -> renvoie le score de l'ordinateur
    """

    while(tour % 2 == 1):
        score = main.alea(6)
        if (score == 1):
            print("Votre tour est fini, vous avez fait 1. Score total : " + str(player_score))
            tour += 1
        else:
            print("Dé : " + str(score))
            player_score += score
            print("Score joueur : " + str(player_score))
            choice = input("Voulez-vous continuer ? y/n ")
            while (choice == "y" and score > 1 and player_score < 100):
                score = main.alea(6)
                print("Dé : " + str(score))
                player_score += score
                print("Score joueur :" + str(player_score))
                choice = input("Voulez-vous continuer ? y/n ")

            if (player_score >= 100):
                print("Bravo, vous avez gagné ! Le jeu a duré " + str(tour) + " tours")
                return
            print("Votre tour est fini. Score total : " + str(player_score))
            tour += 1
        print("C'est au tour de l'ordinateur")

    score = main.alea(6)
    if (score == 1):
        print("Le tour de l'ordinateur est fini, il a fait 1. Score total : " + str(computer_score))
        tour += 1
    else:
        print("Dé : " + str(score))
        computer_score += score
        choice = "y"
        while (choice == "y" and score > 1 and computer_score < 100):
            score = main.alea(6)
            print("Dé : " + str(score))
            computer_score += score
        if (computer_score >= 100):
            print("La prochaine, vous gagnerez ! Le jeu a duré " + str(tour) + " tours et l'ordinateur a fait " + str(computer_score))
            return
        print("Le tour de l'ordinateur est fini. Score total : " + str(computer_score))
        tour += 1

    print("C'est à votre tour")
    shuffle(list_in, player_score, computer_score, tour)


print("Quel est votre nom ?")
player_name = input("Votre nom ? ")
print("Bienvenue " + player_name + ". Vous allez jouer contre un ordinateur. C'est parti !")
game_start = input("Appuyez sur Entrée pour lancer le dé.")
if game_start == "":
    dice_faces = [1, 2, 3, 4, 5, 6]
    player_score = 0
    computer_score = 0
    tour = 1
    shuffle(dice_faces, player_score, computer_score, tour)
    #print("Voici votre score :" + player_score)