# @ Author: Hugo The Immortal
# @ Created: 2024-09-05
# @ Modified by: Hugo The Immortal
# @ Last Modified: 2024-09-05
# @ Description: An Animation of Lissajou Curve

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  
from matplotlib.animation import PillowWriter
import numpy as np

plt.style.use('default')
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')  
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_title('Lissajou Curve')

# Wave Amplitudes
A = 1
B = 1

# Wave Angular Frequencies
a = 3
b = 4

# Wave Phase
delta = np.pi / 2

# Display the changes in phase for Lissajou animation demo
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = np.linspace(-10, 10, num=1000)
    x = A * np.sin(a * t + delta * (t - 0.01 * frame))
    y = B * np.sin(b * t)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, update, frames=200, init_func=init, interval=20, blit=True)
writer = PillowWriter(fps=30, metadata=dict(artist='Hugo'), bitrate=1800)

plt.show()
plt.close()