from matplotlib import pyplot as plt
import numpy as np



x = np.arange(1, 6)
y = np.arange(2, 11, 2)

"""
plt.plot(x, y, "blue")
plt.show()
"""



"""
plt.subplot(2, 2, 1)
plt.plot(x, y, "red")

plt.subplot(2, 2, 2)
plt.plot(y, x, "blue")

plt.subplot(2, 2, 3)
plt.plot(y, x, "green")

plt.subplot(2, 2, 4)
plt.plot(x, x ** 2, "black")
plt.show()
"""




"""
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.2, 0.3])

axes1.plot(y, x)
axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outer Graph")


axes2.plot(y, x)
axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")
fig.show()
"""

print(x, y)