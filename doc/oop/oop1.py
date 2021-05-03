from oop import *
# bouncing ball with gravity

class Ball(pyglet.shapes.Circle):
    def __init__(self, win, *args):
        super().__init__(x=100, y=100, radius=20, color=(255, 127, 0))
        self.win = win
        self.dx = 2
        self.dy = 2
        self.gravity = 0, -0.1
        self.wind = 0.02, 0
    
    def update(self, dt):
        self.dx += self.gravity[0] + self.wind[0]
        self.dy += self.gravity[1] + self.wind[1]
        
        self.x += self.dx
        self.y += self.dy
        
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
        self.ball = Ball(self)
        self.status = pyglet.text.Label('status', x=10, y=10)
        self.clear()
        pyglet.clock.schedule_interval(self.ball.update, 1/120.0)

    def on_draw(self):
        self.clear()
        self.ball.draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.ball.x = x
        self.ball.y = y

if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
