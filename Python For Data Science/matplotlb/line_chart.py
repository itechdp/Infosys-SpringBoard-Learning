# Problem Statement:
# XYZ Custom Cars is planning to generate a report comparing the Mileage, Horsepower, and Weight of the cars manufactured in different years, starting from 1970 to 1982.

# Solution:
# As a data analyst, a line chart can be created to visualize the relationship between mileage, horsepower, and the weight of the cars manufactured in different years.

# Let us create a DataFrame containing the mean values of mileage, horsepower and the weight of the cars based on the model year.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)

line_df = df.groupby(by=['model_year'])
line_df = line_df.mean()

#importing the required packages
import matplotlib.pyplot as plt
#creating an empty canvas/figure
fig = plt.figure(figsize=[8,4])
#setting axes
ax = fig.add_axes([0, 0, 1, 1])
#plotting the lines
ax.plot(line_df['mpg']/10,label='Mileage /10',linestyle='-',linewidth=2)
ax.plot(line_df['weight']/1000,label='Weight /1000',linestyle=':',linewidth=3)
ax.plot(line_df['horsepower']/100,label='Horsepower /100',linestyle='--',linewidth=3)

ax.set_title('Mileage vs Weight vs Horsepower',fontsize = 17)
ax.set_ylabel('Value',fontsize=12)
ax.set_xlabel('Model year',fontsize=12)
ax.legend()

# Linestyle
# Matplotlib supports several line styles such as solid line, dashed line (-----), dotted line (…..), dashdot (-.-.-.-) etc. In addition to color and linestyle, the width of the line can be customized to get a unique plot.

# Below is a small example of how linestyle, width, and color can be used.
