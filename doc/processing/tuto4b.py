# 4b RGB color
from p5 import *

class Demo(App):

    def draw(self):
        background(255)
        noStroke()

        # Bright red
        fill(255, 0, 0)
        ellipse(20, 20, 20, 20)

        # Dark red
        fill(127, 0, 0)
        ellipse(50, 20, 20, 20)

        # Pink (pale red)
        fill(255, 200, 200)
        ellipse(80, 20, 20, 20)

Demo().run()
