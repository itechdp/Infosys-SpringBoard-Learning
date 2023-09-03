import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

# Finding the lis of unique values of car type
car_type_list = cars_df['Type'].unique()

# Subplot of box plot for other features
fig,ax = plt.subplots()
fig.set_figwidth(10) # Setting the width for the plot
fig.set_figheight(7) # Setting the width for the plot

# Creating a bolx plot for every unique car type
ax.boxplot([cars_df['Price'][cars_df["Type"]==k]for k in car_type_list])

# Tos set the position for each plots in the iteration
plt.xticks([i for i in range(1,len(car_type_list)+1)],[k for k in car_type_list])

# Super title
fig.suptitle("Prices of car accoriding to car type")
print(car_type_list)
plt.show()
