import random

def dicegame():

    #Player data
    playerRoll = 0
    playerResult = 0
    playerRound = 0

    #Bot data
    botRoll = 0
    botRound = 0
    botResult = 0

    #Game data
    interact = 'y'
    game = True
    botKeepPlaying = 1

    while(game):
        while(interact == 'y' and playerRoll != 1):
            botRound=0
            botKeepPlaying = 1
            playerRoll = random.randrange(1,7)
            playerRound += playerRoll
            interact = input("Would you like to keep rolling ? (y or n)")
            if(interact == 'q'):
                game = False
            if(interact != 'y'):
                playerResult = playerResult
            elif(playerRoll == 1):
                playerResult -= playerRound - 1
                playerRound = 0
                print('Player dice: ',playerRoll)
                print('Oh no! you rolled a 1! Your score for this round is reset.')
            else:
                playerResult += playerRoll
                print('Player dice: ',playerRoll)
            print('Player total = ',playerResult)
            botRoll = 0
            if(playerResult >= 100):
                interact = 2
                game = False
                botKeepPlaying = 0
                print('PLAYER WINS!!')

        while(botRoll != 1 and botKeepPlaying != 0):
            playerRound = 0
            botRoll = random.randrange(1,7)
            botRound += botRoll
            botKeepPlaying = random.randrange(0,3)
            if(botRoll == 1):
                botResult -= botRound - 1
                botRound = 0
                print('Lucky for you, the bot just rolled a 1 and lost his points...')
            else:
                botResult += botRoll
                print('Bot dice: ', botRoll)
            print('Bot total = ', botResult)
            playerRoll = 0
            interact = 'y'
            if (botResult >= 100):
                interact = 2
                botRoll = 0
                game = False
                interact='n'
                print('BOT WINS...')

dicegame()