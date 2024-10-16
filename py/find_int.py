import math
for i in range(0,10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+168))
    if (x*x==i+100) and (y*y==i+168):
        print(i)
