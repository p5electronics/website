# @ Author: Hugo The Immortal
# @ Created: 2024-09-08
# @ Modified by: Hugo The Immortal
# @ Last Modified: 2024-09-08
# @ Description: Lissajou Curve Charts

from itertools import product
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = False
plt.rcParams['font.size'] = 10
plt.style.use('dark_background')

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
phase = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

unique = []
seen = set()

for ai, bi in product(a, b):
    ratio = ai / bi
    if ratio not in seen:
        unique.append((ai, bi))
        seen.add(ratio)

# 4 x 4 grid size
fig, axs = plt.subplots(nrows=4, ncols=4)

for i, ax in enumerate(axs.flatten()):
    if i < len(unique):
        ai, bi = unique[i]
        t = np.linspace(-10, 10, num=1000)
        x = np.sin(ai * t + phase[i % len(phase)])
        y = np.sin(bi * t)
        ax.plot(x, y)
        ax.axis('off')
        
        phase_deg = np.rad2deg(phase[i % len(phase)])
        ax.set_title(f'{ai}:{bi}')
        
        # Crappy formatting lol
        if i < 4:
            ax.set_title(f'($\\delta$ = {phase_deg:.0f}$\\degree$)\n\n {ai}:{bi}')
        else:
            ax.set_title(f'{ai}:{bi}')

plt.tight_layout()
plt.savefig("lissajou-graph-dark.png", dpi=300) 
plt.show()