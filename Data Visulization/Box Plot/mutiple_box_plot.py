import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]
cars_df[columns].head()

# Subplot of box plot for other features
fig,ax = plt.subplots(2,3)
fig.set_figwidth(10) # Setting the width for the plot
fig.set_figheight(7) # Setting the width for the plot

# Title
fig.suptitle("Multiple Box Plots")

# Accessing each partitiion[m][n] and providing the plot its title
ax[0][0].boxplot(cars_df['Price'][cars_df["Type"]=="Compact"])
ax[0][0].set_title("Compact")
ax[0][1].boxplot(cars_df['Price'][cars_df["Type"]=="Large"])
ax[0][1].set_title("Large")
ax[0][2].boxplot(cars_df['Price'][cars_df["Type"]=="Midsize"])
ax[0][2].set_title("Midsize")
ax[1][0].boxplot(cars_df['Price'][cars_df["Type"]=="Small"])
ax[1][0].set_title("Small")
ax[1][1].boxplot(cars_df['Price'][cars_df["Type"]=="Sporty"])
ax[1][1].set_title("Sporty")
ax[1][2].boxplot(cars_df['Price'][cars_df["Type"]=="Van"])
ax[1][2].set_title("Van")
plt.show()