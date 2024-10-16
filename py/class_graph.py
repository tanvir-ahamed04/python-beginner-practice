import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

x = np.linspace(0, 2*np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)

ax1.plot(x, y_sin)
ax2.plot(x, y_sin, 'go--', linewidth=1, markersize=2)
ax3.plot(x, y_cos, color="red", marker='+', linestyle="dashed")  # Fixed typo here

plt.show()




fig = plt.figure()
x = np.linspace(0, 10, 200)
data_obj = {'x': x, 
            'y1': 2 * x +1,
            'y2': 3 * x + 1.2,
            'mean':0.5* x*np.cos(2*x)+2.5*x+1.1}

# Fill the color between the two lines
plt.fill_between('x','y1','y2',color='yellow',data=data_obj)

# Plot the centerline with plot

plt.plot('x','mean', color = 'black', data=data_obj)

plt.show()
# Generate some random data for demonstration
np.random.seed(0)
x = np.random.randn(10)
y = np.random.randn(10)

# Plot the points using scatter plot
plt.scatter(x, y, color='red', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')

# Display the plot
plt.show()