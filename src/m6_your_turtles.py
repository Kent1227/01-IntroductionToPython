"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Kent Smith.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg
import math

window = rg.TurtleWindow()
window.delay(0.5)


worden = rg.SimpleTurtle()
jack = rg.SimpleTurtle()
worden.pen = rg.Pen('red', 1)
jack.pen = rg.Pen('blue', 3)
worden.pen_up()
worden. forward(100)
worden.left(90)
worden.forward(100)
worden.left(90)
worden.pen_down()
jack.speed = 3
worden.speed = 4
for k in range(70):
    worden.forward(200)
    worden.left(90 + k)
    a = worden.x_cor() - jack.x_cor()
    b = worden.y_cor() - jack.y_cor()
    print(((180/3.1415265) * (math.atan(a / b))))
    jack.set_heading((90 * (k % 4)) + math.fabs(((180/3.1415265) * (math.atan(a / b)))))
    jack.forward(k)


