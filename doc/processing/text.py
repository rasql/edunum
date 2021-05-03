# Ref : text
from p5 import *

class Demo(App):
    def setup(self):
        textSize(32)
        text('word', 10, 30)
        fill(0, 102, 153)
        text('word', 10, 60)
        fill(0, 102, 153, 51)
        text('word', 10, 90)

Demo().run()