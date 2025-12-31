#2. Draw lines with different slopes: m < 1, m > 1, horizontal, vertical and negative slope.

import matplotlib.pyplot as plt
def dda(x0, y0, x1, y1):
    x_coords = []
    y_coords = []
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x = x0
    y = y0
    for _ in range(steps + 1):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc
    return x_coords, y_coords
lines = [
    ((0, 0), (8, 4)),   # m < 1
    ((0, 0), (4, 8)),   # m > 1
    ((0, 5), (8, 5)),   # horizontal
    ((5, 0), (5, 8)),   # vertical
    ((0, 0), (8, -4))   # negative slope
]
plt.figure(figsize=(8, 6))
colors = ['b', 'r', 'g', 'm', 'c']
for i, line in enumerate(lines):
    x0, y0 = line[0]
    x1, y1 = line[1]
    x_coords, y_coords = dda(x0, y0, x1, y1)
    plt.plot(x_coords, y_coords, marker='o', color=colors[i], label=f"Line {i+1}")
plt.title("DDA Line Drawing with Different Slopes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()