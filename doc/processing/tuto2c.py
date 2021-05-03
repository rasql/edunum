# 2c Overview: hello mouse with background erase
from p5 import *

class Demo(App):
    def setup(self):
        size(400, 400)
        stroke(255)

    def draw(self):
        x, y = pygame.mouse.get_pos()
        background(192, 64, 0)
        line(150, 25, x, y)

Demo().run()