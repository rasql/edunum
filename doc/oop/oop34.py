from oop import *
# 34 Oscillator class

class Oscillator(pyglet.shapes.Circle):
    def __init__(self, win, *args, **kwargs):
        self.x0 = win.width/2
        self.y0 = win.height/2
        super().__init__(x=self.x0, y=self.y0, radius=20, color=(255, 0, 0), *args, **kwargs)
        self.win = win
        self.opacity = 200
        self.theta = 0
        self
        self.amplitude = 200
        self.amplitude_y = 50
        
    def update(self, dt):
        self.theta += 0.1        
        self.x = self.x0 + math.cos(self.theta) * self.amplitude
        self.y = self.y0 + math.cos(self.theta) * self.amplitude_y
    
class AppWindow(pyglet.window.Window):
    # This is the app window
    def __init__(self, *args):
        super().__init__(*args)
        self.ball = Oscillator(self)
        self.ball1 = Oscillator(self)
        self.ball1.x0 += 100
        self.status = pyglet.text.Label('status', x=10, y=10)
        self.clear()
        
        pyglet.clock.schedule_interval(self.ball.update, 1/120.0)
        pyglet.clock.schedule_interval(self.ball1.update, 1/120.0)

    def on_draw(self):
        self.clear()
        self.ball.draw()
        self.ball1.draw()
        self.status.draw()   
        
if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
