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



x = np.arange(-5, 5, 0.25)
y = np.zeros(x.shape, dtype=np.float64)
y = y + np.exp(x)
plt.plot(x, y)
plt.title("Exponential function", fontdict=font1)
plt.grid(axis="x")
plt.xlabel("x", fontdict=font2)
plt.ylabel("y = exp(x)", fontdict=font2)
plt.show()
