from board import *

c = Board(4,12,3)

c.playerBoard[2][0] = '1'
c.playerBoard[2][1] = '2'
c.playerBoard[2][2] = '3'
c.playerBoard[2][3] = '4'
c.playerBoard[2][4] = '5'
c.playerBoard[2][5] = '6'
c.playerBoard[2][6] = '7'
c.playerBoard[2][7] = '8'
c.playerBoard[2][8] = 'F'
c.playerBoard[3][4] = 'M'
c.playerBoard[3][5] = '?'

c.printBoard()

