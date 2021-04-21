from oop import *
# bouncing ball with mass

class Ball(pyglet.shapes.Circle):
    def __init__(self, win, *args, **kwargs):
        super().__init__(radius=20, color=(255, 0, 0), *args, **kwargs)
        self.win = win
        self.opacity = 150
        self.dx = 2
        self.dy = 2
        self.radius = random.randint(5, 50)
        self.m = self.radius / 10
        self.gravity = 0, -0.1
        self.wind = 0.02, 0
    
    def update(self, dt):
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
    
class AppWindow(pyglet.window.Window):
    # This is the app window
    def __init__(self, *args):
        super().__init__(*args)
        
        n = 10
        self.balls = []
        for i in range(n):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            b = Ball(self, x=x, y=y)
            self.balls.append(b)
            pyglet.clock.schedule_interval(b.update, 1/120.0)
        
        self.status = pyglet.text.Label('status', x=10, y=10)
        self.clear()

    def on_draw(self):
        self.clear() 
        for ball in self.balls:
            ball.draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.balls[0].x = x
        self.balls[0].y = y

if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
