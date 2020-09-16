import random

class DiceGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.hasStarted = False
        self.msg_throwDice = 'Throwing dice ...'
        self.msg_resultThrow = 'Result of throw : '
        self.msg_pressThrow = 'Press t to throw the dice'

    def hasWin(self):
        if self.player_score >= 100:
            return [True,'player']
        elif self.computer_score >=100:
            return [True,'computer']
        else:
            return False

    def alea(self,x,min=None):
        """
        This function generate a random number

        Parameters :
            x: max number
        Returns :
            return random nuumber
        """
        if min != None:
            return random.randint(min, x)
        else:
            return random.randint(0, x)

    def throwDice(self):
        return self.alea(6,1)

    def printScore(self,x):
        print('Your score is now : ' + self.)

    def playerRoundStart(self):
        print("Welcome to Dice Game, player start")
        print(self.msg_throwDice)
        print(self.msg_pressThrow)
        if input() == 't':
            print(self.msg_resultThrow + str(self.throwDice()))
            self.printScore('player')

    def start(self):
        if not self.hasWin():
            if self.hasStarted:
                pass
            else:
                self.playerRoundStart()



dice = DiceGame()
dice.start()