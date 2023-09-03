import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
PATH = r"E:\\Programming languages\\Python\\Infosys SpringBoard\\Python For Data Science\\Pandas\\PythonForDataScienceCodeData\\auto_mpg.csv"
df = pd.read_csv(PATH)

fig = plt.figure(figsize=[10,5])
ax = fig.add_axes([0,0,1,1])
ax.scatter(df['horsepower'],df['mpg'])
ax.set_title("Scatter plot of horsepower and mileage")
ax.set_xlabel('Mileage per gallon')
ax.set_ylabel('Horsepower')

# Visualizing the correlation between mileage and horsepower based on the origin of the cars.

fig = plt.figure(figsize=[12,5])
ax = fig.add_axes([0,0,1,1])
ax.set_title("Scatter plot of horse power and mileage based on origin")
ax.set_xlabel("Mileage per gallon")
ax.set_ylabel("Horsepower")

# Assigning different colors for each origin
origin_list = df['origin'].unique()
colors = plt.jet(np.linspace(0,1,len(origin_list)))

#plotiing based on the origin
for origin,color in zip(origin_list,colors):
    x = df[df['origin'] == origin]['horsepower']
    y = df[df['origin'] == origin]['mpg']
    plt.scatter(x,y,color=color,label=origin)
plt.legend()