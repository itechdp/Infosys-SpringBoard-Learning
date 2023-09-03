import numpy as np 
import matplotlib.pyplot as plt

# Creating a simple data for plotting 
x = np.arange(1,16)
y = x**2
z = (y/2)+40

# creating simple canvas 
fig = plt.figure(figsize=(8,5))

# Setting axes as [left,bottom,width,height]
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.10,0.42,0.45,0.45])

# Plotting the lines 
ax1.plot(x,y,color='g',label='line1')
ax1.set_title('Title for plot 1',fontsize=15)
ax1.set_xlabel('Plot 1 X axis',fontsize=15)
ax1.set_ylabel('Plot 1 y axis',fontsize=15)


ax2.plot(x,y,color='r',label='line2')
ax2.set_title('Title for plot 2',fontsize=15)
ax2.set_xlabel('Plot 2 X axis',fontsize=15)
ax2.set_ylabel('Plot 2 y axis',fontsize=15)

ax1.legend()
ax2.legend()

plt.show()