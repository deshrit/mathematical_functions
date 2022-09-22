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


# values
x = np.linspace(0.1, 15, 50)
y = np.log(x)

plt.plot(x, y, marker="x", label="loge")
plt.grid(axis="y")
plt.yticks(y)

plt.title("Logarithmic function", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y = loge(x)", fontdict=font2)
plt.legend(loc="center right")

plt.show()
