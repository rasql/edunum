# 4b Color Transparency
from p5 import *

class Demo(App):

    def setup(self):
        size(200, 200)
        background(0)
        noStroke()
        
        fill(0, 0, 255)
        rect(0, 0, 100, 200)
        
        # 255 means 100% opacity.
        fill(255, 0, 0, 255)
        rect(0, 0, 200, 40)

        # 75% opacity.
        fill(255, 0, 0, 191)
        rect(0, 50, 200, 40)

        # 55% opacity.
        fill(255, 0, 0, 127)
        rect(0, 100, 200, 40)

        # 25% opacity.
        fill(255, 0, 0, 63)
        rect(0, 150, 200, 40)

Demo().run()
