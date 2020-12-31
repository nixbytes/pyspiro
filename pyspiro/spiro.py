# A class that draws a Spirograph
import turtle
import math
from datetime import datetime
from fractions import gcd


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

    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.col = col
        self.R = R
        self.r = r
        self.l = l
        """
        Reduce r/R to the smallest form by Dividing with the
        GCD (Greatest Command Divisor )
        """
        gcd_val = gcd(self.r, self.R)
        self.nRot = self.r // self.R

        # Ratio of Radii

        self.k = r / float(R)
        self.t.color(*col)
        self.a = 0

    def restart(self):
        self.drawing_complete = False
        self.t.showturtle()
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        """
        Equation for SpiroGraph
        The mathical model:

        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) + l * k * math.sin((1 - k) * a / k))
        
        These curves are called hypotrochoids and epitrochoids. 

        """
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) + l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()