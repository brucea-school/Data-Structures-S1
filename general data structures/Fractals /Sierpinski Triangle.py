
from graphics import *

def fractal_triangle(d, x1, y1, x2, y2, x3, y3):
   if d == 0:
       return
   else:
       Line(Point(x1, y1), Point(x2, y2)).draw(win)
       Line(Point(x1, y1), Point(x3, y3)).draw(win)
       Line(Point(x2, y2), Point(x3, y3)).draw(win)
       fractal_triangle(d - 1, x1, y1, (x1 + x2) / 2, (y1 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2)
       fractal_triangle(d - 1, x2, y2, (x1 + x2) / 2, (y1 + y2) / 2, (x2 + x3) / 2, (y2 + y3) / 2)
       fractal_triangle(d - 1, x3, y3, (x1 + x3) / 2, (y1 + y3) / 2, (x2 + x3) / 2, (y2 + y3) / 2)



win = GraphWin("My Circle", 1000, 800)  # Creates a window 1000 x 800 pixels
win.setBackground("white")

fractal_triangle(7, 100, 700, 500, 100, 900, 700)


win.getMouse()  # Pause to view result
win.close()  # Close window when done




