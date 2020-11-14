import S1_algotools as s1
import os
import time

players = [['Nathan', 0], ['IA', 0]]

goal = 10
dice_number = [1, 2, 3, 4, 5, 6]  # change here, if want an other dice
current_player = 0  # 'the user always starts'
tmp_score = 0


def start_game():
    """
        Lunch the dice game
    Returns:
        void
    """
    global tmp_score

    print("========================================")
    print("=       WELCOME ON THE DICE GAME       =")
    print("========================================")

    print(players[current_player][0] + " Commence, bonne chance !")
    while True:
        player = players[current_player]
        is_first_throw = True

        while True:
            if current_player == 0:
                relaunch = input(get_name(player) + " lancer le dé (y), arrêter (n), quitter (q)")
            else:
                relaunch = automatic_decision(is_first_throw)
                print("Réponse automatique : " + relaunch)
            if relaunch == 'q':
                quit()

            if relaunch == 'n':
                break

            if relaunch == 'y':
                if not dice():
                    tmp_score = 0
                    print(get_name(player) + " a fait 1, aucun point lui a été rajouté !")
                    break

                if check_win(player, tmp_score):
                    print(message_win(player))
                    break

                print(str(tmp_score) + " point(s) en jeu")
                is_first_throw = False
            else:
                print("Mauvaise réponse : soit dé (y), arrêter (n), quitter (q)")

        add_score(player, tmp_score)

        if not check_win(player, tmp_score):
            show_current_score()
            next_player()
        else:
            break

    relaunch = input("Relancer la partie ? (y)")
    if relaunch == "y":
        reset_game()


def cls():
    """
        Clear console, use if the player wants to play again
    Returns:
        void
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_current_score():
    """
        Show score of each players, when there is a switch of turn
    Returns:
        void
    """
    print("======================================")
    for data in players:
        print(data[0] + " : " + str(data[1]) + " point(s)")
    print("======================================")


def next_player():
    """
        Switch id of current_player
    Returns:
        void
    """
    global current_player
    current_player = 0 if current_player == 1 else 1


def get_name(player) -> str:
    """
        Get name of player
    Parameters:
        player

    Returns:
        string
    """
    return player[0]


def add_score(player: list, score: int):
    """
        Increased the sum of all the dice values obtained this turn.
    Args:
        player
        score

    Returns:
        void
    """
    global tmp_score
    player[1] += score
    tmp_score = 0


def check_win(player: list, current_tmp_score: int) -> bool:
    """
    Check if the score of player is greater that the current score + sum of all the dice values obtained in this turn

    Parameters:
        tmp_score player
    Returns:
        bool
    """
    if player[1] + current_tmp_score >= goal:
        return True

    return False


def message_win(player: list) -> str:
    """
        Show win message with name and score of player
    Parameters:
        player
    Returns:
        string
    """
    return "===========================================\n" + \
           "/!\\ " + player[0] + " gagne avec " + str(player[1] + tmp_score) + " points /!\\\n" + \
           "==========================================="


def dice() -> bool:
    """
        Simulate a dice roll
    Parameters:

    Returns:
        number contains in dice_number
    """
    global tmp_score

    number_obtained = throw_dice()
    if number_obtained != 1:
        tmp_score += number_obtained
        print("Le dé est tombé sur " + str(number_obtained))
        return True
    else:
        tmp_score = 0

    return False


def throw_dice() -> int:
    """
     Simulate a dice roll

    Parameters:

    Returns:
        number contains in dice_number
    """
    return s1.shuffle(dice_number)[0]


def automatic_decision(is_first_throw: bool) -> str:
    """
    If is the first throw in the turn, return 'y' like a human

    Parameters:
        is_first_throw: bool
    Returns:
        char ('y' = yes, 'n' = no)
    """
    time.sleep(1)
    if is_first_throw:
        return 'y'
    return s1.shuffle(['y', 'y', 'n'])[0]


def reset_game():
    """
        Reset score, current_player and clear the console
    Returns:
        void
    """
    global tmp_score, current_player
    for data in players:
        data[1] = 0
    tmp_score = 0
    current_player = 0  # 'the user always starts'
    cls()
    start_game()


"""
start_game()
"""
