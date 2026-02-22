import matplotlib.pyplot as plt

# Function to scale a point about a fixed point
def scale_point(x, y, xf, yf, s):
    x_new = xf + s * (x - xf)
    y_new = yf + s * (y - yf)
    return x_new, y_new

# Original line endpoints
x1, y1 = 2, 3
x2, y2 = 6, 7

# Calculate midpoint of the line (fixed point)
xf = (x1 + x2) / 2
yf = (y1 + y2) / 2

# Scaling factor
s = 1.5

# Scale both endpoints about midpoint
x1_new, y1_new = scale_point(x1, y1, xf, yf, s)
x2_new, y2_new = scale_point(x2, y2, xf, yf, s)

# Plot original and scaled lines
plt.plot([x1, x2], [y1, y2], 'b-', label='Original Line')
plt.plot([x1_new, x2_new], [y1_new, y2_new], 'r--', label='Scaled Line')

# Plot midpoint
plt.scatter(xf, yf)
plt.text(xf, yf, ' Midpoint')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scaling of a Line About Its Midpoint')
plt.legend()
plt.grid(True)
plt.show()
