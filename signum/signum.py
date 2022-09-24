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
x = np.arange(-1000, 1000, step=1)

# y values
# if x < 0 => y = -1
# if x = 0 => y = 0
# if x > 0 => y = 1
y = np.sign(x)


plt.plot(x, y)
plt.title("Signum function", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y", fontdict=font2)
plt.grid()
plt.show()