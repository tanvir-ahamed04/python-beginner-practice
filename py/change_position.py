import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax=plt.subplot(111)

ax.plot([-2,2,3,4], [-10,20,25,5])
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()