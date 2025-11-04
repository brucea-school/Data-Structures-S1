from graphics import *
import random
import math

def rgb_to_hex(r, g, b):
    """
    Converts RGB color values (0-255) to a hexadecimal string.
    """
    return "#{:02X}{:02X}{:02X}".format(int(r), int(g), int(b))
def randomTree(r,len,size,x,y,dir,first=False):
    if r <= 0:
        return
    randomNumThing = ((math.pi/10)*2)*random.random()-(math.pi/10)
    if first:
        randomNumThing = 0
    nextPoint = Point(
        x + (len * math.sin(dir + randomNumThing)),
        y + (len * math.cos(dir + randomNumThing))
    )
    Line(Point(x, y), nextPoint)._draw(win, {"width": size,"fill":"black"})

    randomTree(r - 1, len / 1.5, size / 1.5, nextPoint.x, nextPoint.y, dir - (math.pi / 4))
    randomTree(r - 1, len / 1.5, size / 1.5, nextPoint.x, nextPoint.y, dir)
    randomTree(r - 1, len / 1.5, size / 1.5, nextPoint.x, nextPoint.y, dir + (math.pi / 4))


win = GraphWin("My Circle", 1000, 1000)  # Creates a window 1000 x 800 pixels
win.setBackground("white")


randomTree(20,-200,20,500,800,0,True)

win.getMouse()  # Pause to view result
win.close()  # Close window when done

