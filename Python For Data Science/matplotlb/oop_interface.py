# We can also create the plotting elements using object oriented approach. The use of an object-oriented approach is recommended as it gives more control over customization of the plots.

# Now, let us recreate the plot using object oriented approach following the below steps:

# Creating a figure
# Setting up the axes
# Creating a plot using the axes object
# Creating multiple plots using the same axes object
# Setting up the title, label, and legend for a plot
# Creating sample data for plotting as below:
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,16)
y = x**2
z = (y/2)+40

# creating a object of canvas 
fig = plt.figure()

# <Figure size 432x288 with 0 Axes>

# Setting the aces for the figure
# The axes object is the region where the data can be plotted. A figure can have n number of axes object. 

# settin gaces as [left,botton,width,height]
ax = fig.add_axes([0,0,1,1])

# Plotting a line on the axes

# Syntax:

#        ax.plot(x, y, color, label) #ax represents axes

#        x = data on the horizontal axis

#        y = data on the vertical axis

# Plotting the lines 
ax.plot(x,y,color='g',label='line1')

# Plotting multiple lines on the axes
ax.plot(x,y,color='b',label='line2')
ax.plot(x,y,color='r',label='line3')

# Setting the title for the plot and the labels for the axes.

#creating an empty canvas/figure
fig = plt.figure()
#setting axes
ax = fig.add_axes([0,0,1,1])
#plotting the lines
ax.plot(x,y,color="g", label='line1' )
ax.plot(x,z,color="r", label='line2')
ax.set_title('Title of the Plot',fontsize=15)    #setting title
ax.set_xlabel('Label for X axis',fontsize=15)    # setting X label
ax.set_ylabel('Label for Y axis',fontsize=15)    # setting Y _label

# Adding legend
ax.legend()
plt.show()