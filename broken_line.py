import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt

x = ([6, 10, 18])
y1 = ([6.469, 6.419, 1.986])
y2 = ([2.16, 1.506, 0.6113])
y3 = ([37.85, 34.18, 17.85])

plt.plot(x, y1, 'ro-')
plt.plot(x, y2, 'g+-')
plt.plot(x, y3, 'b^-')
plt.xlabel('row')
plt.ylabel('coloum')
plt.show()
