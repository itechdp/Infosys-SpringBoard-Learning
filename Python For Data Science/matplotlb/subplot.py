import numpy as np
import matplotlib.pyplot as plt

#creating sample data for plotting
x = np.arange(1,16)    #1 … 15
y = x**2    #square of x values
z = (y/2)+40    #arithmetic operation applied to y values

#initializing two axes for the subplot
fig, (ax1, ax2) = plt.subplots(1, 2)    
ax1.plot(x,y,color="g", label='line1' )
ax1.set_title('Title for Plot 1',fontsize=15)    #setting title
ax1.set_xlabel('Plot 1 - X axis',fontsize=15)    # setting X label
ax1.set_ylabel('Plot 1 - Y axis',fontsize=15)    # setting Y _label
ax2.plot(x,z,color="r", label='line2')
ax2.set_title('Title for Plot 2',fontsize=15)    #setting title
ax2.set_xlabel('Plot 2 - X axis',fontsize=15)    # setting X label
ax2.set_ylabel('Plot 2 - Y axis',fontsize=15)    # setting Y _label
fig.tight_layout()