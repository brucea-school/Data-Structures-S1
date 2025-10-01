import math

# colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'
class Board:

    def __init__(self, x: int, y: int, mines: int):
        self.mineBoard = [' ']*x
        self.isMined = False
        self.startingMineAmt = mines

        for i in range(0, len(self.mineBoard)):
            self.mineBoard[i] = [False]*y

        # make payer board
        self.playerBoard = [' ']*x

        for i in range(0, len(self.playerBoard)):
            self.playerBoard[i] = [' ']*y

    def printBoard(self):

        print("_"+"_" * len(self.playerBoard)+"_")
        if (self.isGameOver() == "run"):
            print("|"+" "*math.floor(len(self.playerBoard)/2)+"🙂"+" "*math.ceil(len(self.playerBoard)/2)+"|")
        elif (self.isGameOver() == "loss"):
            print("|" + " " * math.floor(len(self.playerBoard) / 2) + "😵" + " " * math.ceil(len(self.playerBoard) / 2) + "|")
        else:
            print("|" + " " * math.floor(len(self.playerBoard) / 2) + "😎" + " " * math.ceil(len(self.playerBoard) / 2) + "|")




    def isGameOver(self) -> str:
        #TODO
        return "loss"

