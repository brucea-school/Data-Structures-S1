import manim
class SquareToCircle(manim.Scene):
    def construct(self):
        circle = manim.Circle()
        circle.set_fill(manim.BLUE, opacity=0.5)
        circle.set_stroke(manim.BLUE_E, width=4)

        self.add(circle)

