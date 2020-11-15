import random as random

def shuffle ():
    user_score = 0
    comp_score = 0
    winner = ''
    temp2 = 0

    print('------------------------------------------------------\n Bienvenue dans le meilleur jeu de dés de l\'unvivers \n------------------------------------------------------')

    while(winner == ''):
        print("Score Joueur : " + str(user_score) + "\nScore PC : " + str(comp_score))
        temp = user_turn()
        temp2 += temp
        if(temp != 0 and temp != -1):
            user_score += temp
            print('---------- SCORE TOTAL JOUEUR : ' + str(user_score) + ' ----------')
        if(user_score >= 100):
            winner = "Joueur"
        
        if(temp == 0 or temp == -1):
            if(temp == 0):
                user_score -= temp2
            temp_comp = comp_turn()
            comp_score += temp_comp
            temp2 = 0
        if(comp_score >= 100):
            winner = "PC"

    print("------------------------------------------------------\n Le gagnant de la partie est : " + str(winner) + ' \n------------------------------------------------------')


def user_turn():
    point = -1
    roll = 0
    play = input("Voulez vous lancer le dé ? (y or otherkey)")

    if (play == "y"):
        point = 0
        roll = roll_dice()
        if(roll == 1):
            point = 0
            print("Vous avez perdu vos points pour ce tour car vous avez fait 1")
        else:
            point += roll
            print("Score du tour : " + str(point))

    return point


def comp_turn():
    point = 0
    roll = 0

    print("---------------- Tour du Pc : ----------------")

    while(roll != 1):
        roll = roll_dice()
        print("Le pc à fait : " + str(roll))
        if(roll == 1):
            print("Le PC a fait 1 et a perdu ces points pour ce tour")
            point = 0
        else:
            point += roll

        print("---------------- Score PC : " + str(point) + ' ---------------------')

        if(point > roll_dice() * 6):
            break

    return point


def roll_dice ():
    return int(random.randint(1,6)) 

shuffle()