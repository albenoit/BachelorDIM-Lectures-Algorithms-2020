import random


class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


def dice_roll(current_player):
    roll = random.randint(1, 6)
    print("%s rolled a %d " % (current_player, roll))
    return roll


def main():
    players = []
    players.append(Player("User", 0))
    players.append(Player("Computer", 0))
    current_player = players[0]
    exit_roll = False
    no_one = True
    current_score = 0
    # Start game with user
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+              Dice Game Player vs Computer             +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print("")
    print("User is played")

    while no_one == True:
        if exit_roll == False:
            exit_roll = True
            enter = input("ENTER to roll the dice: ")

        else:
            again = input(
                "Do you want to play again or stop and add %d to your score? (C to continue / S to stop)"
                % current_score
            )
            if again == "C":
                exit_roll = False
            else:
                current_player.score = current_player.score + current_score
                exit_roll = False
                current_score = 0
                if current_player.name == "User":
                    current_player = players[1]
                else:
                    current_player = players[0]
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("                      SCORE                              ")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("%s ===> %d pts" % (players[0].name, players[0].score))
                print("%s ===> %d pts" % (players[1].name, players[1].score))
                print("")

        if enter == "":  # hitting enter == ''  empty string
            roll = dice_roll(current_player.name)
            if roll != 1:
                current_score = current_score + roll
            else:
                exit()
        else:
            print("exiting program.")
            exit()


main()
