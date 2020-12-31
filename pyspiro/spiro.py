# A class that draws a Spirograph
import turtle

class Spiro:
    def __init__(self, xc, yc, col, R, r, l) -> None:
        # Create Turtle Shape
        self.t = turtle.Turtle()

        self.t.shape("turtle")

        self.step = 5

        self.drawing_complete = False

        self.setparams(xc, yc, col, R, r, l)
        # initalize the drawing
        self.restart()

