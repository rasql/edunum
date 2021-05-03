# 1 Getting started: draw a circle
from p5 import *

class Demo(App):

    def draw(self):
        ellipse(50, 50, 80, 80)

Demo().run()