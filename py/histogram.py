import matplotlib.pyplot as plt

temperatures=[25,30,32,34,34,23]
cities =['A','B','C','D','E','F']
plt.figure(figsize=(8, 6))
plt.bar(cities,temperatures,color='skyblue')
plt.xlabel('Cities')
plt.ylabel('Temperature(C)')
plt.title('Temperature of Cities ABCDEF')
plt.grid(True)
plt.show()
