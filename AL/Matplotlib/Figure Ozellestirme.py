from matplotlib import pyplot as plt
import numpy as np



x = np.arange(1, 6)
y = np.arange(2, 11, 2)

"""
fig,axes = plt.subplots(nrows=2, ncols=1)

# for ax in axes:
#     ax.plot(x, y)

axes[0].set_title("Arafat")
axes[0].plot(x, y)

axes[1].set_title("Emin")
axes[1].plot(x, x ** 3)

plt.tight_layout()
plt.show()
"""


"""
fig = plt.figure(figsize=(6, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(x, y, color="purple")
plt.show()
"""


"""
fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))
axes[0].set_title("Arafat")
axes[0].plot(x, y, color='red')

axes[1].set_title("Emin")
axes[1].plot(x, x * 3, color='blue')

plt.tight_layout()

# fig.savefig("Figure1.png")
# fig.savefig("Figure1.pdf")

plt.show()
"""







"""
fig = plt.figure(figsize=(8, 6))
axes = fig.add_axes([0.2, 0.2, 0.6, 0.6])
axes.plot(x, x ** 0.5, color="purple", label="X Karekok")
axes.plot(x, x**2, color="red", label="X Kare")
axes.plot(x, x**3, color="blue", label="X Kup")

axes.legend() # renk adini figure'de gostermek icin
plt.show()
"""