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

CORNER = 0
CORNERS = 1
CENTER = 2
RADIUS = 3
r_mode = CORNER
e_mode = CENTER

size = 24
font = 'Otto'
#font = pygame.font.SysFont(None, 24)


stroke_col = 0, 0, 0
stroke_weight = 1
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
        
def strokeWeight(w):
    global stroke_weight
    
    stroke_weight = w
        
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

def rectMode(mode):
    global r_mode
    r_mode = mode

def rect(x, y, w, h):
    global r_mode
    print('r_mode', r_mode)
    if r_mode == CENTER:
        x -= w/2
        y -= h/2
    if fill_col:
        # https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame
        shape_surf = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, fill_col, shape_surf.get_rect())
        screen.blit(shape_surf, pygame.Rect(x, y, w, h))
        
    if stroke_col:
        pygame.draw.rect(screen, stroke_col, (x, y, w, h), stroke_weight)
        print(stroke_col)
        
def ellipseMode(mode):
    global e_mode
    e_mode = mode    

def ellipse(x, y, w, h):
    if e_mode == CENTER:
        x -= w/2
        y -= h/2
    elif e_mode == RADIUS:
        x -= w/2
        y -= h/2
        w *= 2
        h *= 2
    elif e_mode == CORNERS:
        w -= x
        h -= y
    
    if fill_col:
        shape_surf = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.ellipse(shape_surf, fill_col, shape_surf.get_rect())
        screen.blit(shape_surf, pygame.Rect(x, y, w, h))     
        #pygame.draw.ellipse(screen, fill_col, (x-a/2, y-b/2, a, b), 0)
             
    if stroke_col:
        pygame.draw.ellipse(screen, stroke_col, (x, y, w, h), stroke_weight)

        
def triangle(x0, y0, x1, y1, x2, y2):
    if fill_col:
        # https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame
        x_0 = min(x0, x1, x2)
        x_1 = max(x0, x1, x2)
        y_0 = min(y0, y1, y2)
        y_1 = max(y0, y1, y2)
        w = x_1 - x_0
        h = y_1 - y_0
        
        shape_surf = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.polygon(shape_surf, fill_col, ((x0-x_0, y0-y_0), (x1-x_0, y1-y_0), (x2-x_0, y2-y_0)))
        screen.blit(shape_surf, pygame.Rect(x_0, y_0, w, h))
        #pygame.draw.polygon(screen, fill_col, ((x0, y0), (x1, y1), (x2, y2)))

        
    if stroke_col:
        pygame.draw.polygon(screen, stroke_col, ((x0, y0), (x1, y1), (x2, y2)), stroke_weight)


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
        print('bitsize =', screen.get_bitsize())
        print(screen)
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
        pass


if __name__ == '__main__':
    print('testing p5')
    
    #App().run()
    
    class Demo(App):
        def setup(self):
            size(800, 400)
            
        def draw(self):
            background(127)
            fill(255)
            triangle(30, 75, 58, 20, 86, 75)
            fill(255, 0, 0, 127) 
            triangle(10, 15, 70, 30, 46, 85)
            x, y = pygame.mouse.get_pos()
            triangle(x+10, y+15, x+70, y+30, x+46, y+85)
             
    Demo().run()
