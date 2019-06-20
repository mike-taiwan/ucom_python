import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
x3 = np.linspace(0.1, 10.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
y3 = np.tan(x3) * np.log2(x3)
plt.subplot(3, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('')
plt.ylabel('figure1')

plt.subplot(312)
plt.plot(x2, y2, 'r*--')
plt.title('')
plt.ylabel('figure2')

plt.subplot(313)
plt.plot(x3, y3, 'g.-', linewidth=2)
plt.title('')
plt.ylabel('figure3')

plt.show()