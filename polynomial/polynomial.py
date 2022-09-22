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
x = np.arange(-15, 15,1)
# polynomial function
y = np.poly1d([1, 2, 3]) # x^2 + 2*x + 3
z = np.poly1d([-1, 4, 100]) # -x^2 + 4*x + 100

# plotting
plt.plot(x, y(x), label="x^2 + 2*x + 3", ls="-.", color="red", marker="o")
plt.plot(x, z(x), label="-x^2 + 4*x + 100", marker="*")
plt.grid()
plt.xticks(x)

plt.title("Polynomial functions", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y(x)", fontdict=font2)
plt.legend()

plt.show()