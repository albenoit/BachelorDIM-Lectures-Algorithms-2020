import random


class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


def dice_roll(current_player):
    roll = random.randint(1, 6)
    print("%s rolled a %d " % (current_player, roll))
    return roll


def dice_game():
    players = []
    players.append(Player("User", 0))
    players.append(Player("Computer", 0))
    current_player = players[0]
    first_roll = True
    winner = -1
    current_score = 0

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
            enter = input(
                "Do you want to play again or stop and add %d to your score? (C to continue / S to stop)"
                % current_score
            )

        if enter == "" or (
            first_roll == False and (enter == "C" or enter == "c")
        ):  # hitting enter == ''  empty string
            roll = dice_roll(current_player.name)
            if roll != 1:
                current_score = current_score + roll
            else:
                if current_player.name == "User":
                    current_player = players[1]
                else:
                    current_player = players[0]
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("+                    Faillllllll                        +")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("")
                print(
                    "You roll a one, you loose %d pts. %s play"
                    % (current_score, current_player.name)
                )
                first_roll = True
                current_score = 0

        else:
            current_player.score = current_player.score + current_score
            first_roll = True
            exit_roll = True
            current_score = 0
            if current_player.name == "User":
                current_player = players[1]
            else:
                current_player = players[0]

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
