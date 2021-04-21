from oop import *
# 41 Particle system with repellers

class Particle:
    def __init__(self, win, x, y):
        self.win = win
        self.pos = Vec2(x, y)
        self.vel = Vec2(random.randint(-9, 9), random.randint(-5, 5))
        self.acc = Vec2(0, 0)
        self.circle = pyglet.shapes.Circle(x, y, 10)
        self.lifespan = 255
    
    def update(self, dt):
        self.vel += self.acc
        self.pos += self.vel
        self.circle.x = self.pos.x
        self.circle.y = self.pos.y
        
        self.lifespan -= 5
        self.circle.opacity = self.lifespan

    def draw(self):
        self.circle.draw()
        
    def is_dead(self):
        return self.lifespan < 0
    
    def apply_force(self, f):
        self.acc += f
        
    def apply_repeller(self, repeller):
        pass
    
class Repeller:
    def __init__(self, win, x, y):
        self.win = win
        self.pos = Vec2(x, y)
        self.circle = pyglet.shapes.Circle(x, y, radius=20, color=(255, 200, 0))
    
    def repel(self, particle):
        r = particle.pos - self.pos
        dist = r.mag()
        r.normalize()
        force = r * (500/(dist*dist))
        return force
        
    
    def draw(self):
        self.circle.draw()
       
       
class ParticleSystem:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.particles = []
        
    def add_particle(self):
        p = Particle(self.win, self.x, self.y)
        self.particles.append(p)
        
    def apply_force(self, f):
        for p in self.particles:
            p.apply_force(f)
            
    def apply_repeller(self, repeller):
        for p in self.particles:
            f = repeller.repel(p)
            p.apply_force(f)

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
            if p.is_dead():
                self.particles.remove(p)
        
    def draw(self):
        for p in self.particles:
            p.draw()
        
    
class AppWindow(pyglet.window.Window):
    # This is the app window
    def __init__(self, *args):
        super().__init__(*args)
        self.status = pyglet.text.Label('status', x=10, y=10)
        
        self.gravity = Vec2(0, -0.05)
        self.repeller = Repeller(self, self.width/2-20, self.height/4)
        self.ps = ParticleSystem(self, self.width/2, self.height-50)   
        pyglet.clock.schedule_interval(self.ps.update, 1/120.0)

    def on_draw(self):
        self.clear()
        self.status.draw()
        
        self.ps.apply_force(self.gravity)
        self.ps.apply_repeller(self.repeller)
        self.ps.add_particle()
        self.ps.draw()
        self.repeller.draw()
 
        
if __name__ == '__main__':
    win = AppWindow(800, 300)
    win1 = AppWindow(600, 400)
    pyglet.app.run()
    sys.exit()
