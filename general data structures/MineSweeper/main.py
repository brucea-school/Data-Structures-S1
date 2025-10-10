"""
I RECOMMEND CHANGING YOUR TERMINAL FONT HEIGHT TO 0.6 FOR BETTER READABILITY
"""

from board import *
import time # Import time for AI delay

print(RED_BG+"HEY!"+RESET)
print(RED_TEXT+"I RECOMMEND CHANGING YOUR TERMINAL FONT HEIGHT TO 0.6 FOR BETTER READABILITY")
print("see Settings > Editor > Console Scheme > Console Font"+RESET)
print("\n"*3)

print("input board size " + GRAY_TEXT + "(must be more than 10 and less than 100):" + RESET)
try:
    size = int(input())
except ValueError:
    print(RED_BG + "Invalid input. Using default size 10." + RESET)
    size = 10

print("input board mines#:")
try:
    mines = int(input())
except ValueError:
    print(RED_BG + "Invalid input. Using default mines 15." + RESET)
    mines = 15

# Ensure valid size/mine counts
size = max(10, min(100, size))
mines = max(1, min(size * size - 10, mines))

brd = Board(size, mines)

lastRoundStatus = ""

while brd.isGameOver() == "run":

    print("\n"*50)

    brd.printBoard()

    if lastRoundStatus != "":
        print(RED_BG+lastRoundStatus+RESET)
        lastRoundStatus = ""
    else:
        print()

    print("what do you want to do?:     "+GRAY_TEXT+"(you can type "+BOLD+"help"+RESET+GRAY_TEXT+" or "+BOLD+"AI"+RESET+GRAY_TEXT+" for automatic play)"+RESET)
    intake = input()

    # intake commands

    if intake.startswith("d"):
        try:
            xwant = int(input("x cord?:"))
            ywant = int(input("y cord?:"))
        except ValueError:
            lastRoundStatus = "Invalid coordinate input!"
            continue

        board_size = len(brd.mineBoard)
        if xwant < 0 or xwant >= board_size or ywant < 0 or ywant >= board_size:
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
                print("are you sure you want to dig there?"+GRAY_TEXT+"  type y to dig"+RESET)
                if input() == "y":
                    brd.tryToDig(xwant,ywant)
                else:
                    lastRoundStatus = RESET+MAGENTA_BG+"dig aborted!"+RESET
        else:
            lastRoundStatus = "CANT DIG THERE!"

    elif intake.startswith("f"):
        try:
            xwant = int(input("x cord?:"))
            ywant = int(input("y cord?:"))
        except ValueError:
            lastRoundStatus = "Invalid coordinate input!"
            continue

        board_size = len(brd.mineBoard)
        # Corrected range check: max index is board_size - 1
        if xwant < 0 or xwant >= board_size or ywant < 0 or ywant >= board_size:
            lastRoundStatus = "OUT OF RANGE"
        elif brd.playerBoard[xwant][ywant] == "F":
            brd.playerBoard[xwant][ywant] = " "
            lastRoundStatus = RESET+BLUE_BG+"Flag removed"+RESET
        elif brd.playerBoard[xwant][ywant] == " ":
            brd.playerBoard[xwant][ywant] = "F"
            lastRoundStatus = RESET + BLACK_TEXT + YELLOW_BG + "Flag added" + RESET
        else:
            lastRoundStatus = "UNABLE TO FLAG THERE!"

    # --- AI Command Implementation ---
    elif intake.startswith("AI"):
        moved = True

        print("\n"*50)
        print(CYAN_BG + BLACK_TEXT + "AI playing... (Press Ctrl+C to stop)" + RESET)

        # Loop until no deterministic move is found or the game ends
        while moved and brd.isGameOver() == "run":
            moved, status_msg = brd.ai_move()

            if moved:
                # Clear screen and show board after each move
                print("\n"*50)
                brd.printBoard()
                print(CYAN_BG + BLACK_TEXT + status_msg + RESET)
                time.sleep(0.1) # Pause to see the move

        # After the loop finishes (either no moves or game over)
        if brd.isGameOver() != "run":
            lastRoundStatus = GREEN_BG + BLACK_TEXT + "AI finished the game! Status: " + brd.isGameOver().upper() + RESET
        else:
            lastRoundStatus = YELLOW_BG + BLACK_TEXT + "AI stopped: No more deterministic moves found. Manual intervention required." + RESET
    # --- End AI Command ---

    elif intake.startswith("e"):
        print("\n"*100)
        print("GOOD BYE!!!")
        exit("fun fact: you can have any value as a exit code")

    elif intake.startswith("help"):
        print("\n"*100)
        print(CYAN_TEXT+"💣MINESWEEPER💣"+ RESET + GRAY_TEXT + "           if you dont know how to play: look it up")
        print("")
        print(GREEN_TEXT+"COMMANDS"+RESET)
        print(BLUE_TEXT+"d - dig"+RESET)
        print(CYAN_TEXT + "dc - dig without confirm"+RESET)
        print(YELLOW_TEXT+"f - add/remove a flag"+RESET)
        print(MAGENTA_TEXT+"AI - let the computer play deterministically"+RESET)
        print(RED_TEXT+"e - leave"+RESET)
        input("press enter to continue")

    else:
        lastRoundStatus = "COMMAND DOSE NOT EXIST!"

# Final status display
brd.printBoard()
print("you "+brd.isGameOver())
