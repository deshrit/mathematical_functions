import numpy as np
import matplotlib.pyplot as plt
import math

# Title font
font1 = {
	'family':'serif',
	'size':20,
	'color':'black'
}

# Labels font
font2 = {
	'family':'serif',
	'size':15,
	'color':'brown'
}

# Angles in raidan
x = np.arange(-3*np.pi/2, 3*np.pi/2, 0.0174)
y = np.zeros(x.shape)
y = x + np.tan(x)


plt.plot(x, y)
plt.ylim(-20, 20)
plt.grid(axis="x")
plt.title("Tangent Function", fontdict=font1)
plt.xlabel("x (radian)", fontdict=font2)
plt.ylabel("y = tan(x)", fontdict=font2)
plt.show()
