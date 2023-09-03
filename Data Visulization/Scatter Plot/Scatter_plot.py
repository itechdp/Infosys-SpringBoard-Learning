import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cars_df = pd.read_csv("E:\\Programming languages\\Python\\Infosys SpringBoard\\Data Visulization\\Cars93.csv")

columns = ["Manufacturer","Model","Type","Price",
"MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

ax = cars_df.plot(["Horsepower"],['MPG.city'],kind='scatter',color='black',marker='*',figsize=(10,7))

ax.set_xlabel("Horserpower")
ax.set_ylabel("MPG.City")
ax.set_title("Horsepower vs MPG.city")
plt.show()