import pyglet, sys, random, math
# Create a bouncing ball window

# for k, v in pyglet.options.items():
#     print(k, '=', v)

# press C to add circles
# press R to add rectangles

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'Vec2({self.x}, {self.y})'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vec2(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vec2(x, y)
   
    def __mul__(self, k):
        return Vec2(self.x * k , self.y * k)
    
    def __div__(self, k):
        return Vec2(self.x / k , self.y / k)
        
    def mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self):
        d = self.mag()
        self.x /= d
        self.y /= d
        

        
        
class Ball(pyglet.shapes.Circle):
    def __init__(self, win, *args):
        super().__init__(x=100, y=100, radius=20, color=(255, 127, 0), batch=win.batch)
        self.win = win
        self.pos = Vec2(100, 100)
        self.v = Vec2(2, 2)
    
    def update(self, dt):
        self.pos += self.v
        
        if self.pos.x < 0:
            self.v.x = abs(self.v.x)
        if self.pos.x > self.win.width:
            self.v.x = -abs(self.v.x)
        
        if self.pos.y < 0:
            self.v.y = abs(self.v.y)
        if self.pos.y > self.win.height:
            self.v.y = -abs(self.v.y)
            
        self.x = self.pos.x
        self.y = self.pos.y
        
        
class Circle(pyglet.shapes.Circle):
    def __init__(self, win, x, y, r):
        super().__init__(x, y, r, batch=win.batch)
        self.win = win
        
class Rect(pyglet.shapes.Rectangle):
    def __init__(self, win, *args, **kwargs):
        super().__init__(*args, **kwargs, batch=win.batch)
        self.win = win

class AppWindow(pyglet.window.Window):
    # This is the app window
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pyglet.graphics.Batch()
        self.status = pyglet.text.Label('status', x=10, y=10, batch=self.batch)
        self.selection_rect = pyglet.shapes.BorderedRectangle(200, 200, 100, 50,
                            color=(100, 100, 100), batch=self.batch)
        self.objects = []

        self.ball = Ball(self)
        self.rect = Rect(self, 100, 50, 100, 50, (100, 100, 255))

        pyglet.clock.schedule_interval(self.update, 1/120.0)
        
    def update(self, dt):
        self.ball.update(dt)
 
    def on_draw(self):
        self.clear()
        self.batch.draw()
            
    def on_key_press(self, symbol, modifiers):
        self.status.text = f'key press: {symbol}, mffod={modifiers}'
        if symbol == pyglet.window.key.R:
            self.ball.v.x = random.randint(-3, 3)
            self.ball.v.y = random.randint(-3, 3)
        if symbol == pyglet.window.key.F:
            print('full screen')
#             self.set_fullscreen() # BUG remains with a black screen

        if symbol == pyglet.window.key.C:
            c = Circle(self, *self.mouse, 30)
            self.objects.append(c)

        if symbol == pyglet.window.key.R:
            r = Rect(self, *self.mouse, 30, 15)
            self.objects.append(r)

    def on_key_release(self, symbol, modifiers):
        self.status.text = f'key release: {symbol}, mod={modifiers}'

        
    def on_mouse_press(self, x, y, button, modifiers):
        self.status.text = f'mouse press at {x}, {y} button={button}'
        self.selection_rect.position = x, y
   
    def on_mouse_release(self, x, y, button, modifiers):
        self.status.text = f'mouse realease at {x}, {y} button={button}'

    def on_mouse_motion(self, x, y, dx, dy):
        self.status.text = f'mouse motion to {x}, {y}'
        self.mouse = x, y
        
        w = x - self.selection_rect.x 
        h = y - self.selection_rect.y
        self.selection_rect.w = w
        self.selection_rect.h = h

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.status.text = f'mouse drag {x}, {y}'


    def on_mouse_leave(self, x, y):
        self.status.text = f'mouse leave {x}, {y}'
        
    def on_mouse_enter(self, x, y):
        self.status.text = f'mouse enter {x}, {y}'
          
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.status.text = f'mouse scroll {scroll_x}, {scroll_y}'
        
    def on_move(self, x, y):
        self.status.text = f'window move: {x}, {y}'

# makes the program stop on a black window
#     def on_resize(self, width, height):
#         self.status.text = f'window resize: {width}, {height}'
#          
#     def on_close(self):
#         print('on close')
        
    def on_exit(self):
        print('on exit')
    
        
if __name__ == '__main__':
    win = AppWindow()
    
    win2 = AppWindow(800, 200, 'Bouncing Ball')
    win2.ball.v = Vec2(3, 5)
    win2.ball.color = (255, 0, 0)

    win3 = AppWindow(caption='Press R to change speed')
    win3.ball.v = Vec2(5, -3)
    win3.ball.color = (0, 0, 255)
    
    pyglet.app.run()
    sys.exit()
