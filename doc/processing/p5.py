import pygame
from pygame.locals import *

screen = None
width = 100
height = 100

mousePressed = False
mouseX = 0
mouseY = 0

LEFT = 0
CENTER = 1
RIGHT = 2
align = LEFT

size = 24
font = 'Otto'
#font = pygame.font.SysFont(None, 24)


stroke_col = 0, 0, 0
fill_col = 255, 255, 255
bg_col = 200, 200, 200
no_stroke = False
no_fill = False

def background(*rgb):
    global bg_col
    
    bg_col = rgb
    if len(rgb) == 1:
        bg_col = (rgb) * 3
        
    screen.fill(bg_col)


def fill(*rgb):
    global fill_col
    
    fill_col = rgb
    if len(rgb) == 1:
        fill_col = (rgb) * 3

        
def noFill():
    global fill_col
    fill_col = None
        

def stroke(*rgb):
    global stroke_col
    
    stroke_col = rgb
    if len(rgb) == 1:
        stroke_col = (rgb) * 3
        
def noStroke():
    global stroke_col
    stroke_col = None    

def size(w, h):
    global width, hight, screen
    
    width = w
    height = h
    screen = pygame.display.set_mode((w, h))
    screen.fill(bg_col)



def line(x0, y0, x1, y1):
    if stroke_col:
        pygame.draw.line(screen, stroke_col, (x0, y0), (x1, y1))


def rect(x, y, w, h):
    if fill_col:
        shape_surf = pygame.Surface(pygame.Rect(x, y, w, h).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, fill_col, shape_surf.get_rect())
        screen.blit(shape_surf, (w, h))
        
        pygame.draw.rect(screen, fill_col, (x, y, w, h), 0)
    if stroke_col:
        pygame.draw.rect(screen, stroke_col, (x, y, w, h), 1)
        
    print(fill_col)
    
    
def ellipse(x, y, a, b):
    if fill_col:
        pygame.draw.ellipse(screen, fill_col, (x-a/2, y-b/2, a, b), 0)
    if stroke_col:
        pygame.draw.ellipse(screen, stroke_col, (x-a/2, y-b/2, a, b), 1)


def text(s, x, y):
    global align
    
    w, h = font.size(s)
    if align == CENTER:
        x -= w/2
    elif align == RIGHT:
        x -= w
    
    img = font.render(s, True, fill_col)
    a = font.get_ascent()
    screen.blit(img, (x, y-a))
    

def textSize(size):
    global font
    font = pygame.font.SysFont(None, size)
    

def textAlign(a):
    global align
    align= a
    
def textFont(f, s):
    global font, size
    
    font = f
    font_size = s

class App:
    
    def __init__(self):
        global screen, font

        pygame.init()
        screen = pygame.display.set_mode((width, height))
        screen.fill(bg_col)
        font = pygame.font.SysFont(None, 24)
        
        self.running = True
        self.setup()

    def run(self):
    
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
                elif event.type == MOUSEBUTTONDOWN:
                    self.mousePressed()
                    
                elif event.type == MOUSEBUTTONUP:
                    pass
                    
                elif event.type == MOUSEMOTION:
                    global mouseX, mouseY
                    
                    mouseX, mouseY = event.pos
                
                
            self.draw()
            pygame.display.update()
                     
        pygame.quit()
        
    def setup(self):
        size(100, 100)
    
    def draw(self):
        pass
    
    def mousePressed(self):
        print('mouse pressed')


if __name__ == '__main__':
    print('testing p5')
    
    #App().run()
    
    class Demo(App):
        def setup(self):
            background(0)
            stroke(255)
            line(50, 0, 50, 100)
            textSize(16)
            textAlign(RIGHT)
            text("ABCD", 50, 30)
            textAlign(CENTER)
            text("EFGH", 50, 50)
            textAlign(LEFT)
            text("IJKL", 50, 70)

    Demo().run()
