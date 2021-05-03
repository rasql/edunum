import pyglet, sys, random
# mulltiple balls attracted towards the mouse

class Ball(pyglet.shapes.Circle):
    def __init__(self, win, *args):
        super().__init__(x=random.randint(50, 150),
                         y=random.randint(50, 150),
                         radius=20, color=(255, 0, 0))
        self.opacity = 100
        self.win = win
        self.dx = 2
        self.dy = 2
    
    def update(self, dt):
        self.x += self.dx
        self.y += self.dy
        
        fx = (self.win.mouse_x - self.x) * 0.001
        fy = (self.win.mouse_y - self.y) * 0.001
        
        self.dx += fx
        self.dy += fy
        
        if self.x < 0:
            self.dx = abs(self.dx)
        elif self.x > self.win.width:
            self.dx = -abs(self.dx)
        
        if self.y < 0:
            self.dy = abs(self.dy)
        elif self.y > self.win.height:
            self.dy = -abs(self.dy)


class AppWindow(pyglet.window.Window):
    # This is the app window
    def __init__(self, *args):
        super().__init__(*args)
        n = 10
        self.balls = []
        for i in range(n):
            self.balls.append(Ball(self))
            
        for ball in self.balls:
            pyglet.clock.schedule_interval(ball.update, 1/120.0)
        
        self.status = pyglet.text.Label('status', x=10, y=10)
        self.mouse_x = 100
        self.mouse_y = 100      

    def on_draw(self):
        self.clear()
        for ball in self.balls:
            ball.draw()
        self.status.draw()
        
    def on_mouse_motion(self, x, y, dx, dy):
        self.status.text = f'mouse motion to {x}, {y}'
        self.mouse_x = x
        self.mouse_y = y

if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
