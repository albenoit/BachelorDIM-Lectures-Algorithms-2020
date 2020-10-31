# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:26:46 2020

@author: polletb
"""
import S1_algotools as s1

dice = [1, 2, 3, 4, 5, 6]

while True:

    playerScore = 0
    computerScore = 0
    turn = 0
    numberTmp = 0

    print("---------------------------------------------------")
    print("-------------------- Dice game --------------------")
    print("---------------------------------------------------")
    print("\n")
    print("------> Are you ready? Please enter 'start' <------")

    start = input()

    if start == 'start':
        while True:

            if (playerScore or computerScore) >= 100:
                break

            print("Score player : " + str(playerScore))
            print("Score computer : " + str(computerScore))
            print("---------------------------------------------------")
            turnOf = "Turn of player" if turn % 2 == 0 else "Turn of computer"
            print(turnOf)

            while True:

                randomNumber = s1.function_shuffle(dice)[0]
                numberTmp = numberTmp + randomNumber
                print("You have done : " + str(randomNumber))

                if randomNumber == 1:
                    print("nice try you have get 1 no points add")
                    numberTmp = 0
                    turn += 1
                    break

                reroll = input("Please enter 'go' to continue or 'stop'")

                if reroll == "stop":
                    if turn % 2 == 0:
                        playerScore += numberTmp
                    else:
                        computerScore += numberTmp
                    numberTmp = 0
                    turn += 1
                    break

        print("Game is over")
        winner = "player" if playerScore <= 100 else "computer"
        print("Winner is : " + winner)
        print("---------------------------------------------------")
        print("You want to retry ? Y/N")
        retry = input()
        if retry == 'N':
            break