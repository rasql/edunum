# 5 Interactivity move 3 disks
from p5 import *

class Demo(App):
    def setup(self):
        noStroke()

    def draw(self):
        x, y = pygame.mouse.get_pos()
        background(126)
        ix = width - x   # Inverse X
        iy = height - y   # Inverse Y
        background(126)
        fill(255, 150)
        ellipse(x, height/2, y, y)
        fill(0, 159)
        ellipse(ix, height/2, iy, iy)


Demo().run()