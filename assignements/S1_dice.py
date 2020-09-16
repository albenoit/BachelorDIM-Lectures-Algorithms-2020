# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:18:16 2020

@author: bouvaran
"""
import random

#////////////////////////////////////////////    
gameStart      = False
human_score    = 0
computer_score = 0
winner_score   = 20
round_hu_comp  = 0
pointParRound  = 0
pointRoundEnd  = 0
mini           = 1
maxi           = 6
comp_RoundMax  = 3
    
def alea(mini,maxi):
    return random.randint(mini, maxi)
    
def Menue(gameStart):
    if gameStart == False:
        print("Welcome to the dice game")
        print("Do you want to play ? y / n ")
        
        if input() == "y":
            print("Let's go !")
            gameStart = True
            Start(gameStart,round_hu_comp,mini,maxi,comp_RoundMax,pointRoundEnd,human_score,computer_score)
        else:
            print("ok, bye")
            raise SystemExit
            
def CountPoint(round_hu_comp,pointRoundEnd,human_score,computer_score):
    if round_hu_comp == 0:
        print("human round")
        human_score = human_score + pointRoundEnd
        print("Human score : " + str(human_score))
        if human_score > winner_score:
            print("YOU WIN")
            raise SystemExit
        return Start(True,1,mini,maxi,comp_RoundMax,pointRoundEnd,human_score,computer_score)
    else : 
        print("computer round")
        computer_score = computer_score + pointRoundEnd
        print("Computer score : " + str(computer_score))
        if computer_score > winner_score:
            print("LOOOOOOSER")
            raise SystemExit
        return Start(True,0,mini,maxi,comp_RoundMax,pointRoundEnd,human_score,computer_score)
     

def Start(gameStart,round_hu_comp,mini,maxi,comp_RoundMax,pointRoundEnd,human_score,computer_score):
    if gameStart == True:
        if round_hu_comp == 0:
            print("Do you want throw the dice ? y/n")
            if input() == "y":
                pointParRound = alea(mini,maxi)
                print("dice = " + str(pointParRound))
                if pointParRound == 1:
                    pointRoundEnd = 1
                    print("end of round, point won : " + str(pointRoundEnd))
                    human_score = pointRoundEnd
                    CountPoint(0,pointRoundEnd,human_score,computer_score)
                else:
                    pointRoundEnd += pointParRound
                    Start(gameStart,round_hu_comp,mini,maxi,comp_RoundMax,pointRoundEnd,human_score,computer_score)
            else:
                print("end of round, point won : " + str(pointRoundEnd))
                CountPoint(0,pointRoundEnd,human_score,computer_score)
                
        else:
            computer_Round = alea(1,comp_RoundMax)
            for i in range(computer_Round):
                pointParRound = alea(mini,maxi)
                print("dice = " + str(pointParRound))
                if pointParRound == 1:
                    pointRoundEnd = 1
                    computer_score = pointRoundEnd
                    CountPoint(1,pointRoundEnd,human_score,computer_score)
                    print("end of round, point won : " + str(pointRoundEnd))
                else:    
                    pointRoundEnd += pointParRound
            print("end of round, point won : " + str(pointRoundEnd))
            computer_score = pointRoundEnd
            CountPoint(1,pointRoundEnd,human_score,computer_score)
    else:
        raise ValueError("Error, the game can't start")



Menue(gameStart)







