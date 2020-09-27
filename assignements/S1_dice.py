"""
@author: fabien-v
"""

# Dice Game


def shuffle():

    import random
    user_score = 0
    computer_score = 0
    minimum = 1
    maximum = 6
    user_roll = random.randint(minimum, maximum)
    computer_roll = random.randint(minimum, maximum)

    if user_roll == 1:
        user_score += 1
    elif user_roll == 2:
        user_score += 2
    elif user_roll == 3:
        user_score += 3
    elif user_roll == 4:
        user_score += 4
    elif user_roll == 5:
        user_score += 5
    elif user_roll == 6:
        user_score += 6

    if user_score  == 100:
        print("user win !")
    if computer_score == 100:
        print("computer win !")

# idea / in progress

# boucle avec
# Tant que user_try > 1
#    roll_again (continue ?)

# Si user_try == 1
#    alors c'est au tour de à computer_try et ainsi de suite













