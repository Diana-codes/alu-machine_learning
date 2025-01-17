#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# The 3x2 grid layout
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle("All in One")

# plot 1
axs[0, 0].plot(y0, 'r')
axs[0, 0].set_xlim(0, 10)

# plot 2
axs[0, 1].scatter(x1, y1, color='m', s=9)
axs[0, 1].set_xlabel("Height (in)", fontsize="small")
axs[0, 1].set_ylabel("Weight (lbs)", fontsize="small")
axs[0, 1].set_title("Men's Height vs Weight", fontsize="small")

# plot 3
axs[1, 0].plot(x2, y2)
axs[1, 0].set_xlabel("Time (years)", fontsize="small")
axs[1, 0].set_ylabel("Fraction Remaining", fontsize="small")
axs[1, 0].set_title("Exponential Decay of C-14", fontsize="small")
axs[1, 0].set_xlim(0, 28650)
axs[1, 0].set_yscale('log')

# plot 4
axs[1, 1].plot(x3, y31, 'r--', label='C-14')
axs[1, 1].plot(x3, y32, 'g-', label='Ra-226')
axs[1, 1].set_xlabel("Time (years)", fontsize="small")
axs[1, 1].set_ylabel("Fraction Remaining", fontsize="small")
axs[1, 1].set_title(
    "Exponential Decay of Radioactive Elements", fontsize="small"
)
axs[1, 1].set_xlim(0, 20000)
axs[1, 1].set_ylim(0, 1)
axs[1, 1].legend(loc='upper right')

# overlapping subplots
fig.delaxes(axs[2, 0])
fig.delaxes(axs[2, 1])

# plot 5
ax4 = plt.subplot2grid((3, 2), (2, 0), colspan=2)
ax4.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
ax4.set_xlabel("Grades", fontsize="small")
ax4.set_ylabel("Number of Students", fontsize="small")
ax4.set_title("Project A")
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 30)
ax4.set_xticks(range(0, 101, 10))

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
