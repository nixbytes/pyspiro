import sys, random, argparse
import numpy as np
import math
import turtle
from PIL import Image
from datetime import datetime

# from fractions import gcd


# import spiro
# import spiroanimator


# A class that draws a Spirograph


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
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
        gcd_val = math.gcd(self.r, self.R)
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

    def draw(self):
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) + l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
            self.t.hideturtle()

    def update(self):
        if self.drawing_complete:
            return
        self.a += self.step
        R, k, l = self.R, self.k, self.l

        a = math.radians(self.a)
        x = self.R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            self.t.hideturtle()

    def clear(self):
        self.t.clear()


# a class for animating spirograph
class Spiro_Animator:
    def __init__(self, N):
        # set the timer value in milliseconds and get the window dimensions
        self.deltaT = 10
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = []
        for i in range(N):
            # generate random parameters and set the spiro parameters
            rparams = self.genRandomParams()
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            turtle.ontimer(self.update, self.deltaT)

    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width // 2, width // 2)
        yc = random.randint(-height // 2, height // 2)

        col = (random.random(), random.random(), random.random())
        return (xc, yc, col, R, r, l)

    # restart method for the program

    def restart(self):

        for spiro in self.spiros:

            spiro.clear()
            rparams = self.genRandomParams()

            spiro.setparams(*rparams)
            spiro.restart()

    def update(self):
        # update spiro and count completion on spiros
        # also restart once completed
        nComplete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawingComplete:
                nComplete += 1
        if nComplete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtle(self):
        # turtle cursor on and off
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

    def saveDrawing(self):
        # Drae an PNG and hide the cursor
        # in addition get the tkinter canvas and
        # Pillow mode to convert
        turtle.hideturtle()
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = "spiro-" + dateStr
        print("saving drawing to %s.eps/png" % fileName)
        # Save drawing to a postscipt image and pillow mod
        # to convert it to png
        canvas = turtle.getcanvas()
        canvas.postscript(file=fileName + ".eps")
        img = Image.open(fileName + ".eps")
        img.save(fileName + ".png", "png")

        turtle.showturtle()


def main():
    print("generating spirograph...")

    descStr = """The program draws Spiropgraph using the Turtle Modules.
    When run with no arguments, this program draws random Spirographs.

    Terminology:

    R: radius of outer circle
    r: radius of inner circle
    l: ratio of hole distance to r


    """
    parser = argparse.ArgumentParser(description=descStr)

    parser.add_argument(
        "--sparam",
        nargs=3,
        dest="sparams",
        required=False,
        help="The three arguments in sparams: R, r, l.",
    )

    args = parser.parse_args()

    turtle.setup(width=0.8)

    turtle.shape("turtle")

    turtle.title("Spirograph")

    turtle.onkey("saveDrawing", "s")

    turtle.listen()

    turtle.hideturtle()

    if args.sparams:
        params = [float(x) for x in args.sparams]

        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        sprio.draw()
    else:
        spiroAnim = Spiro_Animator(4)
        turtle.onkey(spiroAnim.toggleTurtle, "t")

        turtle.onkey(spiroAnim.restart, "space")

    turtle.mainloop()


if __name__ == "__main__":
    main()
