# Ref : text
from p5 import *

class Demo(App):
    def setup(self):
        background(0)
        stroke(255)
        line(50, 0, 50, 100)
        textSize(16)
        textAlign(RIGHT)
        text("ABCD", 50, 30)
        textAlign(CENTER)
        text("EFGH", 50, 50)
        textAlign(LEFT)
        text("IJKL", 50, 70)

Demo().run()