from board import *

c = Board(100,5000,)

print(len(c.mineBoard))
print(len(c.playerBoard))


c.tryToDig(20,20)



c.printBoard()


