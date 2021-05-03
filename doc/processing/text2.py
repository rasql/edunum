# Ref : text
from p5 import *

headlines = [ "Processing downloads break downloading record.", 
              "New study shows computer programming lowers cholesterol."]


class Demo(App):
# A list of news headlines

    def setup(self):
        global f, x, index
        
        size(400,200)
        #f = createFont("Arial", 16, True)
        
        f = pygame.font.SysFont('Courier', 16)
        
        # Initialize headline offscreen to the right 
        x = width 
        index = 0

    def draw(self):
        global f, x, index, headlines, font
        background(255)
        fill(0)

        # Display headline at x  location
        textFont(f, 16)       
        textAlign(LEFT)
        text(headlines[index], x, 180)

        # Decrement x
        x = x - 3

        # If x is less than the negative width, 
        # then it is off the screen
        #w = textWidth(headlines[index])
        w, h = font.size()
        if (x < -w):
            x = width 
            index = (index + 1) % len(headlines)
Demo().run()
