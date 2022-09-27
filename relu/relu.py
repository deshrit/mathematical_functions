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
x = np.arange(-40, 40)

# relu output
y = [ a if(a > 0) else 0 for a in x]

# plotting the values
plt.plot(x, y)
plt.title("Relu function", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y(x)", fontdict=font2)
plt.grid()
plt.show()