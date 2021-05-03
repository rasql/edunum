from oop import *
# bouncing ball
    
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

if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
