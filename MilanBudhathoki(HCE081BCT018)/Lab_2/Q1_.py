#1.Implement the DDA algorithm as a function that returns x and y coordinate lists.

import matplotlib.pyplot as plt
def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x = x0
    y = y0
    x_coords = []
    y_coords = []
    for i in range(steps + 1):
        x_coords.append(round(x, 2))  
        y_coords.append(round(y, 2))
        x += x_inc
        y += y_inc
    return x_coords, y_coords
x0, y0 = 19,16
x1, y1 = 8, 18
x_coords, y_coords = dda(x0, y0, x1, y1)
plt.plot(x_coords, y_coords, marker='o', color='b')
plt.title(f"DDA Line from ({x0},{y0}) to ({x1},{y1})")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()