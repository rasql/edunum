# 1b Getting started: moving circle
from p5 import *

class Demo(App):
    def setup(self):
        size(480, 120)

    def draw(self):
        b = pygame.mouse.get_pressed()[0]
        if b:
            fill(0)
        else:
            fill(255)
        x, y = pygame.mouse.get_pos()
        ellipse(x, y, 80, 80)

Demo().run()