import numpy as np
import matplotlib.pyplot as plt


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

plt.subplots_adjust(wspace=0.5)

# x >= 0
x = np.arange(0, 5, 0.25)
y = np.zeros(x.shape, dtype=np.float64)
y = y + np.exp(x)
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.xlabel("x(>= 0)", fontdict=font2)
plt.ylabel("y = exp(x)", fontdict=font2)

# x <= 0
x = -x
y = y + np.exp(x)
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.xlabel("x(<= 0)", fontdict=font2)
plt.ylabel("y = exp(x)", fontdict=font2)

plt.suptitle("Exponential function", fontsize=20, fontfamily="serif")

plt.show()
