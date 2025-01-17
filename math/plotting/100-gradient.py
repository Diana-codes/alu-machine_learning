#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

fig, ax = plt.subplots()

# the scatter diagram with the color bar
im = ax.scatter(x, y, c=z)
fig.colorbar(im, ax=ax, label="elevation (m)")

# plot axes descriptions
ax.set_title("Mountain Elevation")
ax.set_xlabel("x coordinate (m)")
ax.set_ylabel("y coordinate (m)")

plt.show()
