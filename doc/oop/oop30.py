from oop import *
# 30 rotation of a rectangle

class Rect(pyglet.shapes.Rectangle):
    def __init__(self, win, *args, **kwargs):
        x = win.width/2
        y = win.height/2
        w = 50
        h = 100
        super().__init__(x, y, w, h, color=(0, 255, 0), *args, **kwargs)
        self.win = win
        self.anchor_x = w/2
        self.anchor_y = h/2
        self.pos = Vec2(x, y)
        
        self.gravity = 0, -0.1
        self.wind = 0.1, 0
        self.dx = 0
        self.dy = 0
        self.m = 1
        self.radius = max(w/2, h/2)
        
    def update(self, dt):
        self.rotation += 1
        
        self.dx += (self.gravity[0] + self.wind[0]/self.m)
        self.dy += (self.gravity[1] + self.wind[1]/self.m)
        
        self.x += self.dx
        self.y += self.dy
        
        if self.x < self.radius:
            self.dx = abs(self.dx)
        elif self.x > self.win.width-self.radius:
            self.dx = -abs(self.dx)
        
        if self.y < self.radius:
            self.dy = abs(self.dy)
        elif self.y > self.win.height-self.radius:
            self.dy = -abs(self.dy)
            
        self.pos.x = self.x
        self.pos.y = self.y
        

class Ball(pyglet.shapes.Circle):
    def __init__(self, win, *args, **kwargs):
        super().__init__(radius=20, color=(255, 0, 0), *args, **kwargs)
        self.win = win
        self.opacity = 150
        self.dx = 2
        self.dy = 2
        self.radius = random.randint(5, 20)
        self.m = self.radius / 10
        self.gravity = 0, 0
        self.wind = 0, 0
        self.pos = Vec2(0, 0)
    
    def update(self, dt):
        self.dx += (self.gravity[0] + self.wind[0]/self.m)
        self.dy += (self.gravity[1] + self.wind[1]/self.m)
        
        f = self.win.attractor.attract(self)
        self.dx += f.x
        self.dy += f.y
        
        self.x += self.dx
        self.y += self.dy
        
        if self.x < self.radius:
            self.dx = abs(self.dx)
        elif self.x > self.win.width-self.radius:
            self.dx = -abs(self.dx)
        
        if self.y < self.radius:
            self.dy = abs(self.dy)
        elif self.y > self.win.height-self.radius:
            self.dy = -abs(self.dy)
            
        self.pos.x = self.x
        self.pos.y = self.y
    
class AppWindow(pyglet.window.Window):
    # This is the app window
    def __init__(self, *args):
        super().__init__(*args)
        self.rect = Rect(self)
        self.rect1 = Rect(self)
        self.status = pyglet.text.Label('status', x=10, y=10)
        pyglet.clock.schedule_interval(self.rect.update, 1/120.0)

    def on_draw(self):
        self.clear() 
        self.rect.draw()
        self.rect1.draw()
        
        
if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
