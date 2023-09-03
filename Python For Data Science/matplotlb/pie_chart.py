# Problem Statement:
# The management of XYZ Custom Cars has decided to open a new branch and is yet to decide the location. They would like to concentrate more on the ‘origin’ of the cars to make a better decision.

# Solution:
# The details on origin of the cars and their numbers can be presented to the stakeholders visually for their easy understanding.
# Let us visualize the data using a pie chart as follows:

# Syntax:
#        ax.pie(x, labels) #ax represents axes
#        x = wedge size. one-dimensional array
#        labels = sequence of strings providing the label for wedges

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)

pie_df = pd.DataFrame()
pie_df['Count'] = df['origin'].value_counts()
pie_df = pie_df.reset_index()
pie_df.rename(columns={'index':'Country'},inplace=True)

fig = plt.figure(figsize=[8,6])
#setting axes
ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('Origin of the Cars')
#plotting pie chart
colors = ['yellowgreen', 'mediumaquamarine', 'khaki' ]
explode = [0.05, 0, 0]
ax.pie(pie_df['Count'], labels=pie_df['Country'],
        autopct='%0.1f%%',explode = explode, 
        shadow = True, startangle = 250,
        colors = colors)
plt.show()
