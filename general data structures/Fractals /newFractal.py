
from graphics import *
import math
win = GraphWin("My Circle", 1000*math.sqrt(3), 1000*2)  # Creates a window 1000 x 800 pixels
win.setBackground("white")


def theCube(r, x, first=True, plusBoxPos=None,vary=None,wih=1.0,color="black"):
    """
    Creats a cube with some cool stuff
    :param r: repetition
    :param x: size of the side of the cube
    :param first: render cube?
    :param plusBoxPos: if not first then render a + between the 4 points provided
    :param vary: the - of all the 4 different regions
    :param wih: width of lines
    :param color: the color of the lines
    :return: nothing.
    """
    if r <= 0:
        return None

    if plusBoxPos is None:
        plusBoxPos = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]
    if vary is None:
        vary = [1,1,1,1]

    if first:
        #WE ARE DOING RED TEXT
        b = math.floor(math.sqrt(3)*x)
        Line(Point(0, x/2), Point(b/2,0))._draw(win, {"width": wih, "fill": color})
        Line(Point(b/2,0), Point(b, x/2))._draw(win, {"width": wih, "fill": color})
        Line(Point(0, x / 2), Point(b/2, x))._draw(win, {"width": wih, "fill": color})
        Line(Point(b/2,x), Point(b, x/2))._draw(win, {"width": wih, "fill": color})
        Line(Point(b, x/2), Point(b, x*1.5))._draw(win, {"width": wih, "fill": color})
        Line(Point(b,x*1.5), Point(b/2,x*2))._draw(win, {"width": wih, "fill": color})
        Line(Point(b/2,x*2), Point(0, x*1.5))._draw(win, {"width": wih, "fill": color})
        Line(Point(b / 2, x*2), Point(b/2,x))._draw(win, {"width": wih, "fill": color})
        Line(Point(0, x*1.5), Point(0, x/2))._draw(win, {"width": wih, "fill": color})
        theCube(r, x, first=False, plusBoxPos=[Point(0, x/2),Point(b/2,x),Point(0, x*1.5),Point(b/2,x*2)], vary=vary,wih=wih)
        theCube(r, x, first=False,
                plusBoxPos=[Point(b, x / 2), Point(b / 2, x), Point(b/2,0), Point(0,x/2)], vary=vary,wih=wih)
        theCube(r, x, first=False,
                plusBoxPos=[Point(b, x / 2), Point(b / 2, x), Point(b, x * 1.5), Point(b / 2, x * 2)], vary=vary,wih=wih)
    else:
        l0 = Line(plusBoxPos[0],plusBoxPos[1])
        l1 = Line(plusBoxPos[2], plusBoxPos[3])
        rl0 = Line(l0.getCenter(),l1.getCenter())

        l2 = Line(plusBoxPos[0], plusBoxPos[2])
        l3 = Line(plusBoxPos[1], plusBoxPos[3])
        rl1 = Line(l2.getCenter(), l3.getCenter())

        rl0._draw(win,{"width": wih, "fill": color})
        rl1._draw(win,{"width": wih, "fill": color})

        theCube(r-vary[0], x, first=False, plusBoxPos=[l0.getCenter(),plusBoxPos[1],rl0.getCenter(),l3.getCenter()], vary=vary,wih=wih)
        theCube(r - vary[1], x, first=False, plusBoxPos=[l2.getCenter(), rl0.getCenter(), plusBoxPos[2], l1.getCenter()], vary=vary,wih=wih)
        theCube(r - vary[2], x, first=False, plusBoxPos=[plusBoxPos[0], l0.getCenter(), l2.getCenter(),rl0.getCenter()], vary=vary,wih=wih)
        theCube(r - vary[3], x, first=False, plusBoxPos=[rl0.getCenter(), l3.getCenter(), l1.getCenter(), plusBoxPos[3]], vary=vary,wih=wih)







"""
vary key
2 | 0
- + -
1 | 3

show off:
1,999,999,999 - bad
1,1,999,999 - solid rock paper
1,2,999,999 - rock paper
1,4,2,2 - complex
1,2,3,3 - fancy complex
1,999,1,1 - sierpinski
1,2,1,1 - open gl be like
"""

theCube(10,500,vary=[1,2,1,1],wih=1)

win.getMouse()  # Pause to view result
win.close()  # Close window when done







