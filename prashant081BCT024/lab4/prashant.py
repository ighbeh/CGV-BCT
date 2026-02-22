import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r, X, Y):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        # 8-way symmetry
        X.extend([xc + x, xc - x, xc + x, xc - x,
                  xc + y, xc - y, xc + y, xc - y])
        Y.extend([yc + y, yc + y, yc - y, yc - y,
                  yc + x, yc + x, yc - x, yc - x])

        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*(x - y) + 1


# Center of concentric circles
xc, yc = 0, 0

# Different radii (target pattern)
radii = [4, 8, 12, 16, 20]

X, Y = [], []

for r in radii:
    midpoint_circle(xc, yc, r, X, Y)

# Plot
plt.scatter(X, Y)
plt.title("Concentric Circles using Midpoint Circle Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis("equal")
plt.grid(True)
plt.show()
