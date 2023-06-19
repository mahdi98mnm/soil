import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Monthly precipitation data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
precipitation_data = [2, 3, 1, 2, 5, 4]

# Create a figure and axis
fig, ax = plt.subplots()
bars = ax.bar(months, precipitation_data)

# Set the axis limits
ax.set_ylim(0, max(precipitation_data) + 1)

# Animation update function
def update(frame):
    # Update the bar heights
    for i, bar in enumerate(bars):
        bar.set_height(precipitation_data[i] * (frame + 1))
    return bars

# Create the animation
animation = FuncAnimation(fig, update, frames=5, interval=200, blit=True)

# Display the animation
plt.show()
