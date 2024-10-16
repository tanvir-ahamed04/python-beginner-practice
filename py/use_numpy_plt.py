import matplotlib.pyplot as plt
import numpy as np

# Define the input data
data = [('apples', 2), ('oranges', 3), ('peaches', 1)]
fruit, value = zip(*data)

# Create the figure and subplots
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Create the bar plot
x = np.arange(len(fruit))
ax1.bar(x, value, align='center', color='gray')
ax2.bar(x, value, align='center', color='gray')
ax2.set(xticks=x, xticklabels=fruit)

# Show the plot
plt.show()

''' The first digit represents the total nu
mber of rows, the second digit represents
the total number of columns, and the third
digit represents the the number of the subplot in the grid.'''