from oop import *
# 36 Pendulum class

class Pendulum():
    def __init__(self, win, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.angle = math.pi/4
        self.ang_vel = 0
        self.g = 0.4
        self.circle = pyglet.shapes.Circle(x, y, 20)
        self.line = pyglet.shapes.Line(x, y, x, y)
        
    def update(self, dt):
        self.ang_acc = -self.g / self.r * math.sin(self.angle)
        self.ang_vel += self.ang_acc
        self.angle += self.ang_vel
        
    def draw(self):
        x2 = self.x + math.sin(self.angle)*self.r
        y2 = self.y - math.cos(self.angle)*self.r
        
        self.line.x2 = x2
        self.line.y2 = y2
        self.line.draw()
        
        self.circle.x = x2
        self.circle.y = y2
        self.circle.draw()


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
        self.pendulum = Pendulum(self, 100, 200, 150)
        self.pendulum2 = Pendulum(self, 300, 300, 250)
        self.status = pyglet.text.Label('status', x=10, y=10)
        
        pyglet.clock.schedule_interval(self.pendulum.update, 1/120.0)
        pyglet.clock.schedule_interval(self.pendulum2.update, 1/120.0)

    def on_draw(self):
        self.clear()
        self.pendulum.draw()
        self.pendulum2.draw()
        self.status.draw()   
        
if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
