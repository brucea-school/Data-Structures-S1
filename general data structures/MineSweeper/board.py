import math
import os
import random
import sys
sys.setrecursionlimit(99999999)

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

    def __init__(self, x: int, mines: int):
        self.mineBoard = [' ']*x
        self.startingMineAmt = mines
        self.flags = 0
        self.status = "run"

        for i in range(0, len(self.mineBoard)):
            self.mineBoard[i] = [False]*x

        i = 0

        while i <= self.startingMineAmt:
            ex = random.randint(0, len(self.mineBoard)-1)
            ey = random.randint(0, len(self.mineBoard[0])-1)
            if not self.isMine(ex,ey):
                #print("("+str(ex)+","+str(ey)+")")
                self.mineBoard[ex][ey] = True
                i+=1

        # make payer board
        self.playerBoard = [' ']*x

        for i in range(0, len(self.playerBoard)):
            self.playerBoard[i] = [' ']*x

    def printBoard(self):

        #print face
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

        #print numbers
        if len(str(len(self.playerBoard))) == 2:
            print("  ",end="")
        else:
            print(" ",end="")


        if len(str(len(self.playerBoard))) >1:
            for i in range(0, len(self.playerBoard)):
                if len(str(i)) == 1:
                    print(" ",end="")
                else:
                    print(str(i)[0],end="")
            print()
            if len(str(len(self.playerBoard))) == 2:
                print("  ", end="")
            else:
                print(" ", end="")
            for i in range(0, len(self.playerBoard)):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")
        else:
            for i in range(0, len(self.playerBoard)):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")


        print()
        b = 0
        for x in range(0, len(self.playerBoard)):

            if len(self.playerBoard[0]) > 10:
                if b < 10:
                    print(" "+str(b), end='')
                else:
                    print( str(b), end='')
            else:
                print(b, end='')

            b += 1
            for h in range(0, len(self.playerBoard)):
                #print actual board
                y = self.playerBoard[h][x]
                if y == " ":
                 print(GRAY_BG+str(y)+RESET , end='')
                elif y == "-":
                    print(BLACK_BG + " " + RESET, end='')
                elif y == "F":
                    print(RED_TEXT+ GRAY_BG + "⚑" + RESET, end='')
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

        if len(str(len(self.playerBoard))) == 2:
            print("  ", end="")
        else:
            print(" ", end="")

        if len(str(len(self.playerBoard))) > 1:
            for i in range(0, len(self.playerBoard)):
                if len(str(i)) == 1:
                    print(" ", end="")
                else:
                    print(str(i)[0], end="")
            print()
            if len(str(len(self.playerBoard))) == 2:
                print("  ", end="")
            else:
                print(" ", end="")
            for i in range(0, len(self.playerBoard)):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")
        else:

            for i in range(0, len(self.playerBoard)):
                if len(str(i)) == 1:
                    print(i, end="")
                else:
                    print(str(i)[1], end="")

        print()



    def isMine(self,x:int,y:int):
        #is out of range?
        if x < 0:
            return False
        if x >= len(self.mineBoard):
            return False
        if y < 0:
            return False
        if y >= len(self.mineBoard[0]):
            return False
        # check mine
        return self.mineBoard[x][y]

    def tryToDig(self, x:int,y:int):
        # is out of range?
        if x < 0:
            return
        if x > len(self.mineBoard)-1:
            return
        if y < 0:
            return
        if y > len(self.mineBoard[0])-1:
            return

        # are you checked alerdy?
        if not (self.playerBoard[x][y] == ' ' or self.playerBoard[x][y] == 'F'):
            return


        if self.isMine(x,y):
            # KABOOM!
            self.status="loss"
            self.playerBoard[x][y] = "M"
        else:
            #scan for mines
            self.playerBoard[x][y] = "?"
            sourrond = 0
            if self.isMine(x-1,y-1):
                sourrond += 1
            if self.isMine(x,y-1):
                sourrond += 1
            if self.isMine(x-1,y):
                sourrond += 1
            if self.isMine(x+1,y-1):
                sourrond += 1
            if self.isMine(x-1,y+1):
                sourrond += 1
            if self.isMine(x+1,y+1):
                sourrond += 1
            if self.isMine(x,y+1):
                sourrond += 1
            if self.isMine(x+1,y):
                sourrond += 1



            if sourrond == 0:
                #if you are a blank space
                self.playerBoard[x][y] = "-"
                self.tryToDig(x + 1,y)
                self.tryToDig(x - 1, y)
                self.tryToDig(x, y+1)
                self.tryToDig(x, y - 1)
                self.tryToDig(x + 1, y-1)
                self.tryToDig(x - 1, y + 1)
                self.tryToDig(x - 1, y - 1)
                self.tryToDig(x + 1, y + 1)
                return
            else:
                #add number
                self.playerBoard[x][y] = str(sourrond)






    def isGameOver(self) -> str:
        #check for win
        for x in range(0, len(self.mineBoard)):
            for y in range(0, len(self.mineBoard[0])):
                if self.playerBoard[x][y] == 'F' or self.playerBoard[x][y] == ' ':
                    if not( self.isMine(x,y)):
                        #just retun the current status
                        return  self.status

        return "win"

