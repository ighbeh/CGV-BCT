#2. Draw ellipses with different radii and centres.
import matplotlib.pyplot as plt
import numpy as np

def draw_ellipse(rx, ry, xc, yc):
    theta = np.linspace(0, 2*np.pi, 300)
    x = xc + rx * np.cos(theta)
    y = yc + ry * np.sin(theta)
    plt.plot(x, y)

# Create figure
plt.figure()

# Draw ellipses with different radii and centers
draw_ellipse(6, 4, 0, 0)      # Ellipse 1
draw_ellipse(4, 2, 8, 5)      # Ellipse 2
draw_ellipse(3, 6, -6, -4)    # Ellipse 3
draw_ellipse(2, 2, -8, 6)     # Ellipse 4 (circle)

# Formatting
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Ellipses with Different Radii and Centers")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()
