
from graphics import *
import random
import math
win = GraphWin("My Circle", 1000, 800)  # Creates a window 1000 x 800 pixels
win.setBackground("white")

from queue import *
q = Queue()
q.enqueue([9,-200,20,500,800,0,True,False])

while not q.empty():
    #r,len,size,x,y,dir,first=False, perfect=False
    q0 = q.dequeue()
    r = q0[0]
    len = q0[1]
    size = q0[2]
    x = q0[3]
    y = q0[4]
    dir = q0[5]
    first = q0[6]
    perfect = q0[7]


    if r <= 0:
        continue
    randomNumThing = ((math.pi / 10) * 2) * random.random() - (math.pi / 10)
    if first or perfect:
        randomNumThing = 0
    nextPoint = Point(
        x + (len * math.sin(dir + randomNumThing)),
        y + (len * math.cos(dir + randomNumThing))
    )
    if r < 5:
        Line(Point(x, y), nextPoint)._draw(win, {"width": size, "fill": "green"})
    else:
        Line(Point(x, y), nextPoint)._draw(win, {"width": size, "fill": "burlywood4"})

    q.enqueue([r - 1, len / 1.5 + random.random() / 2, size / 1.5 + random.random() / 2, nextPoint.x, nextPoint.y, dir - (math.pi / 4), False, perfect])
    q.enqueue([r - 1, len / 1.5 + random.random() / 2, size / 1.5 + random.random() / 2, nextPoint.x, nextPoint.y, dir + (math.pi / 4), False, perfect])
    q.enqueue([r - 1, len / 1.5 + random.random() / 2, size / 1.5 + random.random() / 2, nextPoint.x, nextPoint.y, dir, False, perfect])
    q.enqueue([r - 1, len / 1.2, size / 1.2, nextPoint.x, nextPoint.y, dir+(randomNumThing*random.random()), False, perfect])


win.getMouse()  # Pause to view result
win.close()  # Close window when done