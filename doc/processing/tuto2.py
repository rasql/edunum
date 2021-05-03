# 2 Overview: line
from p5 import *

class Demo(App):
    def setup(self):
        size(400, 400)
        background(192, 64, 0)
        stroke(255)
        line(150, 25, 270, 350)

Demo().run()