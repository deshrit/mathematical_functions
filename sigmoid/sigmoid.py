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


# x values
x = np.linspace(-10, 10, 100)

# sigmoid function
y = 1 / (1 + np.e**(-x))


# ploting the graph
plt.plot(x, y, label="1/(1 + e^(-x))", c="r")
plt.title("Sigmoid function", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y(x)", fontdict=font2)
plt.grid()
plt.legend()
plt.show()