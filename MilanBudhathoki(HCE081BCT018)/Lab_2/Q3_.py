#3. Modify the program to take endpoints as user input.

import matplotlib.pyplot as plt
def dda(x0, y0, x1, y1):
    x_coords = []
    y_coords = []
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))
    if steps == 0:
        return [x0], [y0]
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x0, y0
    for _ in range(steps + 1):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc
    return x_coords, y_coords
try:
    x0 = int(input("Enter x0: "))
    y0 = int(input("Enter y0: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
except ValueError:
    print("Please enter valid integer values.")
    exit()
x_coords, y_coords = dda(x0, y0, x1, y1)
plt.figure(figsize=(6, 4))
plt.scatter(x_coords, y_coords, color='blue', marker='o')  
plt.plot(x_coords, y_coords, color='lightblue', linestyle='--', alpha=0.5)  
plt.title(f"DDA Line from ({x0},{y0}) to ({x1},{y1})")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()