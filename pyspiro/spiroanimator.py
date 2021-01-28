# a class for animating spirograph
class Spiro_Animator:
    def __init__(self, N):
        # set the timer value in milliseconds and get the window dimensions
        self.width = turtle.window_width()
        self.wheight = turtle.window_height
        self.spiros = []
        for i in range(N):
            # generate random parameters and set the spiro parameters
            rparams = self.genRandomParams
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            turtle.ontimer(self.update, self.deltaT)

    def genRandomParams(self):
        width, height = self.width, self.heigth
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

    def saveDrawing():
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
