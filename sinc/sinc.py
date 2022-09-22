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
x = np.linspace(-20, 20, 500)
# sinc funtion
y = np.sin(x) / x

# normalized sinc
z = np.sin(np.pi * x) / (np.pi*x)

plt.plot(x, y, label="sin(x)/x")
plt.plot(x, z, color="red", label="sin(pi*x)/(pi*x)")
plt.title("Sinc function", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y(x)", fontdict=font2)
plt.legend()
plt.show()