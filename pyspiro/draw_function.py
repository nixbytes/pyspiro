"""
Here is a simple python packages
"""

import math
import turtle


# Basic Draw function


def draw_circle_turle(x, y, r):
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in (0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


