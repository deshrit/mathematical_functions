import math
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

# Angles in raidan
x = [ (math.pi/180)*val for val in range(361) ]

# Cosine function
y = [ math.cos(val) for val in x ]

# plot the graph
plt.plot(x, y)
plt.grid()
plt.title("Cosine function", fontdict=font1)
plt.xlabel("x (radian)", fontdict=font2)
plt.ylabel("y = cos(x)", fontdict=font2)
plt.show()