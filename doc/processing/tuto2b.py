# 2b Overview: hello mouse
from p5 import *

class Demo(App):
    def setup(self):
        size(400, 400)
        background(192, 64, 0)
        stroke(255)

    def draw(self):
        x, y = pygame.mouse.get_pos()
        line(150, 25, x, y)

Demo().run()