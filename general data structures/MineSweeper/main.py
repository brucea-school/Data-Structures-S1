from board import *

print("input board size(must be more than 10):")
size = int( input())
print("input board mines#:")
mines = int(input())

brd = Board(size,mines)

lastRoundStatus = ""

brd.playerBoard[4][6] = "F"

while brd.isGameOver() == "run":
    print("\n"*50)

    brd.printBoard()

    if lastRoundStatus != "":
        print(RED_BG+lastRoundStatus+RESET)
        lastRoundStatus = ""
    else:
        print()
    print("what do you want to do?:     "+GRAY_TEXT+"(you can type "+BOLD+"help"+RESET+GRAY_TEXT+" for help)"+RESET)
    intake = input()

    if intake.startswith("d"):
        xwant = int(input("x cord?:"))
        ywant = int(input("y cord?:"))


        if xwant < 0:
            lastRoundStatus = "OUT OF RANGE"
        elif xwant >= len(brd.mineBoard):
            lastRoundStatus = "OUT OF RANGE"
        elif ywant < 0:
            lastRoundStatus = "OUT OF RANGE"
        elif ywant >= len(brd.mineBoard):
            lastRoundStatus = "OUT OF RANGE"
        elif brd.playerBoard[xwant][ywant] == "F":
            lastRoundStatus = BOLD+"OOPS!"+RESET+RED_BG+" looks like ("+str(xwant)+","+str(ywant)+") is flagged! command ingnored"
        elif brd.playerBoard[xwant][ywant] == " ":
            if intake.find("c") != -1:
                brd.tryToDig(xwant, ywant)
            else:
                print("\n"*50)
                brd.playerBoard[xwant][ywant] = "?"
                brd.printBoard()
                brd.playerBoard[xwant][ywant] = " "
                print("are you sure you want to dig there?"+GRAY_TEXT+"  type y to dig"+RESET)
                if input() == "y":
                    brd.tryToDig(xwant,ywant)
                else:
                    lastRoundStatus = RESET+MAGENTA_BG+"dig aborted!"+RESET
        else:
            lastRoundStatus = "CANT DIG THERE!"
    elif intake.startswith("f"):
        xwant = int(input("x cord?:"))
        ywant = int(input("y cord?:"))

        if xwant < 0:
            lastRoundStatus = "OUT OF RANGE"
        elif xwant >= len(brd.mineBoard)-1:
            lastRoundStatus = "OUT OF RANGE"
        elif ywant < 0:
            lastRoundStatus = "OUT OF RANGE"
        elif ywant >= len(brd.mineBoard)-1:
            lastRoundStatus = "OUT OF RANGE"
        elif brd.playerBoard[xwant][ywant] == "F":
            brd.playerBoard[xwant][ywant] = " "
            lastRoundStatus = RESET+BLUE_BG+"Flag removed"+RESET
        elif brd.playerBoard[xwant][ywant] == " ":
            brd.playerBoard[xwant][ywant] = "F"
            lastRoundStatus = RESET + BLACK_TEXT + YELLOW_BG + "Flag added" + RESET
        else:
            lastRoundStatus = "UNABLE TO FLAG THERE!"
    elif intake.startswith("help"):
        #TODO!!!
        pass
    else:
        lastRoundStatus = "COMMAND DOSE NOT EXIST!"
brd.printBoard()
print("you "+brd.isGameOver())



