from oop import *
# 31 point rectangle towards the mouse

class Rect(pyglet.shapes.Rectangle):
    def __init__(self, win, *args, **kwargs):
        x = win.width/2
        y = win.height/2
        w = 150
        h = 50
        super().__init__(x, y, w, h, color=(0, 255, 0), *args, **kwargs)
        self.win = win
        self.pos = Vec2(x, y)
        
        self.gravity = 0, -0.1
        self.wind = 0.1, 0
        self.dx = 0
        self.dy = 0
        self.m = 1
        self.radius = max(w/2, h/2)

        
    def update(self, dt):
        d = self.win.mouse - self.pos
        self.rotation = -math.degrees(math.atan2(d.y, d.x))
        
        
#         self.dx += (self.gravity[0] + self.wind[0]/self.m)
#         self.dy += (self.gravity[1] + self.wind[1]/self.m)
#         
#         self.x += self.dx
#         self.y += self.dy
#         
#         if self.x < self.radius:
#             self.dx = abs(self.dx)
#         elif self.x > self.win.width-self.radius:
#             self.dx = -abs(self.dx)
#         
#         if self.y < self.radius:
#             self.dy = abs(self.dy)
#         elif self.y > self.win.height-self.radius:
#             self.dy = -abs(self.dy)
#             
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
        self.status = pyglet.text.Label('status', x=10, y=10)
        pyglet.clock.schedule_interval(self.rect.update, 1/120.0)
        self.mouse = Vec2(0, 0)

    def on_draw(self):
        self.clear() 
        self.rect.draw()
        self.status.draw()
        
    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse.x = x
        self.mouse.y = y
        self.status.text = f'mouse motion to {x}, {y}'       
        
if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
