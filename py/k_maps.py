import matplotlib.pyplot as plt
import numpy as np

def plot_kmap(kmap, labels=None):
    kmap_array = np.array(kmap)  # Convert the list to a NumPy array
    plt.figure(figsize=(6, 6))
    plt.imshow(kmap_array, cmap='binary', interpolation='nearest')
    
    for i in range(kmap_array.shape[0]):
        for j in range(kmap_array.shape[1]):
            plt.text(j, i, str(kmap_array[i, j]), ha='center', va='center', fontsize=14)
            if labels:
                plt.text(j, i-0.15, labels[i][j], ha='center', va='center', fontsize=12)

    plt.xticks([])
    plt.yticks([])
    plt.show()

# Example K-map
kmap = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Optionally, you can provide labels for the rows and columns
labels = [['A\'B\'', 'A\'B', 'AB', 'AB\''],
          ['CD', 'CD\'', 'C\'D\'', 'C\'D']]

plot_kmap(kmap, labels)
