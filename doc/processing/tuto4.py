# 4 Color
from p5 import *

class Demo(App):

    def draw(self):
        background(150)
        stroke(0)
        line(0, 0, 100, 100)
        stroke(255)
        noFill()
        rect(50, 50, 50, 50)

Demo().run()
