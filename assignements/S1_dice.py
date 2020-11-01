# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:29:13 2020

@author: tapiev
"""

def dicegame():
    score_pc = 0
    score_joueur = 0
    gagnant ='pc'
    while score_pc<100:
        print("score joueur: "+str(score_joueur)+" score pc: "+str(score_pc))
        temp = play_manche_joueur()
        if temp != -1:
            print("cette manche le joueur à marqué "+ str(temp)+" points")
            score_joueur += temp
        if score_joueur>=100:
            gagnant = 'joueur'
            break
        score_pc += play_manche_pc()  
    print("le " + gagnant + " à gagné")
    

import random as random

def play_manche_pc():   
    """
    cette fonction gère la manche du pc
    Returns:
    """
    cagnote = 0
    while True:
        temp = random.randint(1, 6)
        if temp != 1:
            cagnote += temp
        else:
            print("le pc à fait 0 points cette manche ")
            return 0
        #formule aléatoire pour savoir si l'on rejoue en tant que pc
        if(random.randint(5,12)<cagnote):
            break
    print("score de la manche du pc " + str(cagnote))
    return cagnote



def play_manche_joueur():
    """
    cette fonction propose au joueur de jouier une manche si il fauit 1 , son score est annulé et la fonction retourne -1
    Returns:
        le total de la cagnote

    """
    cagnote=0
    if input("voulez vous lancer un dé ? (y pour relancer, ou anykey pour arréter)\n")=="y":
        val_de = lancer_le_de()

        print("resultat du lancé de dé:" + str(val_de))
        if val_de != 1:
            temp = play_manche_joueur()
            if temp == -1:
                return -1
            else:

                cagnote += temp + val_de
        else:
            print("perdu, votre tour est terminé")
            return -1
    return cagnote


    
def lancer_le_de():
    """
    Cettefonction retourne une valeur de dé entre 1 et 6
    Returns:

    """
    return(random.randint(1,6))
    


dicegame()