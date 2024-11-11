import numpy as np
import matplotlib.pyplot as mpl
from math import sqrt

# Intersecțiile
x_min = 0  
x_max = 2 + sqrt(7)  
x_min2 = 2 + sqrt(7) 
x_max2 = 6  

# Axele x si y
mpl.axhline(0, color='black', linewidth=0.8, linestyle='-')
mpl.axvline(0, color='black', linewidth=0.8, linestyle='-')

# Centrul cercului
xp = 2
yp = 3
mpl.plot(xp, yp, marker='o', color='black')

# Cercul
unghi = np.linspace(0, 2 * np.pi, 100)
x_circle = xp + 4 * np.cos(unghi)
y_circle = yp + 4 * np.sin(unghi)

# Funcția liniară f(x)
x_linie = np.linspace(0, 2+sqrt(7), 100)  
y_linie = - 1.391 * x_linie + 6.464

# Functia monotonă h(x)
x_monotona = np.linspace(0, 6, 100)
y_monotona = np.full_like(x_monotona, 3)

#Intervalul punctată 2+sqrt(7)

y_punc = np.linspace(0, 6, 100)
x_punc = np.full_like(y_punc, 2+sqrt(7))


# Integrala reprezentată prin filling points
x_fill1 = np.linspace(x_min, x_max, 200)
x_fill2 = np.linspace(x_min2, x_max2, 200)
y_fill_circle_top1 = yp + np.sqrt(16 - (x_fill1 - xp)**2)
y_fill_circle_top2 = yp + np.sqrt(16 - (x_fill2 - xp)**2)
y_fill_circle_top3 = yp - np.sqrt(16 - (x_fill2 - xp)**2)
y_fill_linie1 = - 1.391 * x_fill1 + 6.464
y_fill_linie2 = 3  

# Desenerea functiilor
mpl.plot(x_circle, y_circle, color='blue', label='Cerc')
mpl.plot(x_linie, y_linie, color='red', label='f(x)')
mpl.plot(x_monotona, y_monotona, color='black', label='3', alpha = 0.5)
mpl.plot(x_punc, y_punc, color='black', label='2+sqrt(7)', alpha = 0.5)

# Filling
mpl.fill_between(x_fill1, y_fill_circle_top1, y_fill_linie1, where=(y_fill_circle_top1 > y_fill_linie1), color='lightgreen', alpha=1)
mpl.fill_between(x_fill2, y_fill_circle_top2, y_fill_linie2, where=(y_fill_circle_top2 > y_fill_linie2), color='lightgreen', alpha=1)
mpl.fill_between(x_fill2, y_fill_circle_top3, y_fill_linie2, where=(y_fill_circle_top3 < y_fill_linie2), color='lightgreen', alpha=1)

mpl.xlim(-3, 7)
mpl.ylim(-2, 9)
mpl.gca().set_aspect('equal')
mpl.title('Aria segmentului')
mpl.grid()
mpl.legend()
mpl.show()
