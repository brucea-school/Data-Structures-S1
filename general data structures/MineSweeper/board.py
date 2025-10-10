import math
import os
import random
import sys

# Set high recursion limit for deep recursive digs of safe spaces
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
        self.mineBoard = [' '] * x
        self.startingMineAmt = mines
        # self.flags is now removed as flags are calculated dynamically
        self.status = "run"

        for i in range(0, len(self.mineBoard)):
            self.mineBoard[i] = [False] * x

        i = 0

        # Place mines randomly
        while i < self.startingMineAmt:
            ex = random.randint(0, len(self.mineBoard) - 1)
            ey = random.randint(0, len(self.mineBoard[0]) - 1)
            if not self.isMine(ex, ey):
                self.mineBoard[ex][ey] = True
                i += 1

        # make player board
        self.playerBoard = [' '] * x

        for i in range(0, len(self.playerBoard)):
            self.playerBoard[i] = [' '] * x

    def count_flags(self) -> int:
        """Counts the total number of flags currently placed on the player board."""
        count = 0
        for r in range(len(self.playerBoard)):
            for c in range(len(self.playerBoard[0])):
                if self.playerBoard[r][c] == 'F':
                    count += 1
        return count

    def printBoard(self):

        # print face
        if (self.isGameOver() == "run"):
            print("🙂")
        elif (self.isGameOver() == "loss"):
            print("😵")
        else:
            print("😎")

        current_flags = self.count_flags()
        minesLeft = str(self.startingMineAmt - current_flags)

        # Mine counter display
        if len(minesLeft) == 1:
            print(BLACK_BG + RED_TEXT + "00" + minesLeft[0] + RESET)
        elif len(minesLeft) == 2:
            print(BLACK_BG + RED_TEXT + "0" + minesLeft[0] + minesLeft[1] + RESET)  # Fixed indexing here
        else:
            print(BLACK_BG + RED_TEXT + minesLeft + RESET)
        print()

        # print numbers for columns
        size = len(self.playerBoard)

        # Determine prefix spacing for rows
        prefix_len = len(str(size - 1))
        prefix = " " * prefix_len
        print(prefix + " ", end="")

        # Print column coordinate part 1 (tens digit)
        if size > 10:
            for i in range(size):
                print(str(i).zfill(2)[0], end="")
            print()
            print(prefix + " ", end="")

        # Print column coordinate part 2 (ones digit)
        for i in range(size):
            print(str(i).zfill(2)[-1], end="")
        print()

        # Print the board content
        for y in range(size):
            # Print row coordinate (y-axis)
            print(str(y).zfill(prefix_len), end=' ')

            for x in range(size):
                # print actual board
                cell = self.playerBoard[x][y]
                if cell == " ":
                    print(GRAY_BG + " " + RESET, end='')
                elif cell == "-":
                    print(BLACK_BG + " " + RESET, end='')
                elif cell == "F":
                    # Use a flag symbol
                    print(RED_TEXT + GRAY_BG + "⚑" + RESET, end='')
                elif str(cell) == "1":
                    print(BLACK_BG + BLUE_TEXT + "1" + RESET, end='')
                elif str(cell) == "2":
                    print(BLACK_BG + GREEN_TEXT + "2" + RESET, end='')
                elif str(cell) == "3":
                    print(BLACK_BG + RED_TEXT + "3" + RESET, end='')
                elif str(cell) == "4":
                    print(BLACK_BG + MAGENTA_TEXT + "4" + RESET, end='')
                elif str(cell) == "5":
                    print(BLACK_BG + RED_TEXT + BOLD + "5" + RESET, end='')
                elif str(cell) == "6":
                    print(BLACK_BG + CYAN_TEXT + "6" + RESET, end='')
                elif str(cell) == "7":
                    print(BLACK_BG + GRAY_TEXT + "7" + RESET, end='')
                elif str(cell) == "8":
                    print(BLACK_BG + GRAY_TEXT + BOLD + "8" + RESET, end='')
                elif str(cell) == "M":
                    print(RED_BG + WHITE_TEXT + BOLD + "!" + RESET, end='')
                elif str(cell) == "?":
                    print(YELLOW_BG + BLACK_TEXT + BOLD + BLINK + "#" + RESET, end='')

            # Print row coordinate again on the right
            print(str(y).zfill(prefix_len))

        # Print column coordinates again at the bottom
        print(prefix + " ", end="")
        if size > 10:
            for i in range(size):
                print(str(i).zfill(2)[0], end="")
            print()
            print(prefix + " ", end="")

        for i in range(size):
            print(str(i).zfill(2)[-1], end="")
        print()

    def isMine(self, x: int, y: int):
        """Checks if a coordinate is within bounds and contains a mine."""
        if x < 0 or x >= len(self.mineBoard):
            return False
        if y < 0 or y >= len(self.mineBoard[0]):
            return False
        return self.mineBoard[x][y]

    def tryToDig(self, x: int, y: int):
        """
        Attempts to dig a cell. Handles game state changes and recursive
        expansion for safe '-' cells.
        """
        # is out of range?
        if x < 0 or x >= len(self.mineBoard) or y < 0 or y >= len(self.mineBoard[0]):
            return

        # are you checked already or flagged?
        if not (self.playerBoard[x][y] == ' ' or self.playerBoard[x][y] == 'F'):
            return

        # If flagged, do not dig (AI should not attempt this, but safety check)
        if self.playerBoard[x][y] == 'F':
            return

        if self.isMine(x, y):
            # KABOOM!
            self.status = "loss"
            self.playerBoard[x][y] = "M"
        else:
            # scan for mines in neighbors
            self.playerBoard[x][y] = "?"  # Temporary set to prevent infinite recursion
            sourrond = 0

            # Iterate through all 8 neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if self.isMine(x + dx, y + dy):
                        sourrond += 1

            if sourrond == 0:
                # if you are a blank space ('-'), recursively dig neighbors
                self.playerBoard[x][y] = "-"
                # Recursive dig on all 8 neighbors
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        self.tryToDig(x + dx, y + dy)
            else:
                # add number
                self.playerBoard[x][y] = str(sourrond)

    def isGameOver(self) -> str:
        """Checks for win (all non-mine cells are dug) or loss."""
        if self.status == "loss":
            return "loss"

        # check for win
        # The game is won if every non-mine cell is revealed.
        for x in range(0, len(self.mineBoard)):
            for y in range(0, len(self.mineBoard[0])):
                is_mine = self.isMine(x, y)
                # is_revealed means the cell is not ' ' (unscanned) or 'F' (flagged)
                is_revealed = self.playerBoard[x][y] not in (' ', 'F')

                if not is_mine and not is_revealed:
                    # Found an unrevealed safe spot, game is still running
                    return self.status

        # If we reached here, all non-mine cells are revealed (or only flags remain on mine spots)
        return "win"

    def get_neighbors(self, x: int, y: int) -> list:
        """Returns a list of valid neighbor (nx, ny) coordinates."""
        neighbors = []
        size = len(self.playerBoard)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    neighbors.append((nx, ny))
        return neighbors

    def get_neighbor_status(self, x: int, y: int) -> tuple:
        """
        Analyzes neighbor status for a cell.
        Returns: (flagged_count, unopened_count, unopened_coords)
        """
        neighbors = self.get_neighbors(x, y)
        flagged = 0
        unopened = 0
        unopened_coords = []

        for nx, ny in neighbors:
            cell = self.playerBoard[nx][ny]
            if cell == 'F':
                flagged += 1
            # Unopened means ' ' (unscanned)
            elif cell == ' ':
                unopened += 1
                unopened_coords.append((nx, ny))

        return flagged, unopened, unopened_coords

    def ai_move(self) -> tuple[bool, str]:
        """
        The core AI logic. Executes one deterministic move or makes a random guess.
        Returns: (was_move_made, status_message)
        """
        size = len(self.playerBoard)

        # 1. First move (Random dig if the board is completely empty)
        is_empty = all(self.playerBoard[r][c] == ' ' for r in range(size) for c in range(size))
        if is_empty:
            rx, ry = random.randint(0, size - 1), random.randint(0, size - 1)
            self.tryToDig(rx, ry)

            if self.status == "loss":
                return False, "AI: Lost on first random dig at ({},{})".format(rx, ry)

            return True, "AI: Initial random dig at ({},{})".format(rx, ry)

        # 2. Apply deterministic logic (Rule 1 & Rule 2)
        # We store moves to make sure we only make one move per call to avoid infinite recursion/loops.
        moves_to_make = []

        for r in range(size):
            for c in range(size):
                cell = self.playerBoard[r][c]

                # Only analyze cells that contain a number
                if cell.isdigit():
                    mine_count = int(cell)
                    flagged, unopened, unopened_coords = self.get_neighbor_status(r, c)

                    # Rule 1: Guaranteed Mine (Flagging)
                    mines_remaining_to_find = mine_count - flagged
                    if mines_remaining_to_find > 0 and mines_remaining_to_find == unopened:
                        # Add flagging moves
                        for nx, ny in unopened_coords:
                            moves_to_make.append(('flag', nx, ny))
                        # Only execute the first move found and return
                        if moves_to_make:
                            break

                    # Rule 2: Guaranteed Safe Dig (Saturated)
                    # If all surrounding mines are already flagged (flagged == N),
                    # all remaining unopened cells must be safe.
                    elif flagged == mine_count and unopened > 0:
                        # Add digging moves
                        for nx, ny in unopened_coords:
                            moves_to_make.append(('dig', nx, ny))
                        # Only execute the first move found and return
                        if moves_to_make:
                            break
            if moves_to_make:
                break

        # Execute the first deterministic move found, if any
        if moves_to_make:
            action, x, y = moves_to_make[0]

            if action == 'flag':
                # Check if it's already flagged by another rule application in this turn (unlikely but safe)
                if self.playerBoard[x][y] == ' ':
                    self.playerBoard[x][y] = 'F'
                    return True, "AI: Flagged ({},{}) deterministically (Rule 1)".format(x, y)

            elif action == 'dig':
                # Digging might trigger recursive tries, which is fine
                if self.playerBoard[x][y] == ' ':
                    self.tryToDig(x, y)

                    # Check if we lost after the dig
                    if self.status == "loss":
                        return False, "AI: Lost by digging a mine at ({},{}) (Rule 2 failure)".format(x, y)

                    return True, "AI: Dug ({},{}) deterministically (Rule 2)".format(x, y)

        # 3. No deterministic move found: Make a random guess (as requested)
        unopened_safe_cells = []
        for r in range(size):
            for c in range(size):
                if self.playerBoard[r][c] == ' ':  # Only look for unopened, unflagged spots
                    unopened_safe_cells.append((r, c))

        if unopened_safe_cells:
            # Make a random guess from available unopened cells
            rx, ry = random.choice(unopened_safe_cells)
            self.tryToDig(rx, ry)

            # Check if we lost immediately after the guess
            if self.status == "loss":
                return False, "AI: Lost by guessing a mine at ({},{})".format(rx, ry)

            return True, "AI: Guessed randomly at ({},{})".format(rx, ry)

        # 4. If no moves were made (deterministic or guess), it means the board is solved (all non-mines are revealed)
        return False, "AI: No moves left to make (Board solved or stuck)."
