import math
import matplotlib.pyplot as plt

print("=== Pipe Flow Velocity Visualization ===")

# Fixed flow rate (m³/h)
flow_rate_m3h = 10
flow_rate = flow_rate_m3h / 3600.0  # Convert to m³/s

# Diameter range (m)
diameters = [i / 1000 for i in range(20, 205, 5)]  # 0.01–0.20 m
velocities = []

for d in diameters:
    area = math.pi * (d ** 2) / 4.0
    velocity = flow_rate / area
    velocities.append(velocity)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(diameters, velocities, marker='o')
plt.title("Flow Velocity vs. Pipe Diameter")
plt.xlabel("Pipe Diameter (m)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()
