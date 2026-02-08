#1. Implement the midpoint ellipse algorithm.
import matplotlib.pyplot as plt

def midpoint_ellipse(rx, ry, xc=0, yc=0):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    points_x = []
    points_y = []

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    while dx < dy:
        points_x.extend([xc + x, xc - x, xc + x, xc - x])
        points_y.extend([yc + y, yc + y, yc - y, yc - y])

        if p1 < 0:
            x += 1
            dx = dx + (2 * ry2)
            p1 = p1 + dx + ry2
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry2)
            dy = dy - (2 * rx2)
            p1 = p1 + dx - dy + ry2

    # Region 2
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        points_x.extend([xc + x, xc - x, xc + x, xc - x])
        points_y.extend([yc + y, yc + y, yc - y, yc - y])

        if p2 > 0:
            y -= 1
            dy = dy - (2 * rx2)
            p2 = p2 + rx2 - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry2)
            dy = dy - (2 * rx2)
            p2 = p2 + dx - dy + rx2

    return points_x, points_y


# Example usage
rx = 6
ry = 4
xc = 0
yc = 0

x_points, y_points = midpoint_ellipse(rx, ry, xc, yc)

plt.scatter(x_points, y_points)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Ellipse Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

