import random
import os

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

def printc(str, multiline=False, color=""):
    if color == "":
        if tour % 2 == 1:
            return print(colors.HEADER + str + colors.ENDC)
        else:
            return print(colors.OKGREEN + str + colors.ENDC)
    else:
        if multiline:
            return print(color + str + colors.ENDC),
        else:
            return print(color + str + colors.ENDC)

def inputc(str):
    if tour % 2 == 1:
        return input(colors.HEADER + str + colors.ENDC)
    else:
        return input(colors.OKGREEN + str + colors.ENDC)

def shuffle(dice):
    if isinstance(dice, list):
        return dice[random.randint(0,len(dice)-1)]

os.system('cls' if os.name == 'nt' else 'clear')
print(" \N{game die} DICE GAME \N{game die} ".center(consoleWidth - 2, "-"))

while isEnded == False:
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
                printc("Tu as fait", True),
                printc(str(pick), True, colors.UNDERLINE),
                printc("! Veux-tu rejouer ?")
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
        # Disons que l'ordinateur à 1 chance sur 4 de rejouer (à part si il tombe sur 1, bien sûr)
        printc("Ordi tour")
        printc(str(scoreJ))
        dejaJoue = False
        tour+=1

