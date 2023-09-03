# Problem Statement:
# The engineers at XYZ Custom Cars want to know the number of cars released in each year. 

# Solution:
# A bar graph can be created for this problem as shown below:

# Syntax:
# ax.scatter(x, height, width, bottom, align) #ax represents axes
# x = data on the horizontal axis
# height = height of the bar
# weight= weight of the bar. default:0.8
# bottom=Y coordinates of bar bases. default:0
# align = alignment of the bars to x coordinates. default value: 'center'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)

grouped_df = df.groupby(['model_year']).count()[['name']] 
grouped_df.reset_index()

fig = plt.figure(figsize=[7,5])
ax = fig.add_axes([0,0,1,1])
ax.set_title("Number of cars each year")
ax.set_xlabel("Model Year")
ax.set_ylabel("Number of cars")
ax.bar(grouped_df['model_year'],grouped_df['name'])
plt.show()