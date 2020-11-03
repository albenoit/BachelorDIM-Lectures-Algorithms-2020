# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:38:43 2020

@author: albentmp
"""

from random import *

'''
Small Dice Game against a bot: first to 100 win the game
'''
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

#Test
#shuffle()


#Sorting:
'''
1.a)
- 10, 15, 7, 1, 3, 3, 9
- 1, 15, 7, 10, 3, 3, 9
- 1, 3, 7, 10, 15, 3, 9
- 1, 3, 3, 10, 15, 7, 9
- 1, 3, 3, 7, 15, 10, 9
- 1, 3, 3, 7, 9, 10, 15

1.b)
The number of iterations depend on the vector content

1.c)
There will be as much iteration as the vector's lenght

1.d)
Vector's lenght

1.e)
Vector's lenght

1.f)
no

1.g)
'''

'''
function which permit de sort a vector (by finding the smallest value and to permut it)
@param: list list_in, list of integers
@return an ASC oredered list
'''
def sort_selective(list_in:list):
    for i in range(len(list_in)):
        #Find the smallest value
        min_idx = i 
        for j in range(i+1, len(list_in)): 
            if list_in[min_idx] > list_in[j]: 
                min_idx = j

        #Swap the smallest value to the first element
        list_in[i], list_in[min_idx] = list_in[min_idx], list_in[i]
    return list_in

#Source: https://www.geeksforgeeks.org/selection-sort/
#Test
listTest = [10, 15, 7, 1, 3, 3, 9]
print(sort_selective(listTest))





































        
    
