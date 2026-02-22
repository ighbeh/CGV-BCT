import numpy as np
import matplotlib.pyplot as plt

# Rotation angle in degrees
theta = 45

# Convert to radians
theta_rad = np.deg2rad(theta)

# Rotation matrix
R = np.array([
    [np.cos(theta_rad), -np.sin(theta_rad)],
    [np.sin(theta_rad),  np.cos(theta_rad)]
])

# Original line endpoints
p1 = np.array([2, 3])
p2 = np.array([6, 7])

# Apply rotation
p1_rot = R @ p1
p2_rot = R @ p2

# Plot original and rotated line
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], label="Original Line")
plt.plot([p1_rot[0], p2_rot[0]], [p1_rot[1], p2_rot[1]], linestyle='--', label="Rotated Line")

# Plot origin
plt.scatter(0, 0)
plt.text(0, 0, " Origin")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Pure Rotation About the Origin")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
