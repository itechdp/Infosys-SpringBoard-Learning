# Problem Statement:
# The engineers at XYZ Custom Cars want to identify the distribution of horsepower.

# Solution
# This can be done with the help of a histogram as follows:
# Syntax:
#        ax.hist(x, bins) #ax represents axes
#        x = Input values. single array or sequence of arrays
#        bins = int or sequence or str. If bins is integer, it defines the number of equal-width bins in the range.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)

#creating a histogram for horsepower
#importing the required packages
import matplotlib.pyplot as plt
#creating an empty canvas/figure
fig = plt.figure(figsize=[8,6])
#setting axes
ax = fig.add_axes([0, 0, 1, 1])
#plotting histogram
ax.hist(df['horsepower'], bins=20)
ax.set_title('Distribution of Horsepower',fontsize = 17)
ax.set_ylabel('Frequency',fontsize=12)
ax.set_xlabel('Horsepower',fontsize=12)
plt.show()