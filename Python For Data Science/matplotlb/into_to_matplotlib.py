import matplotlib.pyplot as plt
import numpy as np
# plt' is the standard alias used for pyplot module of Matplotlib.
# creating two arrays
X = np.array([1,2,3,4,5])
y = X**2

# Now, let us plot the values using matplotlib.pyplot.

# Syntax:

#        plt.plot(x, y)

#        x = data on the horizontal axis

#        y = data on the vertical axis 

# plotting
plt.plot(X,y)
plt.show()