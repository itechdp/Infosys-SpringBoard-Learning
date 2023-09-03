import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]
cars_df[columns].head()

# Creating a box plot for the variable price
cars_df['Price'].plot(kind='box',figsize=(10,7))

# Subplot of box plot for other features
fig,(ax1,ax2) = plt.subplots(2,1)
fig.set_figwidth(10) # Setting the width for the plot
fig.set_figheight(7) # Setting the width for the plot

# Create axws objects to create boxplots alogside eachother

# The folliwng lines enable us to use subplot
ax1.boxplot(cars_df['Horsepower'],vert=False)
ax2.boxplot(cars_df['MPG.city'],vert=False)

ax1.set_title("Horsepower")
ax1.set_xlabel("Horsepower")
ax2.set_title("City Mileage")
ax2.set_xlabel("City Mileage (In miles per US Gallon)")
fig.tight_layout()
plt.show()
