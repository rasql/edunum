# 5 Interactivity move 3 disks
from p5 import *

class Demo(App):
    def setup(self):
        noStroke()

    def draw(self):
        x, y = pygame.mouse.get_pos()
        background(126)
        ellipse(x, 16, 33, 33)   # Top circle
        ellipse(x+20, 50, 33, 33)   # Middle circle
        ellipse(x-20, 84, 33, 33)   # Bottom circle


Demo().run()