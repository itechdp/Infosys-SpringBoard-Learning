import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

# Sorting the data for line chart
cars_df = cars_df.sort_values(by="Horsepower")

# creating a blank canvas to plot 
fig,ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(7)

# Data is fed and plotted using the following lines
cars_df.plot(ax=ax,x="Horsepower",y="MPG.highway",kind='line')
cars_df.plot(ax=ax,x="Horsepower",y="MPG.city",kind='line',linestyle='--')
ax.set_ylabel("Mileage in (mile per US gallon)")
ax.set_title("Mileadge vs Horsepower")
plt.show()

