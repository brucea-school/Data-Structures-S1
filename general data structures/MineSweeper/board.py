import math
import os

# colors
BOLD = '\033[1m'
BLINK = '\033[5m'

BLACK_TEXT = '\033[30m'
GRAY_TEXT = '\033[90m'
RED_TEXT = '\033[31m'
GREEN_TEXT = '\033[32m'
YELLOW_TEXT = '\033[33m'
BLUE_TEXT = '\033[34m'
MAGENTA_TEXT = '\033[35m'
CYAN_TEXT = '\033[36m'
WHITE_TEXT = '\033[97m'

BLACK_BG = '\033[40m'
GRAY_BG = '\033[100m'
RED_BG = '\033[41m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[103m'
BLUE_BG = '\033[44m'
MAGENTA_BG = '\033[45m'
CYAN_BG = '\033[46m'
WHITE_BG = '\033[47m'

RESET = '\033[0m'
class Board:

    def __init__(self, x: int, y: int, mines: int):
        self.mineBoard = [' ']*x
        self.isMined = False
        self.startingMineAmt = mines
        self.flags = 0

        for i in range(0, len(self.mineBoard)):
            self.mineBoard[i] = [False]*y

        # make payer board
        self.playerBoard = [' ']*x

        for i in range(0, len(self.playerBoard)):
            self.playerBoard[i] = [' ']*y

    def printBoard(self):


        if (self.isGameOver() == "run"):
            print("🙂")
        elif (self.isGameOver() == "loss"):
            print("😵")
        else:
            print("😎")

        minesLeft = str(self.startingMineAmt - self.flags)

        if len(minesLeft) == 1:
            print(BLACK_BG+RED_TEXT+"00"+minesLeft[0]+RESET)
        elif len(minesLeft) == 2:
            print(BLACK_BG + RED_TEXT + "0"+ minesLeft[1] + minesLeft[0] + RESET)
        else:
            print(BLACK_BG + RED_TEXT + minesLeft + RESET)
        print()

        if len(str(len(self.playerBoard[0]))) == 2:
            print("  ",end="")
        else:
            print(" ",end="")


        if len(str(len(self.playerBoard[0]))) >1:
            for i in range(0, len(self.playerBoard[0])):
                if len(str(i)) == 1:
                    print(" ",end="")
                else:
                    print(str(i)[0],end="")
            print()
            if len(str(len(self.playerBoard[0]))) == 2:
                print("  ", end="")
            else:
                print(" ", end="")
            for i in range(0, len(self.playerBoard[0])):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")
        else:
            for i in range(0, len(self.playerBoard[0])):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")


        print()
        b = 0
        for x in self.playerBoard:

            if len(str(len(x))) > 1:
                if b < 10:
                    print(" "+str(b), end='')
                else:
                    print( str(b), end='')
            else:
                print(b, end='')

            b += 1
            for y in x:
                if y == " ":
                 print(GRAY_BG+str(y)+RESET , end='')
                elif y == "-":
                    print(BLACK_BG + " " + RESET, end='')
                elif y == "F":
                    print(RED_TEXT + "⚑" + RESET, end='')
                elif str(y) == "1":
                    print(BLACK_BG + BLUE_TEXT + "1" + RESET, end='')
                elif str(y) == "2":
                    print(BLACK_BG + GREEN_TEXT + "2" + RESET, end='')
                elif str(y) == "3":
                    print(BLACK_BG + RED_TEXT + "3" + RESET, end='')
                elif str(y) == "4":
                    print(BLACK_BG + MAGENTA_TEXT + "4" + RESET, end='')
                elif str(y) == "5":
                    print(BLACK_BG + RED_TEXT + BOLD + "5" + RESET, end='')
                elif str(y) == "6":
                    print(BLACK_BG + CYAN_TEXT + "6" + RESET, end='')
                elif str(y) == "7":
                    print(BLACK_BG + GRAY_TEXT + "7" + RESET, end='')
                elif str(y) == "8":
                    print(BLACK_BG + GRAY_TEXT + BOLD + "8" + RESET, end='')
                elif str(y) == "M":
                    print(RED_BG + WHITE_TEXT + BOLD + "!" + RESET, end='')
                elif str(y) == "?":
                    print(YELLOW_BG + BLACK_TEXT + BOLD + BLINK + "#" + RESET, end='')
            print(b-1)

        if len(str(len(self.playerBoard[0]))) == 2:
            print("  ", end="")
        else:
            print(" ", end="")

        if len(str(len(self.playerBoard[0]))) > 1:
            for i in range(0, len(self.playerBoard[0])):
                if len(str(i)) == 1:
                    print(" ", end="")
                else:
                    print(str(i)[0], end="")
            print()
            if len(str(len(self.playerBoard[0]))) == 2:
                print("  ", end="")
            else:
                print(" ", end="")
            for i in range(0, len(self.playerBoard[0])):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")
        else:
            for i in range(0, len(self.playerBoard[0])):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")

        print()



    def tryToDig(self):
        return True


    def isGameOver(self) -> str:
        #TODO
        return "run"

