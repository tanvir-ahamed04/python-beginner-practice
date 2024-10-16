import matplotlib.pyplot as plt



x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.Color = 'red'
plt.lineWidth = 3

plt.plot(x, y)


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')
plt.show()

# plt.plot([1,2,3,4],[10, 20, 25, 30], color = 'lightblue', linewidth = 3)
# plt.xlim(0.5, 4.5)
# plt.show()
