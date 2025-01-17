#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

fig, ax = plt.subplots()

person = ['Farrah', 'Fred', 'Felicia']
fruits = ['apples', 'bananas', 'oranges', 'peaches']
bar_colors = ['tab:red', 'yellow', '#ff8000', '#ffe5b4']

width = 0.5
bottom = np.zeros(3)  # stack the bar graph from bottom to top

# looping through each fruit and plot it on top of the previous ones
for i in range(len(fruits)):
    ax.bar(
        person, fruit[i], label=fruits[i], color=bar_colors[i], bottom=bottom
    )
    bottom += fruit[i]  # updates the bottom position for the next stack

# label the y-axis
ax.set_ylabel("Quantity of Fruit")
ax.set_ylim(0, 80)
ax.set_yticks(range(0, 81, 10))

# sets the title
ax.set_title("Number of Fruit per Person")

# sets a legend
ax.legend()

plt.show()
