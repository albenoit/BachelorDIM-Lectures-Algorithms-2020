import random

class DictMessage:
    def __init__(self):
        self.msg_throwDice = 'Throwing dice ...'
        self.msg_resultThrow = 'Result of throw : '
        self.msg_pressThrow = 'Press t to throw the dice'

class DiceGame:
    def __init__(self):

        self.turn = 0

        self.player_score = 0
        self.computer_score = 0

        self.tmp_score = 0

        self.hasStarted = False
        self.msg_throwDice = '\n-------- [ ROLL ] --------\n\nThrowing dice ...'
        self.msg_resultThrow = 'Result of throw : '
        self.msg_pressThrow = 'Press t to throw the dice\n'

    def getScore(self,x):
        return self.__getattribute__(x)

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

    def replay(self):
        print("\nPress r to reroll the dice \nPress other key to stop\n")
        if input() == 'r':
            self.roll()
        else:
            self.stop()

    def resume(self):
        print("\n-------- [ RESUME SCORE ] --------\n")
        print("\nPlayer score : " + str(self.player_score))
        print("\nComputer score : " + str(self.computer_score))
        input("\nPress any key to continu\n")

        self.tmp_score = 0

        if self.turn: # now player
            self.turn = 0
        else:
            self.turn = 1
            self.computer_turn()

    def computer_turn(self):
        throw = self.throwDice
        if throw == 1:
            self.computer_score += 1
            self.resume()
        else:
            while True: 
                replay = self.alea(3) 
                throw = self.alea(6,1)
                self.tmp_score += throw
                
                if throw == 1:
                    self.computer_score += 1
                    break

                if replay == 0:  
                    self.computer_score += self.tmp_score
                    break  
            self.resume()

    def stop(self):
        self.player_score += self.tmp_score
        self.printScore('player_score')
        self.tmp_score = 0
        self.resume()
        

    def roll(self):
        if not self.hasStarted: 
            print("Welcome to Dice Game, player start")
            self.hasStarted = True

        print(self.msg_throwDice)
        print(self.msg_pressThrow)
        if input() == 't':
            throw = self.throwDice()
            self.updateScore(throw)
            print("\n-------- [ DICE GAME ] --------\n")
            print("You can win : " + str(self.tmp_score) +  ' points')
            print(self.msg_resultThrow + str(throw))
            self.checkScore(throw, 'player_score')

    def updateScore(self,score, force = None):
        if force:
            self.tmp_score = 1
        else:
            self.tmp_score += score

    def checkScore(self, throw, score):
        if throw != 1:
            self.replay()
        else:
            self.updateScore(1,1)
            self.stop()

    def printScore(self,x):
        print('\n-------- [ SCORE ] --------\n\nYour score is now : ' + str(self.getScore(x)))

    def start(self):
        while not self.hasWin():
            self.roll()
        
        if(self.player_score < self.computer_score):
            print("Computer win the game ! ("+str(self.computer_score)+":"+str(self.player_score)+")")
        else:
            print("Player win the game ! ("+str(self.player_score)+":"+str(self.computer_score)+")")



dice = DiceGame()
dice.start()