# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:26:05 2020

@author: vanhouta
"""

import numpy as np
import random 

Tab = [1,5,9,8,7,5,9,6,7,2]

## Documentation for average_above_zero
# @param _table table with number above zero
def average_above_zero(table:list):
    Som = 0 
    ## @var _Som
    # Sum of all number
    N = 0
    ## @var _N
    # Length of the table
    for i in range (1,len(table)):
        if(table[i] > 0):
            Som += table[i]
            N += 1
    if(N > 0):
        Moy = Som/N
    else:
        raise ValueError("no positive value in the table")
    return Moy

#print("Moyenne du tableau : {}".format(average_above_zero(Tab)))

# 1. Si Som n'est pas défini, le programme ne fonctionne plus
# 2. Si toutes les valeus sont en dessous de 0, N restera à 0 et donc une
#   erreur apparaitra à "Moy = Som/N"

def maximum_value(table:list):
    '''
        This function find the highest value in the list
        Args:
            table: list of number
        Returns the maximum value of a list
    '''
    maxValue = 0
    index = 0
    for i in range (1,len(table)):
        if(table[i] > maxValue):
            maxValue = table[i]
            index = i+1
    return maxValue,index
    
(maxi,index) = maximum_value(Tab)
#print("Valeur Max : {} , index de la valeur max : {}".format(maxi,index))

def reverse_table(table:list):
    '''
        This funcion return a reversed list
        Args:
            table: list of number you want to reverse
        Returns the reversed list
    '''
    return table[::-1]

#print("Tableau inversé : {}".format(reverse_table(Tab)))

W=150
H=200
W2 = 12
H2 = 10

Xin = np.zeros((H,W),dtype=float)
Xin2 = np.zeros((H2,W2),dtype=float)

for yXin in range(45,56):
    for xXin in range(70,91):
        Xin[xXin,yXin]=1

for yXin2 in range(7,10):
    for xXin2 in range(6,9):
        Xin2[xXin2,yXin2]=1
Xin2[5,8]=1
Xin2[7,10]=1
Xin2[9,8]=1
def roi_bbox(img):
    '''
        This funcion compute bounding box coordinates of an object
        Args:
            img: Binary image
        Returns the bounding box in numpy array
    '''
    (y,x)=img.shape
    x1 = x
    y1 = y
    x2 = 0
    y2 = 0
    for yImg in range(0,y):
        for xImg in range(0,x):
            if(img[yImg,xImg] == 1):
#                null = 0
#            elif(img[yImg,xImg] == 1 and null == 0):
                if(xImg < x1):
                    x1 = xImg
                if(yImg < y1):
                    y1 = yImg
                if(xImg > x2):
                    x2 = xImg
                if(yImg > y2):
                    y2 = yImg
    
                
    return np.array([x1,y1,x2,y2])

'''print(roi_bbox(Xin))
print(Xin2)
print(roi_bbox(Xin2))'''

chaine = "Ace Of Spades"
def remove_whitespace(string):
    '''
        This funcion romeve whitespace in a string
        Args:
            string: String with character
        Returns the string without whitespace
    '''
    strFinal = ""
    for i in string:
        if(i != " "):
            strFinal += i
    return strFinal
    #return string.replace(" ","")

#print(remove_whitespace(chaine))

listshuffle = [1,2,3,4,5,6,7]
def shuffle(list_in):
    for i in range(len(list_in)-1, 0, -1): 
        randIndex = random.randint(0, i + 1)  
        list_in[i], list_in[randIndex] = list_in[randIndex], list_in[i]  
    return list_in

#print(shuffle(listshuffle))

def a_dice_game():
    userscore = 0
    computerscore = 0
    maxDice = 6
    randChoiceComputer = 2
    winScore = 100
    turn = 0 #0 = user 1 = computer
    sumDiceScore = 0
    decision = ""

    while(userscore <= winScore or computerscore <= winScore):
        if(turn == 0):
            print("Votre score total est de {}".format(userscore))
            print("Votre score sur ce tour est de {}".format(sumDiceScore))
            print("Voulez vous lancer un dé ? (O/N)")
            decision = input()
            print(decision)
            while(decision != 'N' or decision != 'n' or decision != 'O' or decision != 'o'):
                print("Erreur. Voulez vous rejouez ? (O/N)")
                decision = input()
            
            if(decision == "N" or decision == "n"):
                userscore += sumDiceScore
            elif(decision == "O" or decision == "o"):
                dice = random.randint(1,maxdice)
                print("Vous avez fait un lancé de {}".format(dice))
                if(dice == 1):
                    print("Votre score sur ce tout est perdu")
                    sumDiceScore = 0
                    turn = 1
                else:
                    sumDiceScore =+ dice


#a_dice_game()





