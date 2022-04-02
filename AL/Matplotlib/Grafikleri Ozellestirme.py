from matplotlib import pyplot as plt
import numpy as np



x = np.arange(1, 6)
y = np.arange(2, 11, 2)

# lw=linewidth
"""
fig = plt.figure(figsize=(8, 6))
axes = fig.add_axes([0.2, 0.2, 0.6, 0.6])
axes.plot(x, x ** 3, color="purple", label="X Karekok", lw=8, linestyle=" ", marker="o", markersize=20,
          markerfacecolor="red", markeredgecolor="blue", markeredgewidth=5,
          )
axes.legend()
plt.show()
"""




"""
fig = plt.figure(figsize=(8, 6))
axes = fig.add_axes([0.2, 0.2, 0.6, 0.6])
axes.plot(x, x ** 3, color="purple", label="X Karekok", lw=8, marker="o", markersize=20,
          markerfacecolor="yellow", markeredgecolor="blue", markeredgewidth=5,
          )
axes.legend()
axes.set_xlim(0, 5)
axes.set_ylim(0, 50)
plt.show()
"""