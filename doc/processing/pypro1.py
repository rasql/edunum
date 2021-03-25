import pygame
from pygame.locals import *

screen = None
width = 640
height = 480

mousePressed = False
mouseX = 0
mouseY = 0

stroke = (0, 0, 0)

RED = 255, 0, 0

def background(*rgb):
    global bg
    
    if len(rgb) == 1:
        bg = (rgb) * 3
    else:
        bg = rgb
        
    screen.fill(bg)
    

def keyPressed():
    pass


def size(w, h):
    global width, hight, screen
    
    width = w
    height = h
    screen = pygame.display.set_mode((w, h))
    print(w, h)

def set_up():
    print('set up')
    size(500, 500)
    print(screen)

set_up()

def line(x0, y0, x1, y1):
    pygame.draw.line(screen, RED, (x0, y0), (x1, y1))

def rect(x, y, w, h):
    pygame.draw.rect(screen, RED, (x-w/2, y-h/2, w, h), 1)
    
    
def ellipse(x, y, a, b):
    pygame.draw.ellipse(screen, RED, (x-a/2, y-b/2, a, b), 1)

    
def draw():
    background(100, 0, 0)    
#     line(0, 0, width, height)
#     line(0, height, width, 0)
#     ellipse(width/2, height/2, 200, 100)
#     
#     
#     rect(100, 100, 20, 100)
#     ellipse(100, 70, 60, 60)
#     ellipse(81, 70, 16, 32)
#     ellipse(119, 70, 16, 32) 
#     line(90, 150, 80, 160)
#     line(110, 150, 120, 160)

    if mousePressed:
        fill(0):
    else:
        fill(255)
    
    ellipse(mouseX, mouseY, 80, 80)

pygame.init()
set_up()
# screen = pygame.display.set_mode((640, 480))
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            print('quit')
            running = False
        
        elif event.type == MOUSEBUTTONDOWN:
            mousePressed = True
            
        elif event.type == MOUSEBUTTONUP:
            mousePressed = False
            
        elif event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
            
            
    draw()
    pygame.display.update()
        
        
pygame.quit()