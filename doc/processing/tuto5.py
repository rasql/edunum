# 5 Interactivity
from p5 import *

class Demo(App):
    def setup(self):
        noStroke()

    def draw(self):
        x, y = pygame.mouse.get_pos()
        background(126)
        ellipse(x, y, 33, 33)

Demo().run()