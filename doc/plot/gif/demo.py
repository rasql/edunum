import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()  
x, ysin, = [], []
ln1, = plt.plot([], [], 'ro')  

def init():  
    ax.set_xlim(0, 2*np.pi)  
    ax.set_ylim(-1, 1)  
  
def update(i):  
    x.append(i)  
    ysin.append(np.sin(i))  
    ln1.set_data(x, ysin)
    
a = FuncAnimation(fig, update, np.linspace(0, 2*np.pi, 32), init_func=init)  
# writer = PillowWriter(fps=10)  
# a.save("sine.gif", writer=writer);

plt.show()