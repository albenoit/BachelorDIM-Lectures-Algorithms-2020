import random
import time


class Player(object):
    """
    Class to instance players
    Parameters :
        name: name of player,
        score: score of player
    """

    def __init__(self, name, score):
        self.name = name
        self.score = score


def dice_roll(current_player):
    """
    Function to roll dice
    Parameters :
        current_player: current player name for print
    Returns :
        roll: dice value
    """
    roll = random.randint(1, 6)
    print("%s rolled a %d " % (current_player, roll))
    return roll


def dice_game():
    """
    A dice game computer vs player
    Player always play first.
    Computer play a ramdon roll between 1 and 6
    Returns :
        player winner
    """
    players = []
    players.append(Player("User", 0))
    players.append(Player("Computer", 0))
    current_player = players[0]
    first_roll = True
    winner = -1
    current_score = 0
    computer_dices = random.randint(1, 5)

    # Start game with user
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+              Dice Game Player vs Computer             +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print("")

    while winner == -1:
        print("")

        if first_roll == True:
            first_roll = False
            print("%s played" % current_player.name)
            enter = input("ENTER to roll the dice: ")

        else:
            if current_player.name == "Computer":
                if computer_dices >= 0:
                    enter = ""
                    computer_dices = computer_dices - 1
                else:
                    enter = "Q"
                time.sleep(1)
            else:
                enter = input(
                    "Do you want to play again or stop and add %d to your score? (C or Enter to continue / Q to quit)"
                    % current_score
                )

        if enter == "" or (
            first_roll == False and (enter == "C" or enter == "c")
        ):  # hitting enter == ''  empty string
            roll = dice_roll(current_player.name)
            if roll != 1:
                current_score = current_score + roll
            else:
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("+                    Faillllllll                        +")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("")
                print(
                    "You roll a one, you loose %d pts. %s play"
                    % (current_score, current_player.name)
                )

                if current_player.name == "User":
                    current_player = players[1]
                    first_roll = False
                    computer_dices = random.randint(1, 5)
                else:
                    current_player = players[0]
                    first_roll = True

                current_score = 0

        else:
            current_player.score = current_player.score + current_score
            exit_roll = True
            current_score = 0

            if current_player.name == "User":
                current_player = players[1]
                first_roll = False
                computer_dices = random.randint(1, 5)
            else:
                current_player = players[0]
                first_roll = True

            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("+                    Current Scores                     +")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
            print("%s ====> %s pts" % (players[0].name, players[0].score))
            print("%s ====> %s pts" % (players[1].name, players[1].score))
            print("")

        if players[0].score >= 100:
            winner = 0
        if players[1].score >= 100:
            winner = 1

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                       Winner                          +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print("%s win with %s pts" % (players[winner].name, players[winner].score))
    print("")


dice_game()