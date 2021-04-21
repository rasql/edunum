# Ref : text
from p5 import *

class Demo(App):
    def setup(self):
        size(400, 300)
        
    def draw(self):
        background(127)
        fill(255)
        triangle(30, 75, 58, 20, 86, 75)
        fill(255, 0, 0, 127) 
        triangle(10, 15, 70, 30, 46, 85)
        x, y = pygame.mouse.get_pos()
        triangle(x+10, y+15, x+70, y+30, x+46, y+85)

Demo().run()