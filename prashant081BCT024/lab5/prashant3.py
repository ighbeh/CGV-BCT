#3. Compare the point spacing in Region 1 and Region 2.
import matplotlib.pyplot as plt

def midpoint_ellipse_regions(rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    region1 = []
    region2 = []

    # Region 1 (slope < 1)
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    while dx < dy:
        region1.append((x, y))

        if p1 < 0:
            x += 1
            dx += 2 * ry2
            p1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx += 2 * ry2
            dy -= 2 * rx2
            p1 += dx - dy + ry2

    # Region 2 (slope ≥ 1)
    p2 = (ry2 * (x + 0.5)**2) + (rx2 * (y - 1)**2) - (rx2 * ry2)
    while y >= 0:
        region2.append((x, y))

        if p2 > 0:
            y -= 1
            dy -= 2 * rx2
            p2 += rx2 - dy
        else:
            y -= 1
            x += 1
            dx += 2 * ry2
            dy -= 2 * rx2
            p2 += dx - dy + rx2

    return region1, region2


# Example
rx, ry = 8, 5
region1, region2 = midpoint_ellipse_regions(rx, ry)

x1, y1 = zip(*region1)
x2, y2 = zip(*region2)

plt.scatter(x1, y1, label="Region 1")
plt.scatter(x2, y2, label="Region 2")
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Point Spacing in Region 1 and Region 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
