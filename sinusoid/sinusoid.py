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

# Sinusoid function
y = [ math.sin(val) for val in x ]

# Plot the graph
plt.plot(x, y)
plt.grid()
plt.title("Sine function", fontdict=font1)
plt.xlabel("x (radian)", fontdict=font2)
plt.ylabel("y = sin(x)", fontdict=font2)
plt.show()