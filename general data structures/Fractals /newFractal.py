
from graphics import *
import math
win = GraphWin("My Circle", 1000*math.sqrt(3), 1000*2)  # Creates a window 1000 x 800 pixels
win.setBackground("white")


def theCube(r, x, first=True, plusBoxPos=None,vary=None):
    if r <= 0:
        return None

    if plusBoxPos is None:
        plusBoxPos = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]
    if vary is None:
        vary = [1,1,1,1]

    if first:
        #WE ARE DOING RED TEXT
        b = math.floor(math.sqrt(3)*x)
        Line(Point(0, x/2), Point(b/2,0))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(b/2,0), Point(b, x/2))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(0, x / 2), Point(b/2, x))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(b/2,x), Point(b, x/2))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(b, x/2), Point(b, x*1.5))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(b,x*1.5), Point(b/2,x*2))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(b/2,x*2), Point(0, x*1.5))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(b / 2, x*2), Point(b/2,x))._draw(win, {"width": 1, "fill": "black"})
        Line(Point(0, x*1.5), Point(0, x/2))._draw(win, {"width": 1, "fill": "black"})
        theCube(r, x, first=False, plusBoxPos=[Point(0, x/2),Point(b/2,x),Point(0, x*1.5),Point(b/2,x*2)], vary=vary)
        theCube(r, x, first=False,
                plusBoxPos=[Point(b, x / 2), Point(b / 2, x), Point(b/2,0), Point(0,x/2)], vary=vary)
        theCube(r, x, first=False,
                plusBoxPos=[Point(b, x / 2), Point(b / 2, x), Point(b, x * 1.5), Point(b / 2, x * 2)], vary=vary)
    else:
        l0 = Line(plusBoxPos[0],plusBoxPos[1])
        l1 = Line(plusBoxPos[2], plusBoxPos[3])
        rl0 = Line(l0.getCenter(),l1.getCenter())

        l2 = Line(plusBoxPos[0], plusBoxPos[2])
        l3 = Line(plusBoxPos[1], plusBoxPos[3])
        rl1 = Line(l2.getCenter(), l3.getCenter())

        rl0._draw(win,{"width": 1, "fill": "black"})
        rl1._draw(win,{"width": 1, "fill": "black"})

        theCube(r-vary[0], x, first=False, plusBoxPos=[l0.getCenter(),plusBoxPos[1],rl0.getCenter(),l3.getCenter()], vary=vary)
        theCube(r - vary[1], x, first=False, plusBoxPos=[l2.getCenter(), rl0.getCenter(), plusBoxPos[2], l1.getCenter()], vary=vary)
        theCube(r - vary[2], x, first=False, plusBoxPos=[plusBoxPos[0], l0.getCenter(), l2.getCenter(),rl0.getCenter()], vary=vary)
        theCube(r - vary[3], x, first=False, plusBoxPos=[rl0.getCenter(), l3.getCenter(), l1.getCenter(), plusBoxPos[3]], vary=vary)







"""
vary key
2 | 0
- + -
1 | 3

"""

theCube(10,500,vary=[1,999,999,999])

win.getMouse()  # Pause to view result
win.close()  # Close window when done







