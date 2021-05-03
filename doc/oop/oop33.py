from oop import *
# 33 oscillation

class Ball(pyglet.shapes.Circle):
    def __init__(self, win, *args, **kwargs):
        self.x0 = win.width/2
        self.y0 = win.height/2
        super().__init__(x=self.x0, y=self.y0, radius=20, color=(255, 0, 0), *args, **kwargs)
        self.win = win
        self.opacity = 200
        self.theta = 0
        self.amplitude = 200
        

    def update(self, dt):
        self.theta += 0.1        
        self.x = self.x0 + math.cos(self.theta) * self.amplitude
    
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
        self.status.draw()   
        
if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
