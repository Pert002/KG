import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pylab import *




sns.set_style("whitegrid", {"grid.color": ".6", "grid.linestyle": ":"})




a = 30
A = -20
B = 20
y1 = []
y2 = []
x1 = []


ax = plt.gca()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax.arrow(x=0, y=5, dx=-0.5, dy=-1)
ax.arrow(x=0, y=5, dx=0.5, dy=-1)

ax.arrow(x=5, y=0, dx=-1, dy=1)
ax.arrow(x=5, y=0, dx=-1, dy=-1)

arrow(x=0, y=0, dx=a, dy=0, head_width=0.05*a, head_length=0.05*a, color='black')
arrow(x=0, y=0, dx=0, dy=a, head_width=0.05*a, head_length=0.05*a, color='black')





for x in np.arange(A, B, 0.01):
    x = round(x, 2)
    x1.append(x)
    y1.append(np.sqrt((x**2*(a-x))/(a+x)))
    y2.append(-np.sqrt((x**2*(a-x))/(a+x)))



ax = sns.lineplot(x=x1, y=y1, color='blue')
sns.lineplot(x=x1, y=y2, color='blue')
ax.yaxis.set_major_locator(MultipleLocator(2))  # шаг сетки по y
ax.xaxis.set_major_locator(MultipleLocator(2))  # шаг сетки по x
plt.show()

