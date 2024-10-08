import matplotlib.pyplot as plt
import numpy as np

# Position and strength of the positive charge
charge_position = np.array([1, 1])  # Position of the charge
charge_strength = 5  # Strength of the charge

# Create a grid of points for plotting
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate electric field components (Ex, Ey) due to the charge
r = np.sqrt((X - charge_position[0])**2 + (Y - charge_position[1])**2)
Ex = charge_strength * (X - charge_position[0]) / r**3
Ey = charge_strength * (Y - charge_position[1]) / r**3

# Create a streamplot
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, Ex, Ey, color='b', linewidth=1, density=2)
plt.scatter(charge_position[0], charge_position[1], color='red', label='Positive Charge')
plt.title('Electric Field of a Positive Charge')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
