# 2d Overview: hello mouse with mouse press background erase
from p5 import *

global width, height

class Demo(App):
    def setup(self):
        size(400, 400)
        stroke(255)
        ellipse(width/2, height/2, 50, 50)

    def draw(self):
        x, y = pygame.mouse.get_pos()
        line(150, 25, x, y)
        
    def mousePressed(self):
        background(192, 64, 0)
        
Demo().run()