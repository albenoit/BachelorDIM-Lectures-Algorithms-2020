import random
import os
import time

dice = [1,2,3,4,5,6]
isEnded = False
consoleWidth = os.get_terminal_size().columns
tour = 1
scoreJ = 0
scoreO = 0
dejaJoue = False
scoreTemp = 0

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printc(str):
    return print(colors.HEADER + str + colors.ENDC)

def inputc(str):
    if tour % 2 == 1:
        return input(colors.HEADER + str + colors.ENDC)
    else:
        return input(colors.OKGREEN + str + colors.ENDC)

def getComputerAction():
    choice = ""
    if random.randint(1,4) == 1:
        choice = "q"

    return choice

def shuffle(dice):
    if isinstance(dice, list):
        return dice[random.randint(0,len(dice)-1)]

os.system('cls' if os.name == 'nt' else 'clear')
print(" \N{game die} DICE GAME \N{game die} ".center(consoleWidth - 2, "-"))

while isEnded == False:
    print("".center(consoleWidth, "-"))
    print(colors.FAIL + "Score: Joueur ("+str(scoreJ)+") / Ordinateur ("+str(scoreO)+")" + colors.ENDC)
    if tour % 2 == 1:
        # Joueur
        if not dejaJoue:
            printc("A ton tour !")
        
        isSkip = False
        choice = inputc("Choisis une action: Jouer (Entrer) / Passer (q): ")
        if choice == "":
            # Jouer
            pick = shuffle(dice)
            if pick == 1:
                printc("Tu as fait 1 ! Tu ne peux donc pas rejouer et ton score ne s'incrémentera pas. C'est au tour de l'ordinateur.")
                scoreTemp = 0
                isSkip = True
            else:
                printc("Tu as fait " + str(pick) + " ! Veux-tu rejouer ?")
                scoreTemp = scoreTemp + pick
                printc("Score au tour actuel: " + str(scoreTemp))
                dejaJoue = True
        else:
            # Passer son tour
            tour+=1
            scoreJ+=scoreTemp

        if isSkip == True:
            tour+=1
            scoreJ+= scoreTemp

        if scoreJ >= 100:
            isEnded = True
            printc("Vous avez gagné !")
    
    else:
        # Ordinateur
        # Disons que l'ordinateur à 1 chance sur 4 de passer son tour (à part si il tombe sur 1, bien sûr)
        # printc("Ordi tour")
        # printc(str(scoreJ))
        time.sleep(random.uniform(0.25,1.5))
        # tour+=1
        
        isSkip = False
        # print("L'ordinateur choisi une action: Jouer (Entrer) / Passer (q): ")
        choice = getComputerAction()
        # print("choice = " + choice)
        if choice == "":
            # Jouer
            print("L'ordinateur a choisis de jouer.")
            pick = shuffle(dice)
            # print("pick = " + str(pick))
            if pick == 1:
                print("L'ordinateur as fait 1 ! Il ne peux donc pas rejouer et son score ne s'incrémentera pas. C'est à ton tour.")
                scoreTemp = 0
                isSkip = True
            else:
                print("Il as fait " + str(pick) + " ! Veux-t-il rejouer ?")
                scoreTemp = scoreTemp + pick
                print("Score au tour actuel: " + str(scoreTemp))
        else:
            # Passer son tour
            print("L'ordinateur a choisi de passer son tour.")
            tour+=1
            scoreO+=scoreTemp

        if isSkip == True:
            tour+=1
            scoreO+= scoreTemp

        if scoreO >= 100:
            isEnded = True
            print("L'ordinateur a gagné !")

    # print(tour)

